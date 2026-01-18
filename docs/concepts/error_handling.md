# Tratamento de Erros

Esta seção descreve como a biblioteca **pyModbusTCPtools** trata erros de comunicação, exceções do protocolo Modbus e falhas de conversão de dados.

O objetivo é permitir que aplicações industriais consigam **distinguir claramente a causa da falha** e tomem decisões corretas, sem depender de mensagens genéricas ou comportamentos implícitos.

---

## Tipos de erro em sistemas Modbus

Em aplicações Modbus TCP, erros podem ocorrer por diferentes motivos. A biblioteca diferencia explicitamente essas situações.

As categorias principais são:

- Falhas de conexão
- Exceções do protocolo Modbus
- Falhas de leitura ou escrita
- Erros de conversão de dados

Cada categoria é representada por uma exceção específica.

---

## Filosofia de tratamento da biblioteca

A biblioteca foi projetada com os seguintes princípios:

- Falhas de comunicação são eventos normais
- Erros não devem derrubar a aplicação
- O tipo do erro deve ser explícito
- O chamador decide como reagir
- Reconexão deve ser automática quando possível

Por isso, a API oferece **métodos seguros (`_safe`)** e **exceções bem definidas**.

---

## Exceções disponíveis

Todas as exceções da biblioteca herdam de `ModbusError`.

---

### ModbusError

Exceção base para todos os erros relacionados ao Modbus.

Uso típico:
- Captura genérica de erros da biblioteca

---

### ModbusConnectionError

Indica falha de conexão TCP ou perda de comunicação com o dispositivo.

Causas comuns:
- CLP desligado
- Cabo desconectado
- Timeout de rede
- Socket encerrado

---

### ModbusProtocolError

Indica que o dispositivo Modbus respondeu com uma **exceção de protocolo**, como:

- Illegal Function
- Illegal Data Address
- Illegal Data Value

Nesse caso:
- A conexão TCP pode continuar ativa
- O erro indica problema de aplicação ou endereçamento

---

### ModbusReadError

Indica falha durante uma operação de leitura Modbus.

Pode ocorrer quando:
- Não há resposta válida
- O dispositivo retorna dados inconsistentes
- O cliente Modbus falha sem exceção explícita

---

### ModbusWriteError

Indica falha durante uma operação de escrita Modbus.

Pode ocorrer quando:
- O dispositivo rejeita a escrita
- A escrita não é confirmada
- O socket falha durante a operação

---

### ModbusConversionError

Indica erro na conversão de dados Modbus para tipos Python.

Causas comuns:
- Valor fora do range do tipo
- Quantidade incorreta de registradores
- Endianness incompatível
- Valor inválido para FLOAT ou DOUBLE

---

## Métodos `_safe`

Os métodos com sufixo `_safe` são projetados para **uso direto em aplicações**.

Características principais:

- Nunca levantam exceções não tratadas
- Retornam `None` ou `False` em caso de falha
- Realizam reconexão automática
- Aplicam backoff exponencial
- Registram logs detalhados

---

## Exemplo de leitura segura

```py
valor = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if valor is None:
    print("Falha na leitura ou endereço inválido")
```

---

## Uso explícito de exceções

Para aplicações que precisam de controle mais fino, é possível utilizar exceções diretamente.

```py
from pyModbusTCPtools.exceptions import ModbusConnectionError, ModbusProtocolError

try:
    valor = client.read_holding_typed_safe(
        addr=100,
        dtype=ModbusDataType.INT32
    )
except ModbusProtocolError as exc:
    print(f"Erro de protocolo Modbus: {exc}")
except ModbusConnectionError as exc:
    print(f"Falha de conexão: {exc}")
```

---

## Cache de endereços inválidos

A biblioteca mantém um cache interno de endereços inválidos, utilizado quando o dispositivo retorna exceções como `Illegal Data Address`.

### Comportamento

- Endereços inválidos são colocados em quarentena
- Novas tentativas são bloqueadas temporariamente
- O cache possui tempo de expiração configurável
- Evita sobrecarga desnecessária no dispositivo

Esse mecanismo é totalmente transparente para o usuário.

---

## Logs e diagnóstico

A biblioteca gera logs estruturados que auxiliam no diagnóstico de falhas.

Os logs podem incluir:

- Tentativas de reconexão
- Perda de comunicação
- Exceções Modbus
- Erros de conversão

O nível de detalhe pode ser ajustado via configuração do logger.

---

## Boas práticas

- Sempre valide retornos None ou False
- Diferencie erro de protocolo de erro de conexão
- Não trate exceções de forma genérica sem análise
- Registre logs em ambiente de produção
- Nunca assuma que um endereço Modbus existe

---

## Próximo passo

Após compreender o tratamento de erros, avance para a documentação da API, onde a classe ModbusTCPResiliente e seus métodos públicos são descritos em detalhe.