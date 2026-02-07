# Release Checklist

## Pre-release
- [ ] Update version in `pyproject.toml`.
- [ ] Review the `CHANGELOG.md` for accuracy and completeness.
- [ ] Run the test suite:
  - [ ] `PYTHONPATH=src python -m unittest discover -s tests`
- [ ] Validate any compatibility notes (e.g., UINT64 LE register ordering) against target devices.
- [ ] Ensure README instructions are up to date.

## Release
- [ ] Tag the release (e.g., `v0.2.0`).
- [ ] Build artifacts:
  - [ ] `python -m build`
- [ ] Publish to PyPI:
  - [ ] `python -m twine upload dist/*`

## Post-release
- [ ] Verify PyPI page metadata and README rendering.
- [ ] Announce release notes with the changelog summary.
