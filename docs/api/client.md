# API – ModbusTCPResiliente

Esta seção documenta a API pública da biblioteca **pyModbusTCPtools**, com foco na classe `ModbusTCPResiliente`.

O objetivo é descrever de forma clara e objetiva o comportamento, os parâmetros e os retornos de cada método público, sem expor detalhes internos de implementação.

---

## Classe ModbusTCPResiliente

A classe `ModbusTCPResiliente` representa um cliente Modbus TCP resiliente, projetado para uso industrial contínuo.

Principais características:

- Reconexão automática
- Backoff exponencial
- Cache de endereços inválidos
- Leitura e escrita tipada
- Tratamento explícito de erros
- Logging estruturado

---

## Criação do cliente

### Construtor

```py
ModbusTCPResiliente(
    host,
    port=502,
    unit_id=1,
    timeout=3.0,
    retry_delay=2.0,
    max_retry_delay=30.0,
    ping_addr=0,
    ping_count=1,
    log_file="modbus.log",
    console=False,
    logger=None,
    invalid_cache_ttl=600,
    invalid_cache_max=500
)
```

---

## Parâmetros

- host

    Endereço IP ou hostname do dispositivo Modbus TCP.

- port

    Porta TCP utilizada pelo servidor Modbus. Valor padrão: `502`.

- unit_id

    Identificador lógico do dispositivo Modbus.

- timeout

    Tempo máximo de espera por resposta (em segundos).

- retry_delay

    Tempo inicial de espera entre tentativas de reconexão.

- max_retry_delay

    Tempo máximo de espera entre tentativas de reconexão.

- ping_addr

    Endereço utilizado para verificar conectividade ativa.

- ping_count

    Quantidade de registradores utilizados no teste de conexão.

- log_file

    Caminho do arquivo de log. Pode ser `None` para desabilitar.

- console

    Se `True`, imprime logs também no console.

- logger

    Logger externo opcional. Se informado, substitui o logger interno.

- invalid_cache_ttl

    Tempo de vida (em segundos) do cache de endereços inválidos.

- invalid_cache_max

    Número máximo de entradas no cache de endereços inválidos.

---

## Gerenciamento de conexão

### is_connected

Verifica se a conexão Modbus TCP está ativa por meio de uma leitura real no dispositivo.

```py
client.is_connected()
```

- Retorna `True` se a comunicação estiver funcional
- Retorna `False` em caso de falha
- Pode disparar reconexão automática

---

### close

Encerra explicitamente a conexão Modbus TCP.

```py
client.close()
```

---

## Leitura de bits

### read_coils_safe

```py
client.read_coils_safe(addr, count)
```

- Retorna lista de booleanos em caso de sucesso
- Retorna `None` em caso de falha

---

### read_discrete_inputs_safe

```py
client.read_discrete_inputs_safe(addr, count)
```

---

## Escrita de bits

### write_single_coil_safe

```py
client.write_single_coil_safe(addr, value)
```

---

### write_multiple_coils_safe

```py
client.write_multiple_coils_safe(addr, values)
```

---

## Leitura de registradores (bruto)

### read_holding_registers_safe

```py
client.read_holding_registers_safe(addr, count)
```

---

### read_input_registers_safe

```py
client.read_input_registers_safe(addr, count)
```

---

## Escrita de registradores (bruto)

### write_single_register_safe

```py
client.write_single_register_safe(addr, value)
```

---

### write_multiple_registers_safe

```py
client.write_multiple_registers_safe(addr, values)
```

---

## Leitura tipada de registradores

### read_holding_typed_safe

```py
client.read_holding_typed_safe(
    addr,
    dtype,
    endian=Endian.BE
)
```

---

### read_input_typed_safe

```py
client.read_input_typed_safe(
    addr,
    dtype,
    endian=Endian.BE
)
```

---

## Escrita tipada de registradores

### write_holding_typed_safe

```py
client.write_holding_typed_safe(
    addr,
    value,
    dtype,
    endian=Endian.BE
)
```

---

## Exceções

- ModbusConnectionError
- ModbusProtocolError
- ModbusReadError
- ModbusWriteError
- ModbusConversionError

---

## Considerações finais

A classe `ModbusTCPResiliente` foi projetada para uso industrial contínuo, oferecendo previsibilidade, robustez e clareza de API.