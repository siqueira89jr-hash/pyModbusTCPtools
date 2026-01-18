# Endianness

Esta seção descreve como a biblioteca **pyModbusTCPtools** trata a ordenação de palavras e bytes (endianness) ao converter valores Modbus para tipos Python e vice-versa.

O entendimento correto de endianness é essencial para evitar leituras incorretas de valores numéricos em sistemas Modbus.

---

## O problema do endianness no Modbus

O protocolo Modbus define registradores de **16 bits**, mas **não define** como valores maiores (32 ou 64 bits) devem ser organizados quando distribuídos em múltiplos registradores.

Isso faz com que cada fabricante adote sua própria convenção para:

- Ordem das palavras (word order)
- Ordem dos bytes dentro de cada palavra (byte order)

Sem essa definição clara, o mesmo conjunto de registradores pode representar valores completamente diferentes.

---

## Conceitos básicos

### Byte order

Refere-se à ordem dos bytes dentro de uma palavra de 16 bits.

- Big Endian: byte mais significativo primeiro
- Little Endian: byte menos significativo primeiro

---

### Word order

Refere-se à ordem dos registradores quando um valor ocupa mais de um registrador.

- Big Endian (word order): registrador mais significativo primeiro
- Little Endian (word swap): registrador menos significativo primeiro

---

## Endianness na pyModbusTCPtools

A biblioteca controla explicitamente o comportamento de endianness por meio do enum `Endian`.

Esse enum permite tratar separadamente:

- Ordem de palavras
- Ordem de bytes

---

## Enum Endian

Os valores disponíveis são:

### Endian.BE

- Word order: Big Endian
- Byte order: Big Endian
- Comportamento padrão do Modbus

Uso típico:

- CLPs Siemens (padrão)
- Implementações Modbus clássicas

---

### Endian.LE

- Word order: Little Endian (word swap)
- Byte order: Big Endian

Uso típico:

- Alguns CLPs Rockwell
- Gateways configuráveis

---

### Endian.BE_SWAP

- Word order: Big Endian
- Byte order: Little Endian (byte swap)

Uso típico:

- Equipamentos que trocam bytes dentro da palavra
- Dispositivos legados específicos

---

### Endian.LE_SWAP

- Word order: Little Endian
- Byte order: Little Endian

Uso típico:

- Combinação de word swap e byte swap
- Casos específicos de interoperabilidade

---

## Exemplos práticos

### Exemplo de leitura FLOAT32 Big Endian

```py
valor = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.BE
)
```

---

### Exemplo de leitura FLOAT32 com word swap

```py
valor = client.read_holding_typed_safe(
    addr=100,
    dtype=ModbusDataType.FLOAT32,
    endian=Endian.LE
)
```

---

### Exemplo de escrita INT32 com byte swap

```py
client.write_holding_typed_safe(
    addr=200,
    value=12345,
    dtype=ModbusDataType.INT32,
    endian=Endian.BE_SWAP
)
```

---

## Como identificar o endianness correto

Para identificar o endianness correto do dispositivo Modbus:

- Consulte o manual do fabricante
- Verifique exemplos fornecidos pelo fornecedor
- Compare leituras com valores conhecidos
- Teste combinações de endianness até obter valores coerentes
- Nunca assuma o padrão sem validação.

---

## Erros comuns relacionados a endianness

Os sintomas mais comuns de endianness incorreto incluem:

- Valores muito altos ou muito baixos
- Valores negativos inesperados
- Números aparentemente aleatórios
- Oscilações incoerentes em leituras estáveis

A biblioteca não tenta "adivinhar" o endianness correto. Ele deve ser informado explicitamente.

## Boas práticas

- Documente o endianness utilizado por cada dispositivo
- Centralize a configuração de endianness na aplicação
- Evite misturar endianness diferentes no mesmo projeto
- Valide sempre com valores de referência

---

## Próximo passo

Após entender o funcionamento do endianness, avance para a seção Tratamento de Erros, onde são detalhadas as exceções, falhas de comunicação e estratégias de recuperação adotadas pela biblioteca.