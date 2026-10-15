"""Direct stream cases for partial prompts, disconnection, timeouts and limits."""

import importlib.util
import io
from pathlib import Path
import socket
import threading
import unittest


spec = importlib.util.spec_from_file_location(
    "inventory", Path(__file__).resolve().parents[1] / "scripts/flipper_inventory.py"
)
inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)


class PromptCaptureTests(unittest.TestCase):
    def setUp(self):
        self.reader, self.writer = socket.socketpair()
        self.addCleanup(self.reader.close)
        self.addCleanup(self.writer.close)
        self.output = io.BytesIO()

    def test_fragmented_prompt_retains_exact_wire_bytes(self):
        first = b"device_info\r\nfirmware_version: 0.81.1\r\n>"
        self.writer.sendall(first)
        timer = threading.Timer(0.02, self.writer.sendall, args=(b": ",))
        timer.start()
        try:
            actual = inventory.read_prompt(self.reader.fileno(), self.output, timeout=1)
        finally:
            timer.join()
        self.assertEqual(actual, first + b": ")
        self.assertEqual(self.output.getvalue(), actual)

    def test_disconnect_preserves_partial_response(self):
        self.writer.sendall(b"unfinished")
        self.writer.shutdown(socket.SHUT_WR)
        with self.assertRaises(ConnectionError):
            inventory.read_prompt(self.reader.fileno(), self.output, timeout=1)
        self.assertEqual(self.output.getvalue(), b"unfinished")

    def test_timeout_does_not_accept_embedded_prompt(self):
        self.writer.sendall(b"text >: value\r\n")
        with self.assertRaises(TimeoutError):
            inventory.read_prompt(self.reader.fileno(), self.output, timeout=0.03)
        self.assertEqual(self.output.getvalue(), b"text >: value\r\n")

    def test_response_limit_raises_and_retains_received_bytes(self):
        self.writer.sendall(b"0123456789")
        with self.assertRaises(ValueError):
            inventory.read_prompt(self.reader.fileno(), self.output, timeout=1, limit=8)
        self.assertEqual(self.output.getvalue(), b"012345678")


class InventoryProfileTests(unittest.TestCase):
    def test_matching_clean_historical_identity(self):
        inventory.require_inventory_profile(
            b"device_info\r\nfirmware_commit : 1af02211\r\n"
            b"firmware_version : 0.81.1\r\nfirmware_commit_dirty : false\r\n>: "
        )

    def test_mismatched_or_incomplete_identity_stops_before_storage(self):
        for response in (
            b"firmware_commit: 3fb1d517\nfirmware_version: 1.5.1\nfirmware_commit_dirty: false",
            b"firmware_commit: 1af02211\nfirmware_version: 0.81.1\nfirmware_commit_dirty: true",
            b"device_info\r\n>: ",
        ):
            with self.subTest(response=response), self.assertRaises(RuntimeError):
                inventory.require_inventory_profile(response)


if __name__ == "__main__":
    unittest.main()
