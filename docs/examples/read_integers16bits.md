# Exemplo – Leitura de Inteiros de 16 Bits

Este exemplo demonstra como realizar a **leitura de valores inteiros de 16 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT16)** e **valores com sinal (INT16)**.

A leitura de inteiros de 16 bits é comum em aplicações industriais para leitura de contadores, estados codificados e variáveis analógicas simples.

---

## Cenário típico

- Leitura de contadores
- Leitura de estados codificados em registradores
- Leitura de valores analógicos inteiros
- Monitoramento de variáveis internas de CLPs

Neste exemplo, será realizada a leitura a partir do **Holding Register no endereço 100**.

---

## Importações

```py
from pyModbusTCPtools import (
    ModbusTCPResiliente,
    ModbusDataType
)
```

---

## Criação do cliente

```py
client = ModbusTCPResiliente(
    host="192.168.0.10",
    unit_id=1,
    timeout=3.0,
    console=True
)
```

---

## Leitura de inteiro de 16 bits sem sinal (UINT16)

```py
valor_uint16 = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.UINT16
)

if valor_uint16 is not None:
    print(f"UINT16 lido: {valor_uint16}")
else:
    print("Falha na leitura do UINT16")
```

---

## Leitura de inteiro de 16 bits com sinal (INT16)

```py
valor_int16 = client.read_holding_typed_safe(
    addr=101,
    dtype=ModbusDataType.INT16
)

if valor_int16 is not None:
    print(f"INT16 lido: {valor_int16}")
else:
    print("Falha na leitura do INT16")
```

---

## Diferença entre INT16 e UINT16

- `UINT16` representa valores no intervalo de **0 a 65535**
- `INT16` representa valores no intervalo de **-32768 a 32767**
- A conversão é realizada automaticamente pela biblioteca
- Nenhuma manipulação manual de bits é necessária

---

## Comportamento dos métodos

Os métodos de leitura tipada possuem o seguinte comportamento:

- Retornam o valor convertido em caso de sucesso
- Retornam `None` em caso de falha
- Realizam reconexão automática se necessário
- Aplicam backoff exponencial em falhas consecutivas
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Certifique-se do tipo correto configurado no dispositivo Modbus
- Não confunda valores com e sem sinal
- Sempre valide o retorno antes de utilizar o valor

---

## Encerrando a conexão

Após finalizar as leituras, a conexão pode ser encerrada explicitamente:

```py
client.close()
```
