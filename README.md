# Petshoop-leo
PetShop é uma aplicação web desenvolvida em Django, com foco em oferecer uma plataforma simples e intuitiva para a gestão de serviços e produtos para animais de estimação. O sistema permite aos usuários agendar consultas, comprar produtos, e acessar informações sobre os serviços oferecidos pela loja.



# 🐾 Petshoop-Leo

Sistema completo de Petshop desenvolvido com Django e Python. Ideal para gestão de clientes, pets e serviços como banho, tosa e consultas veterinárias.

## 🚀 Funcionalidades

- Cadastro de clientes, pets e serviços
- Upload de fotos dos pets
- Sistema de login para administração
- Painel administrativo com filtros e busca
- Integração com Amazon S3 (armazenamento de imagens)
- Deploy otimizado com `collectfast`
- Testes automatizados com `pytest`

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Framework:** Django 5.1
- **Banco de Dados:** PostgreSQL
- **Frontend:** Bootstrap (HTML/CSS)
- **Gerenciador de pacotes:** Poetry

### 📦 Principais Bibliotecas

| Biblioteca                    | Função                                         |
|------------------------------|------------------------------------------------|
| `python-decouple`            | Variáveis de ambiente                          |
| `dj-database-url`            | Configuração do banco de dados                 |
| `pillow`                     | Upload e manipulação de imagens                |
| `django-s3-folder-storage`   | Armazenamento na AWS S3                        |
| `collectfast`                | Otimização do `collectstatic`                 |
| `sentry-sdk`                 | Monitoramento e captura de erros               |
| `flake8`, `ruff`             | Linting e qualidade de código                  |
| `pytest`, `pytest-django`    | Testes e integração com Django                 |
| `pytest-cov`                 | Cobertura de testes                            |
| `taskipy`                    | Automação de tarefas com comandos simplificados|

## 📂 Instalação e Uso Local

1. Clone o projeto:

```bash
git clone https://github.com/david0407j/petshoop-leo.git
cd petshoop-leo


Instale as dependências com Poetry:

poetry install
poetry shell

Configure o arquivo .env:

DEBUG=True
SECRET_KEY=sua-chave-secreta
DATABASE_URL=postgres://usuario:senha@localhost:5432/nomedb
AWS_ACCESS_KEY_ID=sua-chave
AWS_SECRET_ACCESS_KEY=sua-chave
AWS_STORAGE_BUCKET_NAME=seu-bucket

Rode as migrações e o servidor:

python manage.py migrate
python manage.py runserver

Execute os testes automatizados:
pytest



