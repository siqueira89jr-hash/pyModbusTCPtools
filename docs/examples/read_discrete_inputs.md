# Exemplo – Leitura de Discrete Inputs

Este exemplo demonstra como realizar a **leitura de Discrete Inputs (entradas digitais somente leitura)** utilizando a biblioteca **pyModbusTCPtools** de forma segura.

Discrete Inputs são normalmente utilizados para leitura de sensores digitais, chaves de fim de curso, botões e sinais de estado que **não podem ser escritos** pelo cliente Modbus.

---

## Cenário típico

- Leitura de sensores digitais
- Monitoramento de fim de curso
- Verificação de estados de segurança
- Leitura de entradas físicas de CLPs e módulos remotos

Neste exemplo, será realizada a leitura de **Discrete Inputs a partir do endereço 0**.

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

## Leitura de Discrete Inputs

### Leitura de uma entrada digital

```py
result = client.read_discrete_inputs_safe(addr=0, count=1)

if result is not None:
    estado = result[0]
    print(f"Discrete Input 0: {estado}")
else:
    print("Falha na leitura do Discrete Input")
```

---

### Leitura de múltiplas entradas digitais

```py
result = client.read_discrete_inputs_safe(addr=10, count=4)

if result is not None:
    for i, value in enumerate(result):
        print(f"Discrete Input {10 + i}: {value}")
else:
    print("Falha na leitura dos Discrete Inputs")
```

---

## Comportamento do método

O método `read_discrete_inputs_safe` possui o seguinte comportamento:

- Retorna uma lista de valores booleanos em caso de sucesso
- Retorna `None` em caso de falha
- Realiza reconexão automática se necessário
- Aplica backoff exponencial em falhas consecutivas
- Registra logs detalhados

---

## Observações importantes

- O endereçamento é **zero-based**
- Discrete Inputs são **somente leitura**
- Sempre valide o retorno antes de acessar os valores
- Não assuma que o endereço da entrada existe no dispositivo
- Em ambientes industriais, falhas de leitura devem ser tratadas como eventos normais

---

## Encerrando a conexão

Após finalizar as leituras, a conexão pode ser encerrada explicitamente:

```py
client.close()
```