# Projeto Promental

### Descrição<br>
> Repositório com o sistema para visualização de dados do projeto promental. Utilizando o **Dash** é possível 
criar um ambiente web para a análise dos dados coletados.
>#### Características essenciais para a base de dados
![Data Quality](https://raw.githubusercontent.com/matheuss3/promental-data-visualization/main/arquivos-auxiliares/Notebook_Megacity_V1/data-quality.jpeg?token=GHSAT0AAAAAABSN64Q4UBVRWSNZ55SHWF36YSCJTYQ)
|<br>
>#### Preview page
![Preview Pagina]()

### Equipe<br>
> Alunos: Matheus de Souza<br>
> Professores: Moisés Omena, Carlos Azevedo

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
