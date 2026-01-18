# Exemplo – Escrita de Inteiros de 16 Bits

Este exemplo demonstra como realizar a **escrita de valores inteiros de 16 bits** utilizando a biblioteca **pyModbusTCPtools**, contemplando **valores sem sinal (UINT16)** e **valores com sinal (INT16)**.

A escrita de inteiros de 16 bits é comum em aplicações industriais para envio de setpoints, parâmetros e comandos numéricos simples.

---

## Cenário típico

- Escrita de setpoints
- Escrita de parâmetros de configuração
- Envio de comandos numéricos inteiros
- Ajuste de variáveis internas de CLPs

Neste exemplo, será realizada a escrita em **Holding Registers** a partir do endereço **600**.

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

## Escrita de inteiro de 16 bits sem sinal (UINT16)

```py
ok = client.write_holding_typed_safe(
    addr=600,
    value=12345,
    dtype=ModbusDataType.UINT16
)

if ok:
    print("UINT16 escrito com sucesso")
else:
    print("Falha na escrita do UINT16")
```

---

## Escrita de inteiro de 16 bits com sinal (INT16)

```py
ok = client.write_holding_typed_safe(
    addr=601,
    value=-1234,
    dtype=ModbusDataType.INT16
)

if ok:
    print("INT16 escrito com sucesso")
else:
    print("Falha na escrita do INT16")
```

---

## Diferença entre INT16 e UINT16

- `UINT16` aceita valores no intervalo de **0 a 65535**
- `INT16` aceita valores no intervalo de **-32768 a 32767**
- A biblioteca valida automaticamente o range
- Valores fora do range geram erro de conversão

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
- Utilize o tipo correto (com ou sem sinal)
- Não escreva valores fora do range permitido
- Sempre verifique o retorno do método

---

## Encerrando a conexão

Após finalizar as escritas, a conexão pode ser encerrada explicitamente:

```py
client.close()
```
