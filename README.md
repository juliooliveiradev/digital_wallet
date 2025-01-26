# Digital Wallet API

## Como Rodar o Projeto

### 1. Configuração do Ambiente

#### 1.1 Usando Docker

O projeto pode ser rodado utilizando Docker para facilitar a configuração do ambiente e garantir que o ambiente de desenvolvimento seja idêntico ao de produção. Para rodar o projeto com Docker, siga os passos abaixo:

# 1. Clone o repositório:
   ```
   git clone https://github.com/seu_usuario/digital_wallet.git
   cd digital_wallet
   ```
Construa e inicie os containers do Docker:

````
docker-compose up --build
````

O banco de dados será configurado automaticamente com as credenciais especificadas no arquivo .env.

Para rodar o servidor, acesse o container do Django:

````
docker exec -it digital_wallet_web bash
````

Acesse a aplicação através de http://localhost:8000.

## 1.2 Sem Docker (Modo Local)
Clone o repositório:

````
git clone https://github.com/seu_usuario/digital_wallet.git
cd digital_wallet
````

Crie e ative o ambiente virtual:

````
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
````
Instale as dependências:

````
pip install -r requirements.txt
````
Configure o banco de dados (PostgreSQL):

Edite o arquivo digital_wallet/settings.py com suas credenciais do PostgreSQL.
Execute as migrações:

````
python manage.py migrate
````
Popule o banco de dados com dados fictícios:

````
python manage.py populate_db
````
Rode o servidor:

````
python manage.py runserver
````

# 2. Testar a API
Você pode testar as rotas usando ferramentas como Postman ou Insomnia.

Endpoints
- POST /register: Criar usuário.
- POST /login: Login e obter token JWT.
- POST /add_balance: Adicionar saldo à carteira.
- POST /create_transaction: Criar transferência entre usuários.
- GET /list_transactions: Listar transações do usuário.

# 3. Testes Automatizados

Para garantir a qualidade do código e a funcionalidade da API, testes automatizados foram implementados utilizando o Django Test Framework. Para rodar os testes, execute o seguinte comando:

````
python manage.py test
````

Os testes garantem que todas as funcionalidades da API, como registro de usuários, login, criação de transações e manipulação de saldo, estão funcionando corretamente.

# 4. Linter (Flake8)
O Flake8 foi utilizado como linter para garantir a qualidade e a padronização do código. O Flake8 analisa o código Python em busca de problemas de estilo, erros de sintaxe, e outros problemas que podem impactar a legibilidade e a manutenção do código. A decisão de usar o Flake8 foi tomada por sua popularidade e facilidade de integração com o processo de desenvolvimento, ajudando a manter um padrão de código consistente e a evitar problemas comuns.

Para rodar o Flake8, execute:

````
flake8
````
## Conclusão
Este é um guia completo para implementar o desafio com Django. Ele cobre a configuração do ambiente de desenvolvimento, a estruturação do banco de dados, autenticação JWT, funcionalidades da API de gerenciamento de carteiras digitais e transações financeiras, além de garantir a qualidade do código com testes automatizados e linter.
