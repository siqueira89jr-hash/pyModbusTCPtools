# Instalação

Esta seção descreve os métodos suportados para instalação da biblioteca **pyModbusTCPtools** em ambientes de desenvolvimento e produção.

A biblioteca foi projetada para funcionar com **Python moderno (>= 3.8)** e é compatível com ambientes industriais como servidores Linux, Raspberry Pi e sistemas Windows.

---

## Requisitos

Antes de instalar, verifique se o ambiente atende aos seguintes requisitos:

- Python 3.8 ou superior
- Acesso à rede onde o dispositivo Modbus TCP está conectado
- Permissão para instalar pacotes Python no ambiente (virtual ou sistema)

---

## Instalação via pip (recomendada)

Este é o método recomendado para a maioria dos usuários.

```bash
pip install pyModbusTCPtools
```

Esse comando instala automaticamente a versão mais recente disponível no PyPI, juntamente com suas dependências.

---

## Instalação em ambiente virtual (venv)

Para projetos profissionais e ambientes de produção, recomenda-se o uso de um ambiente virtual Python.

Criar ambiente virtual

```bash
python -m venv .venv
```

Ativar o ambiente virtual

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Instalar a biblioteca no ambiente virtual

```bash
pip install pyModbusTCPtools
```

---

## Instalação local a partir de um pacote wheel

Este método é útil em ambientes industriais sem acesso direto à internet ou com controle rígido de versões.

```bash
pip install pyModbusTCPtools-0.1.0-py3-none-any.whl
```

O arquivo .whl deve estar presente no diretório atual ou o caminho completo deve ser informado.

---

## Dependências

A biblioteca utiliza internamente o pacote:

- pyModbusTCP >= 0.2.0

Essa dependência é instalada automaticamente quando a biblioteca é instalada via pip ou wheel.

---

## Verificação da instalação

Após a instalação, é possível validar rapidamente se a biblioteca está disponível no ambiente:

```bash
python -c "from pyModbusTCPtools import ModbusTCPResiliente; print('OK')"
```

Se não houver erros, a instalação foi concluída com sucesso.

---

Observações para ambientes industriais:

- Recomenda-se fixar a versão da biblioteca em produção
- Utilize ambientes virtuais sempre que possível
- Em sistemas embarcados, evite atualizar dependências sem validação prévia
- Para deploys offline, prefira o uso de arquivos wheel versionados

---

## Próximo passo

Após a instalação, siga para o Quickstart para criar a primeira conexão Modbus TCP e realizar leituras e escritas básicas.