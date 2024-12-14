# ReviewsApp

ReviewsApp é uma aplicação web desenvolvida com Django que permite aos usuários criar, gerenciar e categorizar reviews (avaliações). O projeto facilita a organização de reviews em diferentes categorias.

## Índice

- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo a Passo](#passo-a-passo)
- [Uso](#uso)
  - [Executando o Servidor de Desenvolvimento](#executando-o-servidor-de-desenvolvimento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

## Funcionalidades

- **Gerenciamento de Reviews:**
  - Criar novas reviews com título, conteúdo, nota e categoria.
  - Editar reviews existentes.
  - Visualizar detalhes das reviews.
  - Remover reviews com funcionalidade de deleção suave (soft delete).

- **Gerenciamento de Categorias:**
  - Organizar reviews em categorias pré-definidas.
  - Filtrar reviews por categoria.

## Instalação

### Pré-requisitos

Antes de iniciar a instalação, certifique-se de que os seguintes itens estão instalados no seu sistema:

- **Python 3.x:** [Download Python](https://www.python.org/downloads/)
- **pip:** Gerenciador de pacotes do Python (geralmente instalado com Python)
- **Virtualenv:** Ferramenta para criar ambientes virtuais Python (opcional, mas recomendado)

### Passo a Passo

Siga os passos abaixo para instalar e configurar o projeto localmente.

1. **Clone o Repositório**

   Primeiro, clone o repositório do projeto para o seu ambiente local.

   ```bash
   git clone https://github.com/FelipeVolkweis/apoo-django.git
   ```

2. **Navegue até o Diretório do Projeto**

   ```bash
   cd apoo-django/
   ```

3. **Crie e Ative o Ambiente Virtual**

   Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

   - **Criar o Ambiente Virtual:**

     ```bash
     python -m venv myenv
     ```

   - **Ativar o Ambiente Virtual:**

     - **Windows:**

       ```bash
       myenv\Scripts\activate
       ```

     - **Linux/Mac:**

       ```bash
       source myenv/bin/activate
       ```

4. **Instale as Dependências**
    ```bash
    pip install django
    ```

5. **Aplicar as Migrações**

   Crie e aplique as migrações para configurar o esquema do banco de dados.

   ```bash
   cd src/
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Executar o Servidor de Desenvolvimento**

   Inicie o servidor de desenvolvimento do Django:

   ```bash
   python manage.py runserver
   ```

   A aplicação estará acessível em `http://127.0.0.1:8000/`.

## Uso

### Executando o Servidor de Desenvolvimento

Após seguir os passos de instalação, execute o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação no seu navegador:

```
http://127.0.0.1:8000/
```

## Estrutura do Projeto

A seguir, uma visão geral da estrutura do projeto:

```
myproject/
├── myenv/                      # Ambiente virtual Python
├── src/                        # Diretório principal do projeto Django
|   ├── reviewsapp/             # Aplicação Django para gerenciamento de reviews
│   |   ├── migrations/         # Arquivos de migração do banco de dados
│   |   ├── templates/          # Templates HTML
│   |   │   └── reviews/        # Templates específicos da aplicação
│   |   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   |   ├── admin.py            # Configurações do Django Admin
│   |   ├── apps.py             # Configurações da aplicação
│   |   ├── forms.py            # Formulários para manipulação de dados
│   |   ├── models.py           # Modelos de dados
│   |   ├── views.py            # Views da aplicação
│   |   ├── urls.py             # URLs específicas da aplicação
│   |   └── ...                 # Outros arquivos e diretórios
|   ├── myproject               # Projeto Django
|   ├── db.sqlite3              # Arquivo do banco de dados SQLite
|   ├── manage.py               # Script de gerenciamento do Django
└── README.md                   # Documento de documentação do projeto
```

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**: Framework web para desenvolvimento rápido e eficiente.
- **SQLite**: Banco de dados relacional leve (padrão para Django).
- **Bootstrap 4.5**: Framework CSS para design responsivo e estilização.
- **Virtualenv**: Ferramenta para criação de ambientes virtuais Python.
  
---

Este README fornece um guia completo para instalar, configurar e utilizar o ReviewsApp, além de oferecer informações sobre as funcionalidades principais.