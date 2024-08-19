# Definindo cores
PURPLE = \033[0;35m
NC = \033[0m # No Color

# Nome do diretório do ambiente virtual
VENV_DIR = jogo_da_velha_env

# Cria o ambiente virtual e instala as dependências
venv: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: 
	@echo "$(PURPLE)Criando ambiente virtual... 🖥️$(NC)"
	@python3 -m venv $(VENV_DIR)
	@echo "$(PURPLE)Instalando dependências... ⚙️$(NC)"
	@$(VENV_DIR)/bin/pip install --upgrade pip
	@$(VENV_DIR)/bin/pip install -r requirements.txt

# Roda o jogo
run: venv
	@echo "$(PURPLE)Iniciando o jogo... 🎮$(NC)"
	@$(VENV_DIR)/bin/python3 ./game/main.py

# Executa os testes
test: venv
	@echo "$(PURPLE)Executando os testes... $(NC)"
	@$(VENV_DIR)/bin/python3 -m unittest discover -s ./game/tests

# Remove o ambiente virtual
clean:
	@echo "$(PURPLE)Removendo o ambiente virtual... 🧹🧼$(NC)"
	@rm -rf $(VENV_DIR)
