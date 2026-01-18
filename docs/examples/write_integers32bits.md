# Exemplo – Escrita de Inteiros de 32 Bits

Este exemplo demonstra como realizar a **escrita de valores inteiros de 32 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT32)** e **valores com sinal (INT32)**.

Valores de 32 bits ocupam **dois registradores Modbus consecutivos**, exigindo atenção ao endianness configurado no dispositivo.

---

## Cenário típico

- Escrita de setpoints de alta resolução
- Escrita de contadores acumulados
- Configuração de parâmetros que excedem 16 bits
- Ajuste de variáveis internas de CLPs

Neste exemplo, será realizada a escrita em **Holding Registers** a partir do endereço **700**.

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

## Escrita de inteiro de 32 bits sem sinal (UINT32)

```py
ok = client.write_holding_typed_safe(
    addr=700,
    value=123456789,
    dtype=ModbusDataType.UINT32,
    endian=Endian.BE
)

if ok:
    print("UINT32 escrito com sucesso")
else:
    print("Falha na escrita do UINT32")
```

---

## Escrita de inteiro de 32 bits com sinal (INT32)

```py
ok = client.write_holding_typed_safe(
    addr=702,
    value=-12345678,
    dtype=ModbusDataType.INT32,
    endian=Endian.BE
)

if ok:
    print("INT32 escrito com sucesso")
else:
    print("Falha na escrita do INT32")
```

---

## Observação sobre endianness

Para valores de 32 bits, o endianness é crítico.

Se o dispositivo utilizar word swap ou byte swap, teste:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Diferença entre INT32 e UINT32

- `UINT32` aceita valores de **0 a 4.294.967.295**
- `INT32` aceita valores de **-2.147.483.648 a 2.147.483.647**
- Ambos ocupam **2 registradores Modbus**
- A biblioteca valida automaticamente o range

---

## Comportamento dos métodos

Os métodos de escrita tipada:

- Retornam `True` em caso de sucesso
- Retornam `False` em caso de falha
- Validam tipo e faixa de valores
- Realizam reconexão automática se necessário
- Aplicam backoff exponencial
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Utilize sempre o endianness correto
- Não escreva valores fora do range permitido
- Sempre verifique o retorno do método

---

## Encerrando a conexão

Após finalizar as escritas, a conexão pode ser encerrada explicitamente:

```py
client.close()
```