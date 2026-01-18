# Exemplo – Leitura de Ponto Flutuante de 64 Bits (FLOAT64)

Este exemplo demonstra como realizar a **leitura de valores em ponto flutuante de 64 bits (FLOAT64)** utilizando a biblioteca **pyModbusTCPtools**.

Valores FLOAT64 ocupam **quatro registradores Modbus consecutivos** e representam números reais de **dupla precisão**, conforme o padrão **IEEE 754**.

---

## Cenário típico

- Leitura de energia acumulada
- Leitura de totalizadores de alta precisão
- Leitura de variáveis de processo críticas
- Monitoramento de grandezas com alta resolução numérica

Neste exemplo, será realizada a leitura a partir do **Holding Register no endereço 500**.

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

## Leitura de FLOAT64

```py
valor_float64 = client.read_holding_typed_safe(
    addr=500,
    dtype=ModbusDataType.FLOAT64,
    endian=Endian.BE
)

if valor_float64 is not None:
    print(f"FLOAT64 lido: {valor_float64}")
else:
    print("Falha na leitura do FLOAT64")
```

---

## Observação sobre endianness

Valores FLOAT64 são altamente sensíveis à configuração de endianness.

Caso o valor lido não seja coerente, teste outras opções:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Características do FLOAT64

- Padrão IEEE 754 (dupla precisão)
- 64 bits de largura
- Ocupa 4 registradores Modbus
- Alta precisão para cálculos industriais

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
- Confirme se o dispositivo suporta FLOAT64
- Utilize sempre o endianness correto
- Valores incoerentes geralmente indicam erro de endianness
- Sempre valide o retorno antes de utilizar o valor

---

## Encerrando a conexão

Após finalizar a leitura, a conexão pode ser encerrada explicitamente:

```py
client.close()
```
