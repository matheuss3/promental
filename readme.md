# Projeto Promental

### Descrição<br>
> Repositório com o sistema para visualização de dados do projeto promental. Utilizando o **Dash** é possível 
criar um ambiente web para a análise dos dados coletados.

### Equipe<br>
> Alunos: Matheus de Souza<br>
> Professores: Moisés Omena, Carlos Azevedo

### Requisitos<br>
- Python3
- Libs: [pandas](https://pandas.pydata.org/), [dash](https://dash.plotly.com/)

### Instruções<br>
Para executar o código é necessário:<br>
**Preparando a base de dados SQLite**<br>
1. Criar um banco de dados SQLite chamado de *db.sqlite* na pasta database
2. Configurar as variáveis no arquivo *config.ini*, com o caminho do dataset e do banco de dados
3. E executar *main.py* da pasta etl
**Executando o ambiente web**<br>
4. Com o banco de dados criado basta executar o *app.py* utilizando o python3