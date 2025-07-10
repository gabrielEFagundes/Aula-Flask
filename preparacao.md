# COMANDOS PARA PREPARAÇÃO DE AMBIENTE PYTHON

### Criar pasta .venv:
> python -m venv .venv

### Ativar pasta
> .venv\Scripts\activate

### Instalar Flask
> pip install flask

### Instalar o SQLAlchemy e o Flask-Migrate
> pip install Flask-SQLAlchemy Flask-Migrate

### Executar o bando de dados no models
> flask db init

### Atualizar o BD após alterações
> flask db migrate -m "mensagem"

### Enviar essas atualizações para o BD
> flask db upgrade

***

### Formulários em FLASK
> pip install flask-WTF

### Bilioteca para validar emails
> pip install email_validator

### Segurança do banco de dados
> pip install flask-dotenv

### Senhas aleatórias
> pip install flask-bcrypy

### Validação de usuários
> pip install flask-login