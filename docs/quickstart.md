# Quickstart

Este guia apresenta um primeiro contato prático com a biblioteca **pyModbusTCPtools**, mostrando como estabelecer conexão, ler e escrever dados Modbus TCP de forma segura e tipada.

O objetivo é permitir que a biblioteca seja utilizada em poucos minutos, com foco em uso industrial real e sem abstrações desnecessárias.

---

## Pré-requisitos

- Python 3.8 ou superior
- Acesso a um dispositivo Modbus TCP (CLP, gateway ou simulador)
- Biblioteca pyModbusTCPtools instalada

---

## Instalação

### Instalação via pip:

```bash
pip install pyModbusTCPtools
```

### Instalação local a partir de um pacote wheel:
```bash
pip install pyModbusTCPtools-0.1.0-py3-none-any.whl
```

---

## Importações básicas
```py
from pyModbusTCPtools import (
    ModbusTCPResiliente,
    Endian,
    ModbusDataType
)
```

---

## Criando o cliente Modbus TCP
O núcleo da biblioteca é a classe ModbusTCPResiliente.

Exemplo de criação do cliente:
```py
client = ModbusTCPResiliente(
    host="192.168.0.10",
    port=502,
    unit_id=1,
    timeout=3.0,
    retry_delay=2.0,
    max_retry_delay=30.0,
    console=True
)
```
Descrição dos principais parâmetros:

- host: endereço IP do dispositivo Modbus
- port: porta TCP (padrão 502)
- unit_id: identificador do escravo Modbus
- timeout: tempo máximo de espera por resposta
- retry_delay: atraso inicial entre tentativas de reconexão
- max_retry_delay: limite máximo do backoff exponencial
- console: habilita saída de logs no console

---

## Leitura de Coils

Leitura segura de coils (valores booleanos):
```py
result = client.read_coils_safe(addr=0, count=1)

if result is not None:
    estado = result[0]
    print(f"Coil 0: {estado}")
```

Observações importantes:

- O endereçamento é zero-based
- Em caso de falha, o método retorna None
- Reconexão automática é aplicada se necessário

## Escrita de Coils

Escrita de uma única coil:
```py
ok = client.write_single_coil_safe(addr=0, value=True)

if ok:
    print("Coil escrita com sucesso")
```

O método retorna **True** em caso de sucesso e **False** em caso de falha.

---

## Leitura de Holding Registers (valores brutos)

Leitura direta de registradores sem conversão de tipo:
```py
regs = client.read_holding_registers_safe(addr=100, count=2)

if regs is not None:
    print(regs)
```

Os valores retornados são inteiros sem sinal de 16 bits (UINT16).

---

## Leitura tipada de registradores

A biblioteca permite a leitura direta já convertida para tipos Python nativos.

Exemplo de leitura de um valor FLOAT32:

```py
temperatura = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)

if temperatura is not None:
    print(f"Temperatura: {temperatura:.2f}")
```

Tipos suportados:

- INT16 e UINT16
- INT32 e UINT32
- INT64 e UINT64
- FLOAT32
- FLOAT64

---

## Escrita tipada de registradores

Exemplo de escrita de um valor INT32:
```py
ok = client.write_holding_typed_safe(
    addr=200,
    value=1500,
    dtype=ModbusDataType.INT32,
    endian=Endian.LE
)

if ok:
    print("Valor escrito com sucesso")
```

A biblioteca converte automaticamente o valor informado para o formato Modbus correto, respeitando tipo e endianness.

---

## Endianness

O comportamento de ordenação de palavras e bytes é controlado pelo enum Endian.
Valores disponíveis:

- Endian.BE: Big Endian (padrão Modbus)
- Endian.LE: Little Endian (troca de palavras)
- Endian.BE_SWAP: Big Endian com troca de bytes
- Endian.LE_SWAP: Little Endian com troca de palavras e bytes

A escolha correta depende do fabricante e da configuração do CLP ou gateway Modbus.

---

Tratamento de falhas

Os métodos com sufixo _safe seguem as seguintes regras:

- Retornam None ou False em caso de erro
- Realizam reconexão automática quando a conexão é perdida
- Aplicam backoff exponencial configurável
- Registram logs de erro e advertência
- Cacheiam endereços Modbus inválidos para evitar repetição de falhas

Exemplo de verificação segura:
```py
valor = client.read_input_typed_safe(
    addr=10,
    dtype=ModbusDataType.INT16
)

if valor is None:
    print("Falha na leitura ou endereço inválido")
```

---

## Encerrando a conexão

A conexão pode ser encerrada explicitamente quando não for mais necessária:
```py
client.close()
```

---

## Próximos passos

Após concluir este Quickstart, recomenda-se:

- Ler a seção de conceitos
- Entender em detalhe o funcionamento do endianness
- Consultar a documentação completa da API
- Analisar os exemplos de uso industrial
- Integrar a biblioteca ao projeto final

Este Quickstart cobre apenas o essencial para iniciar o uso da biblioteca. A documentação completa aborda cenários avançados, boas práticas e decisões de projeto.