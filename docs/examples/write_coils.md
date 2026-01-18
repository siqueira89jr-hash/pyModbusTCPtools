# Exemplo – Escrita de Coils

Este exemplo demonstra como realizar a **escrita de coils (valores booleanos)** utilizando a biblioteca **pyModbusTCPtools** de forma segura.

A escrita de coils é normalmente utilizada para acionar comandos digitais, como ligar/desligar motores, válvulas, relés ou flags internas de controle.

---

## Cenário típico

- Acionamento de uma saída digital
- Envio de comando liga/desliga
- Escrita de flags de controle em CLPs e dispositivos Modbus TCP

Neste exemplo, será realizada a **escrita da coil no endereço 0**.

---

## Importações

```py
from pyModbusTCPtools import ModbusTCPResiliente
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

## Escrita de uma coil

### Escrita de valor `True`

```py
ok = client.write_single_coil_safe(addr=0, value=True)

if ok:
    print("Coil 0 escrita com sucesso (True)")
else:
    print("Falha ao escrever a coil 0")
```

---

### Escrita de valor `False`

```py
ok = client.write_single_coil_safe(addr=0, value=False)

if ok:
    print("Coil 0 escrita com sucesso (False)")
else:
    print("Falha ao escrever a coil 0")
```

---

## Escrita de múltiplas coils

Também é possível escrever várias coils em uma única operação.

```py
values = [True, False, True, True]

ok = client.write_multiple_coils_safe(addr=10, values=values)

if ok:
    print("Múltiplas coils escritas com sucesso")
else:
    print("Falha na escrita das coils")
```

---

## Comportamento dos métodos

Os métodos de escrita de coils possuem o seguinte comportamento:

- Retornam `True` em caso de sucesso
- Retornam `False` em caso de falha
- Realizam reconexão automática se necessário
- Aplicam backoff exponencial em falhas consecutivas
- Registram logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Sempre verifique o retorno do método
- Não assuma que o endereço da coil existe no dispositivo
- Em sistemas industriais, comandos devem ser escritos com validação adicional

---

## Encerrando a conexão

Após finalizar as operações, a conexão pode ser encerrada explicitamente:

```py
client.close()
```