# API – Exceções

Esta seção documenta as exceções públicas utilizadas pela biblioteca **pyModbusTCPtools**.

As exceções permitem identificar claramente a causa de uma falha durante a comunicação Modbus TCP, diferenciando problemas de conexão, protocolo, leitura, escrita e conversão de dados.

---

## Hierarquia de exceções

Todas as exceções da biblioteca herdam da classe base `ModbusError`.

```text
ModbusError
├── ModbusConnectionError
├── ModbusProtocolError
├── ModbusReadError
├── ModbusWriteError
└── ModbusConversionError
```

---

## ModbusError

Classe base para todas as exceções relacionadas ao Modbus.

Uso típico:

- Captura genérica de erros da biblioteca
- Tratamento comum de falhas Modbus

---

## ModbusConnectionError

Indica falha de conexão TCP ou perda de comunicação com o dispositivo Modbus.

Causas comuns:

- Dispositivo desligado
- Cabo de rede desconectado
- Timeout de comunicação
- Socket encerrado inesperadamente

Esse erro indica um problema de **transporte**, não de aplicação Modbus.

---

## ModbusProtocolError

Indica que o dispositivo respondeu com uma **exceção do protocolo Modbus**.

Exemplos de exceções Modbus:

- Illegal Function
- Illegal Data Address
- Illegal Data Value

Características:

- A conexão TCP pode continuar ativa
- O erro indica problema de endereçamento ou função inválida
- Pode ser cacheado internamente pela biblioteca

---

## ModbusReadError

Indica falha durante uma operação de leitura Modbus.

Pode ocorrer quando:

- Não há resposta válida do dispositivo
- O dispositivo retorna dados inconsistentes
- O cliente Modbus falha sem exceção explícita

---

## ModbusWriteError

Indica falha durante uma operação de escrita Modbus.

Pode ocorrer quando:

- O dispositivo rejeita a escrita
- A escrita não é confirmada
- O socket falha durante a operação

---

## ModbusConversionError

Indica erro durante a conversão de dados Modbus para tipos Python.

Causas comuns:

- Valor fora do range do tipo
- Quantidade incorreta de registradores
- Endianness incompatível
- Valor inválido para FLOAT ou DOUBLE

Esse erro indica um problema de **interpretação de dados**, não de comunicação.

---

## Uso típico das exceções

Em aplicações avançadas, exceções podem ser capturadas explicitamente para controle fino do fluxo.

```py
from pyModbusTCPtools.exceptions import (
    ModbusConnectionError,
    ModbusProtocolError,
    ModbusConversionError
)

try:
    valor = client.read_holding_typed_safe(
        addr=100,
        dtype=ModbusDataType.FLOAT32
    )
except ModbusProtocolError as exc:
    print(f"Erro de protocolo Modbus: {exc}")
except ModbusConnectionError as exc:
    print(f"Falha de conexão: {exc}")
except ModbusConversionError as exc:
    print(f"Erro de conversão: {exc}")
```

---

## Boas práticas

- Diferencie erros de conexão de erros de protocolo
- Trate exceções conforme a criticidade do erro
- Não ignore exceções silenciosamente
- Utilize logs para diagnóstico em produção
- Evite capturar exceções genéricas sem análise

---

## Próximo passo

Após compreender as exceções disponíveis, retorne à documentação da API para consolidar o uso da biblioteca ou avance para os exemplos práticos.