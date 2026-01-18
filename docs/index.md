# pyModbusTCPtools

**pyModbusTCPtools** é uma biblioteca Python focada em **comunicação Modbus TCP resiliente**, projetada para uso em **ambientes industriais reais**, onde instabilidade de rede, reconexões automáticas e conversões de dados confiáveis são requisitos básicos.

A biblioteca adiciona uma camada robusta sobre o protocolo Modbus TCP tradicional, oferecendo:

- Leitura e escrita tipada (INT, UINT, FLOAT, DOUBLE)
- Suporte avançado a endianness e word/byte swap
- Operações seguras com reconexão automática
- Tratamento consistente de exceções
- Cache inteligente de endereços inválidos
- API clara, explícita e orientada à produção

---

## Objetivo da biblioteca

O objetivo do **pyModbusTCPtools** é fornecer uma **API confiável e reutilizável** para comunicação Modbus TCP em Python, evitando código repetitivo, frágil e difícil de manter, comum em aplicações industriais.

Ela foi projetada para ser utilizada em:

- Supervisórios web (Streamlit, Flask, FastAPI)
- Sistemas embarcados (Raspberry Pi)
- Gateways industriais
- Serviços de coleta de dados
- Integrações OT/IT
- Scripts de controle, monitoramento e diagnóstico

---

## Princípios de projeto

A biblioteca segue princípios técnicos claros:

- Fail-safe: falhas de comunicação são tratadas explicitamente
- Reconexão automática com backoff exponencial
- API explícita e previsível
- Nenhuma operação silenciosa ou implícita
- Foco em estabilidade e compatibilidade de API
- Projeto orientado a uso industrial real

---

## O que a biblioteca não é

Para evitar interpretações incorretas, o pyModbusTCPtools **não é**:

- Uma API REST
- Um servidor Modbus
- Um sistema SCADA
- Uma abstração genérica de CLPs
- Um substituto de plataformas SCADA comerciais

Trata-se de uma **biblioteca cliente Modbus TCP**, voltada exclusivamente à comunicação, conversão e confiabilidade de dados.

---

## Funcionalidades principais

### Comunicação Modbus TCP

- Coils
- Discrete Inputs
- Input Registers
- Holding Registers

### Leitura e escrita tipada

- INT16 / UINT16
- INT32 / UINT32
- INT64 / UINT64
- FLOAT32
- FLOAT64 (DOUBLE)

### Endianness suportado

- Big Endian (padrão Modbus)
- Little Endian (word swap)
- Big Endian com byte swap
- Little Endian com byte swap

### Robustez operacional

- Reconexão automática
- Backoff exponencial configurável
- Verificação ativa de conexão
- Cache de endereços inválidos (Illegal Data Address)
- Logging estruturado

---

## Estrutura da API

O núcleo da biblioteca é a classe:

**ModbusTCPResiliente**

Ela fornece métodos explícitos para:

- Leitura segura (métodos com sufixo _safe)
- Escrita segura (métodos com sufixo _safe)
- Leitura tipada de registradores
- Escrita tipada de registradores
- Conversão automática de dados Modbus

Os comportamentos de endianness e tipos são controlados por enums:

- Endian
- ModbusDataType

As exceções específicas permitem distinguir claramente:

- Erros de conexão
- Erros de protocolo Modbus
- Erros de leitura e escrita
- Erros de conversão de dados

---

## Exemplo rápido
```py

from pyModbusTCPtools import ModbusTCPResiliente, Endian, ModbusDataType

client = ModbusTCPResiliente(
    host="192.168.0.10",
    unit_id=1,
    timeout=3.0,
    console=True
)

temperatura = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if temperatura is not None:
    print(f"Temperatura: {temperatura:.2f} °C")
```

---

## Instalação

### Instalação via pip:
```bash
pip install pyModbusTCPtools
```

### Instalação local a partir de pacote wheel:
```bash
pip install pyModbusTCPtools-0.1.0-py3-none-any.whl
```

---

## Próximos passos na documentação
A leitura recomendada da documentação segue a seguinte ordem:

1. Instalação
2. Quickstart
3. Conceitos (Modbus, endianness e tratamento de erros)
4. API (documentação da classe pública)
5. Exemplos de uso

---

## Roadmap
- Consolidação da API pública
- Expansão de exemplos industriais
- Ampliação da cobertura de testes
- Lançamento da versão 1.0.0 estável

## Licença

Este projeto é distribuído sob a licença MIT, permitindo uso comercial e industrial sem restrições.

