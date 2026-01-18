# Exemplo – Escrita de Inteiros de 64 Bits

Este exemplo demonstra como realizar a **escrita de valores inteiros de 64 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT64)** e **valores com sinal (INT64)**.

Valores de 64 bits ocupam **quatro registradores Modbus consecutivos**, exigindo atenção especial ao endianness configurado no dispositivo.

---

## Cenário típico

- Escrita de contadores de grande capacidade
- Escrita de acumuladores de energia ou produção
- Configuração de parâmetros numéricos extensos
- Ajuste de variáveis internas de alta resolução em CLPs

Neste exemplo, será realizada a escrita em **Holding Registers** a partir do endereço **800**.

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

## Escrita de inteiro de 64 bits sem sinal (UINT64)

```py
ok = client.write_holding_typed_safe(
    addr=800,
    value=123456789012345,
    dtype=ModbusDataType.UINT64,
    endian=Endian.BE
)

if ok:
    print("UINT64 escrito com sucesso")
else:
    print("Falha na escrita do UINT64")
```

---

## Escrita de inteiro de 64 bits com sinal (INT64)

```py
ok = client.write_holding_typed_safe(
    addr=804,
    value=-123456789012345,
    dtype=ModbusDataType.INT64,
    endian=Endian.BE
)

if ok:
    print("INT64 escrito com sucesso")
else:
    print("Falha na escrita do INT64")
```

---

## Observação sobre endianness

Para valores de 64 bits, a configuração correta de endianness é crítica.

Caso o valor escrito não seja interpretado corretamente pelo dispositivo, teste:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Diferença entre INT64 e UINT64

- `UINT64` aceita valores de **0 a 18.446.744.073.709.551.615**
- `INT64` aceita valores de **-9.223.372.036.854.775.808 a 9.223.372.036.854.775.807**
- Ambos ocupam **4 registradores Modbus**
- A biblioteca valida automaticamente o range antes da escrita

---

## Comportamento dos métodos

Os métodos de escrita tipada:

- Retornam `True` em caso de sucesso
- Retornam `False` em caso de falha
- Validam tipo, tamanho e faixa de valores
- Realizam reconexão automática se necessário
- Aplicam backoff exponencial
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Utilize sempre o endianness correto
- Valores fora do range resultam em erro de conversão
- Sempre verifique o retorno do método

---

## Encerrando a conexão

Após finalizar as escritas, a conexão pode ser encerrada explicitamente:

```py
client.close()
```

---

## Próximo passo

Após compreender a escrita de inteiros de 64 bits, avance para os exemplos de **escrita de valores em ponto flutuante**, iniciando com **FLOAT32**.
