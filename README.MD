CONFIGURAR AMBIENTE NO WINDOWS 10:
https://www.youtube.com/watch?v=kkoJTBtj4ds

1° Passo: Download python penúltima versão
2° Passo: Instalar python
3° Passo: Colocar python e pip como variável ambiente
4° Passo: Coloque o powerSheel como administrador 
5° Passo: Rode esse comando  no powerShell "Set-ExecutionPolicy Unrestricted"
6° Passo: Criar pasta 
7° Passo: Abrir pasta no vs code
8° Passo: Abrir terminal do vs code
9° Passo: Rodar "python -m venv venv" para criar ambiente virtual, tudo que for instalado dentro do ambiente virtual é instalado apenas na pasta do projeto
10° Passo: Ativar ambiente virtual ".\venv\Scripts\activate"
11° Passo: Instalar flask "pip install flask"


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
