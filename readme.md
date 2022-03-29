# Projeto Promental

### Descrição<br>
> Repositório com o sistema para visualização de dados do projeto promental. Utilizando o **Dash** é possível 
criar um ambiente web para a análise dos dados coletados.
### Equipe<br>
> Alunos: Matheus de Souza<br>
> Professores: Moisés Omena, Carlos Azevedo


### Características essenciais para a base de dados
><img src="https://raw.githubusercontent.com/matheuss3/promental-data-visualization/main/arquivos-auxiliares/data-quality.jpeg?token=GHSAT0AAAAAABSN64Q5ZWJZQ7N6RAPTPRNUYSCJVOA" width="500" alt="Data Quality">

### Preview page
><img src="https://raw.githubusercontent.com/matheuss3/promental-data-visualization/main/images/preview_dashboard.png?token=GHSAT0AAAAAABSN64Q4OUSJLZFLWLGDL2RCYSCJZHQ" width="1200" alt="Preview Page">
<br>


### Requisitos<br>
- Python3
- Libs: [pandas](https://pandas.pydata.org/), [dash](https://dash.plotly.com/)

### Instruções<br>
**Preparando a base de dados SQLite**
1. Criar um banco de dados SQLite chamado de *db.sqlite* na pasta database
2. Configurar as variáveis no arquivo *config.ini*, com o caminho do dataset e do banco de dados
3. E executar *main.py* da pasta etl<br>
**Executando o ambiente web**
4. Com o banco de dados criado basta executar o *app.py* utilizando o python3
