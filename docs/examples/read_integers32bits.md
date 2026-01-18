# Exemplo – Leitura de Inteiros de 32 Bits

Este exemplo demonstra como realizar a **leitura de valores inteiros de 32 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT32)** e **valores com sinal (INT32)**.

Valores de 32 bits ocupam **dois registradores Modbus consecutivos** e podem exigir atenção especial ao endianness configurado no dispositivo.

---

## Cenário típico

- Leitura de contadores de alta resolução
- Leitura de valores acumulados
- Leitura de variáveis internas de CLPs
- Monitoramento de grandezas que excedem 16 bits

Neste exemplo, será realizada a leitura a partir do **Holding Register no endereço 200**.

---

## Importações

```py
from pyModbusTCPtools import (
    ModbusTCPResiliente,
    ModbusDataType,
    Endian
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

## Leitura de inteiro de 32 bits sem sinal (UINT32)

```py
valor_uint32 = client.read_holding_typed_safe(
    addr=200,
    dtype=ModbusDataType.UINT32,
    endian=Endian.BE
)

if valor_uint32 is not None:
    print(f"UINT32 lido: {valor_uint32}")
else:
    print("Falha na leitura do UINT32")
```

---

## Leitura de inteiro de 32 bits com sinal (INT32)

```py
valor_int32 = client.read_holding_typed_safe(
    addr=202,
    dtype=ModbusDataType.INT32,
    endian=Endian.BE
)

if valor_int32 is not None:
    print(f"INT32 lido: {valor_int32}")
else:
    print("Falha na leitura do INT32")
```

---

## Observação sobre endianness

Valores de 32 bits podem ser organizados de diferentes formas dependendo do fabricante.

Caso os valores lidos estejam incorretos, teste outras opções:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Diferença entre INT32 e UINT32

- `UINT32` representa valores no intervalo de **0 a 4.294.967.295**
- `INT32` representa valores no intervalo de **-2.147.483.648 a 2.147.483.647**
- Ambos ocupam **2 registradores Modbus**
- A conversão é feita automaticamente

---

## Comportamento dos métodos

Os métodos de leitura tipada:

- Retornam o valor convertido em caso de sucesso
- Retornam `None` em caso de falha
- Realizam reconexão automática
- Aplicam backoff exponencial
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Utilize sempre o endianness correto
- Não misture tipos com e sem sinal
- Sempre valide o retorno antes de utilizar o valor

---

## Encerrando a conexão

Após finalizar as leituras, a conexão pode ser encerrada explicitamente:

```py
client.close()
```