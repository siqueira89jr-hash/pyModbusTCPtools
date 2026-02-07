# pyModbusTCPtools

**pyModbusTCPtools** é uma biblioteca Python focada em **comunicação Modbus TCP resiliente**, projetada para uso em **ambientes industriais reais**.

O objetivo da biblioteca é fornecer uma API clara, segura e robusta para leitura e escrita Modbus TCP, evitando código repetitivo, frágil ou improvisado comumente encontrado em aplicações industriais.

---

## Principais características

- Cliente Modbus TCP resiliente
- Reconexão automática com backoff exponencial
- Reconexão automática com backoff exponencial e jitter
- Leitura e escrita segura de Coils e Discrete Inputs
- Leitura e escrita de Holding Registers e Input Registers
- Leitura e escrita **tipada**:
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
- Cache interno de endereços Modbus inválidos
- API pública para limpeza/inspeção do cache de endereços inválidos
- Exceções explícitas e bem definidas
- Logging estruturado
- Compatível com Python 3.8+
- API com type hints para melhor integração com IDEs e análise estática

---

## O que a biblioteca não é

Para evitar ambiguidades, **pyModbusTCPtools não é**:

- Uma API REST
- Um servidor Modbus
- Um SCADA
- Um framework genérico de automação

Trata-se de uma **biblioteca cliente Modbus TCP**, voltada exclusivamente à comunicação e conversão de dados.

---

## Instalação

Instalação via pip:

```bash
pip install pyModbusTCPtools
```

Instalação local a partir de wheel:

```bash
pip install pyModbusTCPtools-0.1.0-py3-none-any.whl
```

---

## Exemplo rápido

Leitura de um valor FLOAT32 a partir de Holding Registers:

```python
from pyModbusTCPtools import ModbusTCPResiliente, ModbusDataType, Endian

client = ModbusTCPResiliente(
    host="192.168.0.10",
    unit_id=1,
    timeout=3.0
)

valor = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if valor is not None:
    print(f"Valor lido: {valor}")
```

---

## Filosofia de projeto

A biblioteca foi desenvolvida com foco em:

- Robustez em ambientes industriais
- Tratamento explícito de falhas
- Reconexão automática sem intervenção do usuário
- API previsível e estável
- Compatibilidade com evolução futura

Falhas de comunicação são tratadas como **eventos normais**, não como exceções fatais.

---

## Documentação

A documentação completa inclui:

- Guia de instalação
- Quickstart
- Conceitos de Modbus e endianness
- Documentação da API
- Exemplos práticos de leitura, escrita e reconexão

Documentação online:

https://siqueira89jr-hash.github.io/pyModbusTCPtools

---

## Cache de endereços inválidos

Além do cache interno, a biblioteca expõe helpers para inspeção e limpeza:

- `clear_invalid_cache()` limpa o cache.
- `get_invalid_cache_snapshot()` retorna os endereços atualmente em quarentena.

---

## Testes

Para executar a suíte de testes:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

---

## Nota de compatibilidade

Para `UINT64` com `Endian.LE`/`Endian.LE_SWAP`, a ordem de registradores foi ajustada para alinhar o roundtrip
de encode/decode. Se sua aplicação dependia da ordem anterior, valide com o equipamento.

---

## Requisitos

- Python 3.8 ou superior
- Rede TCP/IP com acesso ao dispositivo Modbus
- Dispositivo compatível com Modbus TCP

---

## Licença

Este projeto é distribuído sob a licença **MIT**, permitindo uso comercial e industrial sem restrições.

---

## Status do projeto

- Versão atual: **0.1.0**
- Estável para uso funcional
- API ainda pode evoluir até a versão 1.0.0

---

## Contribuição

Contribuições são bem-vindas.

Sugestões, issues e pull requests podem ser enviados via GitHub.

---

## Autor

Jocivaldo Siqueira da Silva Júnior
