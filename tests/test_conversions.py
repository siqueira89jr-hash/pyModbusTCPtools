import math
import unittest

from pyModbusTCPtools import Endian, ModbusTCPResiliente


class TestModbusConversions(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ModbusTCPResiliente(host="127.0.0.1")

    def test_int16_roundtrip(self) -> None:
        value = -12345
        reg = self.client._int16_to_reg(value)
        self.assertEqual(value, self.client._reg_to_int16(reg))

    def test_uint32_roundtrip_all_endians(self) -> None:
        value = 0x12345678
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._uint32_to_regs(value, endian)
            self.assertEqual(value, self.client._regs_to_uint32(regs, endian))

    def test_int32_roundtrip_all_endians(self) -> None:
        value = -12345678
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._int32_to_regs(value, endian)
            self.assertEqual(value, self.client._regs_to_int32(regs, endian))

    def test_uint64_roundtrip_all_endians(self) -> None:
        value = 0x1122334455667788
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._uint64_to_regs(value, endian)
            self.assertEqual(value, self.client._regs_to_uint64(regs, endian))

    def test_int64_roundtrip_all_endians(self) -> None:
        value = -0x1122334455667788
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._int64_to_regs(value, endian)
            self.assertEqual(value, self.client._regs_to_int64(regs, endian))

    def test_float32_roundtrip_all_endians(self) -> None:
        value = 12.345
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._float32_to_regs(value, endian)
            result = self.client._regs_to_float32(regs, endian)
            self.assertTrue(math.isclose(value, result, rel_tol=1e-6))

    def test_float64_roundtrip_all_endians(self) -> None:
        value = 12.3456789012345
        for endian in (Endian.BE, Endian.LE, Endian.BE_SWAP, Endian.LE_SWAP):
            regs = self.client._float64_to_regs(value, endian)
            result = self.client._regs_to_float64(regs, endian)
            self.assertTrue(math.isclose(value, result, rel_tol=1e-12))


if __name__ == "__main__":
    unittest.main()
