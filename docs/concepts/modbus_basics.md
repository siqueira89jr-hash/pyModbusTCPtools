# Fundamentos do Modbus

Esta seção apresenta os **conceitos fundamentais do protocolo Modbus**, necessários para o uso correto da biblioteca **pyModbusTCPtools**.

O objetivo não é ensinar Modbus do zero, mas alinhar **terminologia, endereçamento e comportamento** conforme utilizado pela biblioteca.

---

## O que é Modbus

Modbus é um protocolo de comunicação industrial criado originalmente para troca de dados entre dispositivos de automação, como CLPs, sensores, inversores e gateways.

Características principais:

- Protocolo simples e amplamente adotado
- Modelo mestre/escravo (cliente/servidor)
- Comunicação baseada em leitura e escrita de áreas de memória
- Independente de fabricante

A biblioteca **pyModbusTCPtools** trabalha exclusivamente com **Modbus TCP**, que utiliza TCP/IP como camada de transporte.

---

## Modbus TCP

No Modbus TCP:

- A comunicação ocorre sobre TCP/IP
- A porta padrão é **502**
- Não há checksum (CRC), pois a confiabilidade é garantida pelo TCP
- O campo `Unit ID` identifica o dispositivo lógico

A biblioteca atua como **cliente Modbus TCP**, iniciando todas as requisições.

---

## Modelo de dados Modbus

O protocolo Modbus organiza os dados em **quatro áreas lógicas**, cada uma com comportamento específico.

### Coils

- Tipo: booleano (0 ou 1)
- Função: escrita e leitura
- Uso típico: comandos digitais (liga/desliga)

Exemplo de uso:
- Partida de motor
- Habilitação de controle

---

### Discrete Inputs

- Tipo: booleano
- Função: somente leitura
- Uso típico: estados de sensores digitais

Exemplo de uso:
- Fim de curso
- Chaves de segurança

---

### Input Registers

- Tipo: registrador de 16 bits (UINT16)
- Função: somente leitura
- Uso típico: medições e valores analógicos

Exemplo de uso:
- Temperatura
- Pressão
- Vazão

---

### Holding Registers

- Tipo: registrador de 16 bits (UINT16)
- Função: leitura e escrita
- Uso típico: setpoints e parâmetros

Exemplo de uso:
- Setpoint de velocidade
- Limites de processo
- Configurações gerais

---

## Endereçamento Modbus

A biblioteca **pyModbusTCPtools** utiliza **endereçamento zero-based**, conforme a especificação do Modbus TCP e a maioria das bibliotecas Python.

Isso significa:

- Coil 0 → endereço `0`
- Holding Register 40001 → endereço `0`
- Input Register 30001 → endereço `0`

O uso de endereços baseados em 1 (ex.: 40001, 30001) **não é utilizado internamente**.

---

## Tamanho dos dados

Cada registrador Modbus possui **16 bits**.

Tipos de dados maiores ocupam múltiplos registradores:

- INT32 / UINT32 → 2 registradores
- FLOAT32 → 2 registradores
- INT64 / UINT64 → 4 registradores
- FLOAT64 → 4 registradores

A biblioteca realiza automaticamente esse cálculo quando se utiliza leitura ou escrita tipada.

---

## Conversão de tipos

O protocolo Modbus **não define tipos de dados complexos**, apenas registradores de 16 bits.

A interpretação de tipos como `INT`, `FLOAT` e `DOUBLE` é feita **por convenção** entre cliente e servidor.

A biblioteca **pyModbusTCPtools** fornece:

- Conversão automática de tipos
- Validação de tamanho
- Tratamento de overflow
- Exceções claras em caso de erro

---

## Endianness

Quando múltiplos registradores são usados para representar um valor, é necessário definir a ordem correta:

- Ordem das palavras (word order)
- Ordem dos bytes dentro de cada palavra

Esse comportamento é controlado explicitamente pelo enum `Endian`.

A escolha correta depende do fabricante e da configuração do dispositivo Modbus.

A seção **Endianness** da documentação aborda esse tema em detalhes.

---

## Exceções Modbus

O protocolo Modbus define exceções padronizadas, como:

- Illegal Function
- Illegal Data Address
- Illegal Data Value

Essas exceções indicam **erro de aplicação**, não necessariamente falha de comunicação.

A biblioteca diferencia claramente:

- Erros de conexão
- Erros de protocolo Modbus
- Erros de leitura e escrita
- Erros de conversão de dados

---

## Considerações práticas

Ao trabalhar com Modbus TCP em ambiente industrial:

- Sempre confirme o endereçamento real no CLP
- Verifique o tipo de dado esperado
- Atenção especial ao endianness
- Trate falhas de comunicação como eventos normais
- Não assuma que todos os endereços existem

A biblioteca foi projetada considerando essas premissas.

---

## Próximo passo

Após compreender os fundamentos do Modbus, avance para a seção **Endianness**, onde são detalhadas as combinações de ordenação de palavras e bytes e seus impactos práticos.