# Changelog

## 0.2.0

### Added
- Unit tests for INT/UINT/FLOAT conversions across all supported endian variants.
- Public helpers to clear and inspect the invalid-address cache.
- Jittered backoff for reconnect attempts.
- Type hints on public Modbus client methods.

### Changed
- UINT64 register ordering for `Endian.LE`/`Endian.LE_SWAP` to align encode/decode roundtrips.

### Notes
- If your application relied on the previous UINT64 LE register order, validate with your device.