#API crud for book registration.
<hr>

Na pasta raiz do código insirir o seguinte comando `docker-compose up -d` a aplicação ira ser montada em um container docker e ficara a disposição na porta 5000.

Os testes estão na pasta SRC e possuem o nome tests.py para rodar os testes digite`py src/tests.py`

Para inserir os autores deve ser rodado os código `py src/insert.py`.

Para postar novos livros usar o exemplo:

`{
	"name": "teste01",
    "publication_year": 2019, 
    "edition": "2 edição", 
    "author": ["5ec44e21fc4168f0e37b1d74"]
}`