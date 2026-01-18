$ProjectRoot = "pyModbusTCPtools"

Write-Host "Criando estrutura do projeto $ProjectRoot..."

$paths = @(
    "docs/concepts",
    "docs/api",
    "docs/examples",
    "src/pyModbusTCPtools",
    "tests"
)

foreach ($path in $paths) {
    New-Item -ItemType Directory -Force -Path "$ProjectRoot/$path" | Out-Null
}

$files = @(
    "docs/index.md",
    "docs/installation.md",
    "docs/quickstart.md",
    "docs/changelog.md",
    "docs/concepts/modbus_basics.md",
    "docs/concepts/endianness.md",
    "docs/concepts/error_handling.md",
    "docs/api/client.md",
    "docs/api/enums.md",
    "docs/api/exceptions.md",
    "docs/examples/read_coils.md",
    "docs/examples/read_registers.md",
    "docs/examples/typed_reads.md",
    "docs/examples/typed_writes.md",
    "docs/examples/reconnection.md",
    "src/pyModbusTCPtools/__init__.py",
    "src/pyModbusTCPtools/modbustools.py",
    "src/pyModbusTCPtools/enums.py",
    "src/pyModbusTCPtools/exceptions.py",
    "tests/test_import.py",
    "mkdocs.yml",
    "README.md",
    "pyproject.toml",
    "LICENSE"
)

foreach ($file in $files) {
    New-Item -ItemType File -Force -Path "$ProjectRoot/$file" | Out-Null
}

Write-Host "Estrutura criada com sucesso!"
