# Exemplo – Leitura de Inteiros de 64 Bits

Este exemplo demonstra como realizar a **leitura de valores inteiros de 64 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT64)** e **valores com sinal (INT64)**.

Valores de 64 bits ocupam **quatro registradores Modbus consecutivos** e exigem atenção especial ao endianness configurado no dispositivo.

---

## Cenário típico

- Leitura de contadores de grande capacidade
- Leitura de acumuladores de energia ou produção
- Leitura de identificadores numéricos extensos
- Monitoramento de variáveis de alta resolução

Neste exemplo, será realizada a leitura a partir do **Holding Register no endereço 300**.

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

## Leitura de inteiro de 64 bits sem sinal (UINT64)

```py
valor_uint64 = client.read_holding_typed_safe(
    addr=300,
    dtype=ModbusDataType.UINT64,
    endian=Endian.BE
)

if valor_uint64 is not None:
    print(f"UINT64 lido: {valor_uint64}")
else:
    print("Falha na leitura do UINT64")
```

---

## Leitura de inteiro de 64 bits com sinal (INT64)

```py
valor_int64 = client.read_holding_typed_safe(
    addr=304,
    dtype=ModbusDataType.INT64,
    endian=Endian.BE
)

if valor_int64 is not None:
    print(f"INT64 lido: {valor_int64}")
else:
    print("Falha na leitura do INT64")
```

---

## Observação sobre endianness

Valores de 64 bits podem ser organizados de diferentes formas dependendo do fabricante.

Caso os valores lidos estejam incorretos, teste outras opções:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Diferença entre INT64 e UINT64

- `UINT64` representa valores no intervalo de **0 a 18.446.744.073.709.551.615**
- `INT64` representa valores no intervalo de **-9.223.372.036.854.775.808 a 9.223.372.036.854.775.807**
- Ambos ocupam **4 registradores Modbus**
- A conversão é realizada automaticamente pela biblioteca

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
- Valores de 64 bits exigem atenção redobrada ao endereço inicial
- Sempre valide o retorno antes de utilizar o valor

---

## Encerrando a conexão

Após finalizar as leituras, a conexão pode ser encerrada explicitamente:

```py
client.close()
```