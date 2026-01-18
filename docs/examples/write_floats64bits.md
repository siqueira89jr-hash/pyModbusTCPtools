# Exemplo – Escrita de Ponto Flutuante de 64 Bits (FLOAT64)

Este exemplo demonstra como realizar a **escrita de valores em ponto flutuante de 64 bits (FLOAT64)** utilizando a biblioteca **pyModbusTCPtools**.

Valores FLOAT64 ocupam **quatro registradores Modbus consecutivos** e seguem o padrão **IEEE 754 (dupla precisão)**, exigindo atenção rigorosa ao endianness configurado no dispositivo.

---

## Cenário típico

- Escrita de totalizadores de alta precisão
- Configuração de parâmetros críticos de processo
- Envio de valores de engenharia de dupla precisão
- Ajuste fino de variáveis industriais

Neste exemplo, será realizada a escrita em **Holding Registers** a partir do endereço **1000**.

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

## Escrita de FLOAT64

```py
ok = client.write_holding_typed_safe(
    addr=1000,
    value=12345.6789,
    dtype=ModbusDataType.FLOAT64,
    endian=Endian.BE
)

if ok:
    print("FLOAT64 escrito com sucesso")
else:
    print("Falha na escrita do FLOAT64")
```

---

## Observação sobre endianness

Valores FLOAT64 são extremamente sensíveis à configuração correta de endianness.

Caso o valor escrito não seja interpretado corretamente pelo dispositivo, teste:

- `Endian.LE`
- `Endian.BE_SWAP`
- `Endian.LE_SWAP`

A biblioteca não tenta inferir automaticamente o endianness correto.

---

## Características do FLOAT64

- Padrão IEEE 754 (dupla precisão)
- 64 bits de largura
- Ocupa 4 registradores Modbus
- Alta precisão numérica para aplicações industriais

---

## Comportamento dos métodos

Os métodos de escrita tipada:

- Retornam `True` em caso de sucesso
- Retornam `False` em caso de falha
- Validam tipo e faixa do valor
- Realizam reconexão automática se necessário
- Aplicam backoff exponencial
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Confirme se o dispositivo suporta FLOAT64
- Utilize sempre o endianness correto
- Valores incoerentes normalmente indicam erro de endianness
- Sempre verifique o retorno do método

---

## Encerrando a conexão

Após finalizar a escrita, a conexão pode ser encerrada explicitamente:

```py
client.close()
```

---

## Próximo passo

Com este exemplo, a sequência de **leitura e escrita tipada** está completa.

Recomenda-se agora revisar os exemplos, validar em ambiente real e integrar a biblioteca ao projeto final.
