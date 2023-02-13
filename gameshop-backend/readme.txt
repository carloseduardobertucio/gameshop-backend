Tecnologias do projeto:
.Python 3.11.2
.Postgresql 15
.Flask

Como executar:
.Instalar o postgres com as seguintes configurações:
     database: postgres, user: postgres, password: 1234, port: 5432
.Executar o gameshop-database.sql para criação das tabelas e dados base.
.Instalar as dependencias contidas no arquivo requirements.txt
.Dentro da pasta gameshop-api, executar o comando "flaks --app app run" para iniciar o servidor de desenvolvimento.

Rotas para requisitos funcionais:
./api/login: [O usuário deverá fazer login]
./api/get-games: [O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética.]
./api/new-sale: [O usuário pode realizar checkout de seu carrinho de compras..]
./api/get-sales: [O usuário pode consultar os pedidos feitos.]