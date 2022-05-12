# 🧠 Projeto Promental

### Descrição<br>
> Repositório com o sistema para visualização de dados do projeto promental, utilizando o **Dash** com ele é possível criar um ambiente web para a análise dos dados coletados de forma visual e interativa.
### Equipe<br>
> Alunos: Matheus de Souza<br>
> Professores: Moisés Omena, Carlos Azevedo


### Características essenciais para a base de dados
><img src="https://github.com/matheuss3/promental-data-visualization/blob/main/extras/images/data-quality.jpeg?raw=true" width="500" alt="Data Quality">

### Preview page
><img src="https://github.com/matheuss3/promental-data-visualization/blob/main/extras/images/preview_dashboard_1.png?raw=true" width="1200" alt="Preview Page 1">
><img src="https://github.com/matheuss3/promental-data-visualization/blob/main/extras/images/preview_dashboard_2.png?raw=true" width="1200" alt="Preview Page 2">
<br>


### Requisitos<br>
- Python3
- Dependeces: [pandas](https://pandas.pydata.org/), [dash](https://dash.plotly.com/), dash_bootstrap_components

### Instruções<br>
**Preparando a base de dados SQLite**
- Criar um banco de dados SQLite chamado de *db.sqlite* na pasta database
- Configurar as variáveis no arquivo *config.ini*, com o caminho do dataset e do banco de dados
- E executar *main.py* da pasta etl<br>

**Executando o ambiente web com o dash**
- Com o banco de dados criado basta executar o *app.py* utilizando o python3
