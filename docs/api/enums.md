# API – Enums

Esta seção documenta os enums públicos utilizados pela biblioteca **pyModbusTCPtools**.

Os enums fornecem uma forma explícita e segura de configurar tipos de dados Modbus e comportamento de endianness, evitando o uso de valores mágicos na aplicação.

---

## Enum Endian

O enum `Endian` define a ordenação de palavras e bytes utilizada na conversão de valores Modbus que ocupam múltiplos registradores.

Ele controla separadamente:

- Ordem das palavras (word order)
- Ordem dos bytes dentro da palavra (byte order)

A escolha correta depende do fabricante e da configuração do dispositivo Modbus.

---

### Endian.BE

Big Endian (padrão Modbus).

Características:

- Word order: Big Endian
- Byte order: Big Endian

Uso típico:

- CLPs Siemens
- Implementações Modbus clássicas

---

### Endian.LE

Little Endian com troca de palavras (word swap).

Características:

- Word order: Little Endian
- Byte order: Big Endian

Uso típico:

- Alguns CLPs Rockwell
- Gateways configuráveis

---

### Endian.BE_SWAP

Big Endian com troca de bytes.

Características:

- Word order: Big Endian
- Byte order: Little Endian

Uso típico:

- Dispositivos que realizam byte swap
- Equipamentos legados específicos

---

### Endian.LE_SWAP

Little Endian com troca de palavras e bytes.

Características:

- Word order: Little Endian
- Byte order: Little Endian

Uso típico:

- Casos específicos de interoperabilidade

---

## Enum ModbusDataType

O enum `ModbusDataType` define os tipos de dados suportados pela biblioteca para leitura e escrita tipada.

Cada tipo corresponde a um tamanho fixo em bits e a uma quantidade conhecida de registradores Modbus.

---

### INT16

- Tipo inteiro com sinal
- Tamanho: 16 bits
- Registradores: 1
- Range: -32.768 a 32.767

---

### UINT16

- Tipo inteiro sem sinal
- Tamanho: 16 bits
- Registradores: 1
- Range: 0 a 65.535

---

### INT32

- Tipo inteiro com sinal
- Tamanho: 32 bits
- Registradores: 2
- Range: -2.147.483.648 a 2.147.483.647

---

### UINT32

- Tipo inteiro sem sinal
- Tamanho: 32 bits
- Registradores: 2
- Range: 0 a 4.294.967.295

---

### INT64

- Tipo inteiro com sinal
- Tamanho: 64 bits
- Registradores: 4
- Range: -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807

---

### UINT64

- Tipo inteiro sem sinal
- Tamanho: 64 bits
- Registradores: 4
- Range: 0 a 18.446.744.073.709.551.615

---

### FLOAT32

- Tipo ponto flutuante (IEEE 754)
- Tamanho: 32 bits
- Registradores: 2
- Range aproximado: ±1,18 × 10⁻³⁸ a ±3,40 × 10³⁸

---

### FLOAT64

- Tipo ponto flutuante de dupla precisão (IEEE 754)
- Tamanho: 64 bits
- Registradores: 4
- Range aproximado: ±2,23 × 10⁻³⁰⁸ a ±1,79 × 10³⁰⁸

---

## Considerações de uso

Boas práticas ao utilizar enums:

- Sempre utilize os enums ao invés de valores literais
- Documente o endianness utilizado por cada dispositivo
- Centralize a definição de tipos e endianness na aplicação
- Evite misturar diferentes endianness sem necessidade

---

## Próximo passo

Após compreender os enums disponíveis, avance para a documentação de **Exceções**, onde são detalhados os erros levantados pela biblioteca e como tratá-los corretamente.
