# Changelog

Todas as mudanças relevantes do projeto **pyModbusTCPtools** serão documentadas neste arquivo.

Este projeto segue as boas práticas de versionamento semântico (**Semantic Versioning – SemVer**):

- `MAJOR`: mudanças incompatíveis na API
- `MINOR`: adição de funcionalidades compatíveis
- `PATCH`: correções de bugs e ajustes internos

---

## [Unreleased]

### Planejado

- Consolidação final da API pública
- Revisão completa de testes automatizados
- Otimizações internas de robustez
- Preparação para release estável 1.0.0

---

## [0.1.0] – 2026-01-18

### Adicionado

- Classe `ModbusTCPResiliente` como cliente Modbus TCP principal
- Leitura segura de Coils (`read_coils_safe`)
- Escrita segura de Coils (`write_single_coil_safe`, `write_multiple_coils_safe`)
- Leitura de Discrete Inputs (`read_discrete_inputs_safe`)
- Leitura de Holding Registers (bruto)
- Escrita de Holding Registers (bruto)
- Leitura tipada de registradores:
  - INT16 / UINT16
  - INT32 / UINT32
  - INT64 / UINT64
  - FLOAT32
  - FLOAT64
- Escrita tipada de registradores:
  - INT16 / UINT16
  - INT32 / UINT32
  - INT64 / UINT64
  - FLOAT32
  - FLOAT64
- Suporte completo a endianness:
  - Big Endian
  - Little Endian (word swap)
  - Byte swap
  - Word + byte swap
- Reconexão automática com backoff exponencial
- Cache interno de endereços Modbus inválidos
- Logging estruturado com opção de console e arquivo
- Enums públicos:
  - `Endian`
  - `ModbusDataType`
- Exceções específicas:
  - `ModbusConnectionError`
  - `ModbusProtocolError`
  - `ModbusReadError`
  - `ModbusWriteError`
  - `ModbusConversionError`

### Documentação

- Documentação completa com MkDocs + Material
- Seção de conceitos:
  - Fundamentos do Modbus
  - Endianness
  - Tratamento de erros
- Documentação da API:
  - Client
  - Enums
  - Exceptions
- Exemplos práticos:
  - Leitura e escrita de Coils
  - Discrete Inputs
  - Leitura e escrita de INT16 / INT32 / INT64
  - Leitura e escrita de FLOAT32 / FLOAT64
  - Reconexão automática

### Infraestrutura

- Estrutura de projeto compatível com PyPI
- Suporte a Python 3.8+
- Licença MIT

---

## Notas

- A versão `0.1.0` é considerada **funcional**, porém ainda em evolução
- Mudanças de API podem ocorrer até a versão `1.0.0`
- Recomenda-se fixar versão em ambientes de produção

---

## Links

- Repositório: https://github.com/siqueira89jr-hash/pyModbusTCPtools
- Documentação: https://siqueira89jr-hash.github.io/pyModbusTCPtools
