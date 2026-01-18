# Exemplo – Escrita de Ponto Flutuante de 32 Bits (FLOAT32)

Este exemplo demonstra como realizar a **escrita de valores em ponto flutuante de 32 bits (FLOAT32)** utilizando a biblioteca **pyModbusTCPtools**.

Valores FLOAT32 ocupam **dois registradores Modbus consecutivos** e seguem o padrão **IEEE 754**, exigindo atenção ao endianness configurado no dispositivo.

---

## Cenário típico

- Escrita de setpoints analógicos
- Ajuste de parâmetros de processo
- Configuração de valores de engenharia
- Envio de referências em ponto flutuante

Neste exemplo, será realizada a escrita em **Holding Registers** a partir do endereço **900**.

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

## Escrita de FLOAT32

```py
ok = client.write_holding_typed_safe(
    addr=900,
    value=12.75,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if ok:
    print("FLOAT32 escrito com sucesso")
else:
    print("Falha na escrita do FLOAT32")
```

---

## Observação sobre endianness

Valores FLOAT32 são altamente dependentes da configuração correta de endianness.

Caso o valor não seja interpretado corretamente pelo dispositivo, teste:

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
- Confirme o suporte a FLOAT32 no dispositivo
- Utilize sempre o endianness correto
- Valores inválidos resultam em erro de conversão
- Sempre verifique o retorno do método

---

## Encerrando a conexão

Após finalizar a escrita, a conexão pode ser encerrada explicitamente:

```py
client.close()
```

---

## Próximo passo

Após compreender a escrita de FLOAT32, avance para o exemplo de **escrita de ponto flutuante de 64 bits (FLOAT64)**.
