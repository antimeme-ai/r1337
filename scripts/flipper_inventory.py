#!/usr/bin/env python3
"""Capture Flipper CLI inventory metadata using only Python's standard library."""

import argparse
import array
from datetime import datetime, timezone
import fcntl
from pathlib import Path
import os
import re
import select
import shutil
import subprocess
import termios
import time
import tty


PROMPT = re.compile(rb"(?:^|\n)>: $")
QUERIES = (
    "info power",
    "storage info /int",
    "storage info /ext",
    "free",
    "date",
)


def require_inventory_profile(response):
    fields = {}
    for line in response.decode("ascii", errors="replace").splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    expected = {
        "firmware_commit": "1af02211",
        "firmware_version": "0.81.1",
        "firmware_commit_dirty": "false",
    }
    if any(fields.get(key) != value for key, value in expected.items()):
        raise RuntimeError("Firmware differs from the source-reviewed 0.81.1 profile; stopping")


def require_sole_owner(port):
    executable = shutil.which("lsof")
    if not executable:
        raise RuntimeError("Native lsof is required to check for an existing serial owner")
    paths = [str(port)]
    if port.name.startswith("cu."):
        paths.append(str(port.with_name("tty." + port.name[3:])))
    elif port.name.startswith("tty."):
        paths.append(str(port.with_name("cu." + port.name[4:])))
    result = subprocess.run(
        [executable, "-t", "--", *paths], capture_output=True, text=True, timeout=5
    )
    lines = result.stdout.splitlines()
    # lsof returns 1 when the unused cu/tty alias has no matching open descriptor.
    # Our own PID must still appear, and diagnostics or invalid output fail closed.
    if result.returncode not in (0, 1) or result.stderr.strip() or not lines or not all(
        line.isdecimal() for line in lines
    ):
        raise RuntimeError("Could not establish the serial port's existing owners with lsof")
    if {int(line) for line in lines} != {os.getpid()}:
        raise RuntimeError("Another process already holds the serial port; stopping")


def read_prompt(fd, destination, timeout=8.0, limit=262144):
    """Retain received bytes, including partial output when a query fails."""
    deadline = time.monotonic() + timeout
    received = bytearray()
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("CLI prompt did not arrive before the deadline")
        ready, _, _ = select.select([fd], [], [], remaining)
        if not ready:
            raise TimeoutError("CLI prompt did not arrive before the deadline")
        block = os.read(fd, min(8192, limit + 1 - len(received)))
        if not block:
            raise ConnectionError("Device disconnected before returning a prompt")
        destination.write(block)
        destination.flush()
        received.extend(block)
        if len(received) > limit:
            raise ValueError("CLI response exceeds the capture limit")
        if PROMPT.search(received):
            return bytes(received)


def capture(port, output):
    output.mkdir(parents=True, exist_ok=False)
    fd = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    old = None
    old_modem = None
    exclusive = False
    try:
        fcntl.ioctl(fd, termios.TIOCEXCL)
        exclusive = True
        require_sole_owner(port)
        old = termios.tcgetattr(fd)
        modem = array.array("i", [0])
        fcntl.ioctl(fd, termios.TIOCMGET, modem, True)
        old_modem = modem
        # Opening CDC may already emit a banner while lsof runs; keep queued bytes.
        tty.setraw(fd, when=termios.TCSANOW)
        attrs = termios.tcgetattr(fd)
        attrs[4] = attrs[5] = termios.B115200
        attrs[2] |= termios.CLOCAL | termios.CREAD
        termios.tcsetattr(fd, termios.TCSANOW, attrs)
        fcntl.ioctl(fd, termios.TIOCMBIS, array.array("i", [termios.TIOCM_DTR]))
        with (output / "00-banner.raw").open("xb") as stream:
            read_prompt(fd, stream)
        queries = ("help", "device_info", *QUERIES)
        for index, command in enumerate(queries, 1):
            payload = command.encode("ascii") + b"\r"
            path = output / f"{index:02}-{command.replace(' ', '_').replace('/', '')}.raw"
            with path.open("xb") as stream:
                if os.write(fd, payload) != len(payload):
                    raise OSError("Short CLI command write")
                response = read_prompt(fd, stream)
            if b"unknown command" in response.lower() or b"usage:" in response.lower():
                raise RuntimeError(f"Installed CLI did not accept {command!r}; inspect capture")
            if command == "device_info":
                require_inventory_profile(response)
        (output / "commands.txt").write_text("\n".join(queries) + "\n")
    finally:
        try:
            try:
                if old_modem is not None:
                    operation = termios.TIOCMBIS if old_modem[0] & termios.TIOCM_DTR else termios.TIOCMBIC
                    fcntl.ioctl(fd, operation, array.array("i", [termios.TIOCM_DTR]))
            finally:
                try:
                    if old is not None:
                        termios.tcsetattr(fd, termios.TCSANOW, old)
                finally:
                    if exclusive:
                        fcntl.ioctl(fd, termios.TIOCNXCL)
        finally:
            os.close(fd)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=Path, help="macOS cu.usbmodemflip_* device")
    parser.add_argument("--output", type=Path, help="new private capture directory")
    args = parser.parse_args()
    ports = [args.port] if args.port else list(Path("/dev").glob("cu.usbmodemflip_*"))
    if len(ports) != 1:
        parser.error("select exactly one connected Flipper with --port")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    output = args.output or Path("context") / f"inventory-{stamp}"
    try:
        capture(ports[0], output)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        parser.exit(1, f"Inventory failed: {error}. Partial captures: {output}\n")
    print(f"Inventory captured in {output}; output contains private device identifiers.")


if __name__ == "__main__":
    main()
