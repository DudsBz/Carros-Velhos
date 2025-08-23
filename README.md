# Aplicação de Estudo - FastAPI com Consumo em JavaScript e SQLite

Este repositório contém uma aplicação simples desenvolvida para estudos com FastAPI como backend, consumo via JavaScript no frontend, e banco de dados SQLite (simulado aqui com lista em memória para fins didáticos). O foco é aprendizagem prática da integração entre backend e frontend, tratamento de dados e solução de problemas comuns como CORS.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework Python rápido para construção de APIs RESTful.
- **JavaScript**: Consumo da API no frontend via Axios.
- **SQLite**: Para persistência de dados (na aplicação real, aqui está simulado com lista em memória).
- **CorsMiddleware** do FastAPI para permitir comunicação entre frontend e backend em origens diferentes.

---

## Funcionalidades Principais

- API REST para gerenciamento de uma lista de carros, com operações:
  - Listar todos os carros
  - Adicionar novo carro (com ID gerado automaticamente)
  - Consultar carro pelo ID
  - Deletar carro pelo ID
- Frontend simples em JavaScript para:
  - Exibir lista de carros obtida do backend
  - Formulário para cadastro de novos carros
- Configuração CORS para permitir requisições do frontend hospedado em `http://127.0.0.1:5500`

---

## Estrutura do Projeto

- `server.py` — Código do backend FastAPI:
  - Definição do modelo `Car` com campos: id, model, year, price.
  - Endpoints para CRUD básico na lista de carros.
  - Configuração CORS para comunicação frontend-backend.
  
- `script.js` — Código frontend JavaScript:
  - Função para carregar e renderizar a lista de carros.
  - Função para enviar novos carros via formulário para o backend.
  
- HTML (não incluso aqui) que contém elementos:
  - Lista para exibir carros (`id="lista_carros"`)
  - Formulário para cadastrar carros (`id="form_car"`, com input `id="input_model_car"`)

