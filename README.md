# Projeto Kanban em python

# Sobre o projeto:

Projeto pessoal para aprendizado usando Kanban como inspiração. 
No app é possivel criar/excluir/listar cardboards, CRUD(criar, excluir, alterar, ler) notas, alterar posição das notas fazendo elas irem para o topo e mudar a nota de cardboard livremente.

# Layout
## Pagina Inicial
<p>
  <img src='https://github.com/JeanFurman/Kanban/blob/master/assets/kanban_readme/kanban_1.png'>
</p>

## Algumas Funções
<p>
  <img height='300' src='https://github.com/JeanFurman/Kanban/blob/master/assets/kanban_readme/MudaPosicao.gif'>&nbsp&nbsp
  <img height='300' src='https://github.com/JeanFurman/Kanban/blob/master/assets/kanban_readme/MudaCardboard.gif'>
</p>
<p>
  <img src='https://github.com/JeanFurman/Kanban/blob/master/assets/kanban_readme/CriarCardboard.gif'>
</p>
<p>
  <img height='300' src='https://github.com/JeanFurman/Kanban/blob/master/assets/kanban_readme/ExcluiNota.gif'>
</p>

# Tecnologias utilizadas
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Django-extensions</li>
  <li>Javascript</li>
  <li>Crispy forms</li>
  <li>PyCharm</li>
  <li>SQLite</li>
</ul>

# Como executar o projeto
Pré-requisito: Python 3.11.1, PIP e GIT Bash </br>
Na pasta que deseja clonar abra o Git bash
```bash
git init
git clone https://github.com/JeanFurman/Kanban.git
```
Execute o CMD do Windows na mesma pasta que fez o clone e siga os comandos.
```bash
cd Kanban
python -m venv venv
cd venv
cd scripts
activate
cd ..
cd ..
pip install -r requirements.txt
python env_gen.py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Acesse a URL mostrada no fim dos comandos.
# Autor
Jean Furman de Sousa
