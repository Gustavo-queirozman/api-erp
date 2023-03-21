<h1>Api ERP</h1>
Api erp para empresa de manutenção de equipamentos.

<h2>Como rodar o projeto</h2>

<ol>
	<li>Download python 3.11.2</li>
	<pre><a href="https://www.python.org/downloads/">Baixar aqui</a></pre>
	<li>Instalar python</li>
	<li>Colocar python e pip como variável ambiente</li>
	<li>Coloque o powerSheel como administrador e rode esse comando:</li>
	<pre>Set-ExecutionPolicy Unrestricted</pre>
	<li>Abrir cmd e rodar</li>
	<pre>cd desktop & mkdir nome-do-projeto & cd nome-do-projeto</pre>
	<li>Ainda no cmd criar ambiente</li>
	<pre>python -m venv venv</pre>
	<li>Ainda no cmd ativar ambiente virtual</li>
	<pre>.\venv\Scripts\activate</pre>
	<li>Instalar flask</li>
	<pre>pip install flask</pre>
</ol>

<h2>Referência - Como configurar ambiente no windows 10</h2>
https://www.youtube.com/watch?v=kkoJTBtj4ds


<h3>Lógica da aplicação</h3>

USUÁRIOS

Cadastrar usuário:
	Para cadastrar o usuário a api tem que antes verificar se o usuário já é existente, se não for efetuar cadastro
	Colocar senha padrão. Assim forçando o usuário de refinir senha que será enviado um email para redefinição 

Fazer login:
	Procurar usuario e senha passado para a api no banco de dados, se encontrar retornar os dados. Caso contrário enviar "usuário não encontrado"

Resetar senha:
	Obter email, enviar nova senha no email do usuário

Modificar senha:
	Passar essas informações: email, senha, confirmarSenha. Validar esses dados e fazer alteração

JWT => criar token de autenticação


EQUIPAMENTOS:
Ver
Cadastrar(um por um)
Alterar(um por um)
Deletar(um por um)
