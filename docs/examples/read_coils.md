# Exemplo – Leitura de Coils

Este exemplo demonstra como realizar a **leitura de coils (valores booleanos)** utilizando a biblioteca **pyModbusTCPtools** de forma segura.

A leitura de coils é normalmente utilizada para verificar estados digitais, como comandos, saídas ou flags internas de CLPs e dispositivos Modbus TCP.

---

## Cenário típico

- Leitura do estado de uma saída digital
- Verificação de comando ligado/desligado
- Monitoramento de bits de status

Neste exemplo, será realizada a leitura da **coil no endereço 0**.

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

## Leitura de uma coil

```py
result = client.read_coils_safe(addr=0, count=1)

if result is not None:
    estado = result[0]
    print(f"Estado da coil 0: {estado}")
else:
    print("Falha na leitura da coil")
```

---

## Comportamento do método

O método `read_coils_safe` possui o seguinte comportamento:

- Retorna uma lista de valores booleanos em caso de sucesso
- Retorna `None` em caso de falha
- Realiza reconexão automática se necessário
- Aplica backoff exponencial em falhas consecutivas
- Registra logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Sempre valide o retorno antes de acessar o valor
- Não assuma que o endereço da coil existe no dispositivo
- Em ambientes industriais, falhas de leitura devem ser tratadas como eventos normais

---

## Encerrando a conexão

Após finalizar a leitura, a conexão pode ser encerrada explicitamente:

```py
client.close()
```