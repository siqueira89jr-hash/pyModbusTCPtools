# Exemplo – Leitura de Ponto Flutuante de 32 Bits (FLOAT32)

Este exemplo demonstra como realizar a **leitura de valores em ponto flutuante de 32 bits (FLOAT32)** utilizando a biblioteca **pyModbusTCPtools**.

Valores FLOAT32 ocupam **dois registradores Modbus consecutivos** e representam números reais conforme o padrão **IEEE 754**.

---

## Cenário típico

- Leitura de temperatura
- Leitura de pressão
- Leitura de vazão
- Leitura de níveis analógicos em engenharia

Neste exemplo, será realizada a leitura a partir do **Holding Register no endereço 400**.

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

## Leitura de FLOAT32

```py
valor_float32 = client.read_holding_typed_safe(
    addr=400,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if valor_float32 is not None:
    print(f"FLOAT32 lido: {valor_float32}")
else:
    print("Falha na leitura do FLOAT32")
```

---

## Observação sobre endianness

Valores FLOAT32 dependem diretamente da correta configuração de endianness.

Caso o valor lido não seja coerente, teste outras opções:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Características do FLOAT32

- Padrão IEEE 754
- 32 bits de largura
- Ocupa 2 registradores Modbus
- Representa números reais com casas decimais

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
- Confirme o tipo FLOAT configurado no dispositivo
- Utilize sempre o endianness correto
- Sempre valide o retorno antes de utilizar o valor

---

## Encerrando a conexão

Após finalizar a leitura, a conexão pode ser encerrada explicitamente:

```py
client.close()
```