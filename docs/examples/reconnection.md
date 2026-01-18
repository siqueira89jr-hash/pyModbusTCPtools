# Exemplo – Reconexão Automática

Este exemplo demonstra como a biblioteca **pyModbusTCPtools** realiza **reconexão automática** em caso de falhas de comunicação Modbus TCP.

Em ambientes industriais, quedas de rede, reinicialização de CLPs e perda temporária de conexão são eventos normais. A biblioteca foi projetada para lidar com essas situações de forma transparente.

---

## Cenário típico

- CLP reiniciado durante a operação
- Perda temporária de conexão de rede
- Timeout de comunicação
- Falhas intermitentes em switches ou cabos

Neste exemplo, será demonstrado como a reconexão ocorre automaticamente durante leituras contínuas.

---

## Importações

```py
from time import sleep
from pyModbusTCPtools import (
    ModbusTCPResiliente,
    ModbusDataType
)
```

---

## Criação do cliente com reconexão habilitada

```py
client = ModbusTCPResiliente(
    host="192.168.0.10",
    unit_id=1,
    timeout=3.0,
    retry_delay=2.0,
    max_retry_delay=30.0,
    console=True
)
```

Os parâmetros `retry_delay` e `max_retry_delay` controlam o **backoff exponencial** entre tentativas de reconexão.

---

## Leitura contínua com reconexão automática

```py
while True:
    valor = client.read_holding_typed_safe(
        addr=100,
        dtype=ModbusDataType.INT16
    )

    if valor is not None:
        print(f"Valor lido: {valor}")
    else:
        print("Falha de comunicação. Tentando reconectar...")

    sleep(2)
```

Neste loop:

- Falhas de comunicação não encerram o programa
- A biblioteca tenta reconectar automaticamente
- O tempo entre tentativas aumenta progressivamente
- Leituras bem-sucedidas retomam automaticamente

---

## Verificação explícita de conexão

Também é possível verificar explicitamente o estado da conexão:

```py
if client.is_connected():
    print("Conexão ativa")
else:
    print("Conexão indisponível")
```

O método `is_connected` realiza uma leitura real para validar a comunicação.

---

## Comportamento da reconexão

O mecanismo de reconexão segue as seguintes regras:

- Reconexão automática em falhas de socket ou timeout
- Backoff exponencial configurável
- Limite máximo de atraso entre tentativas
- Logs detalhados de cada tentativa
- Retomada automática após restabelecimento da comunicação

Nenhuma ação manual é necessária para reconectar.

---

## Observações importantes

- Falhas de comunicação são tratadas como eventos normais
- Evite loops muito rápidos sem `sleep`
- Utilize logs para diagnóstico em produção
- Não finalize a aplicação em falhas transitórias

---

## Encerrando a conexão

Quando a aplicação for encerrada, a conexão pode ser fechada explicitamente:

```py
client.close()
```

---

## Conclusão

O mecanismo de reconexão automática da **pyModbusTCPtools** permite criar aplicações Modbus TCP **robustas e resilientes**, adequadas para operação contínua em ambientes industriais reais.
