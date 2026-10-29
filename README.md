# ATV09 - Migração do Portal para Django

## Identificação
- Luiz Philippe de Lima Silva
- Miguel Barbosa Neto
- Manoel Fernando Cavalcante Cruz

Turma 513

## Descrição do projeto
Migração do Portal Acadêmico do Trio (ATV06, feito com HTML, CSS e
JavaScript) para uma aplicação Django. O menu e os conteúdos das páginas
ficam armazenados no banco de dados e são administrados pelo Django Admin.
A identidade visual e a responsividade da ATV06 foram mantidas.

## Tecnologias utilizadas
- Python 3
- Django
- SQLite
- HTML5 e CSS3 (Flexbox e Media Queries)

## Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/Miguell256/ATV09_Luiz_Miguel_Manoel.git
cd ATV09_Luiz_Miguel_Manoel
```

### 2. Criar o ambiente virtual
```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual
```bash

# Linux/macOS
source venv/bin/activate
```

### 4. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 5. Executar as migrations
```bash
python manage.py migrate
```

### 6. Carregar os dados iniciais (menu e conteúdos)
```bash
python manage.py loaddata dados_iniciais
```

### 7. Criar o superusuário
```bash
python manage.py createsuperuser
```

### 8. Executar o servidor
```bash
python manage.py runserver
```

### 9. Acessar a aplicação
- Portal: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

## Estrutura do projeto
- `core/`: configurações do projeto
- `portal/models.py`: models `Conteudo` e `Menu`
- `portal/views.py`: views e obtenção do menu
- `portal/context_processors.py`: disponibiliza o menu em todas as páginas
- `portal/urls.py`: rotas (`/` e `/conteudo/<slug>/`)
- `portal/templates/portal/`: templates (base, index, conteudo)
- `portal/static/portal/`: CSS e imagens
- `portal/fixtures/`: dados iniciais
