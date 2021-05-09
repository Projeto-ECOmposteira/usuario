<div>
    <p align="center">
    <img src='https://raw.githubusercontent.com/Projeto-ECOmposteira/documentacao/main/assets/img/logo/logo.png' alt="Projeto Kokama" width="25%"/>
    </p> 
    <h1 align="center">
    Projeto ECOmposteira
    </h1>
</div>

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Projeto-ECOmposteira_usuario&metric=alert_status)](https://sonarcloud.io/dashboard?id=Projeto-ECOmposteira_usuario)
[![Maintainability](https://api.codeclimate.com/v1/badges/7c4d3fed40287bac69c6/maintainability)](https://codeclimate.com/github/Projeto-ECOmposteira/usuario/maintainability)

## Microsserviço de Usuário

O presente microsserviço disponibiliza informações relativas aos usuários, produtores agrícolas e supermercados. Nesse sentido, fornece meios para realizar login, cadastro e demais recursos pertinentes aos dados do usuário na plataforma.

## Rode o Backend com Docker

### Dependências

Inicialmente, instale localmente as seguintes dependências:

1. Instale o [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/);
2. Instale o [Docker Compose](https://docs.docker.com/compose/install/).

### Arquivo de Configuração

1. Crie um arquivo `.env` e preencha as variáveis de ambiente de acordo com os exemplos localizados nos arquivos `.env.example`.

### Inicialização do Projeto

1. Na pasta principal do projeto, construa e inicialize a aplicação com o comando:

```bash
sudo make
```

2. O microsserviço de usuário estará disponível em: `http://localhost:8001/`.
