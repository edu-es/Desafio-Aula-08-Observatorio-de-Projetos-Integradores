from services.observatorio import executar_rota

# Para usar o código, basta retirar o # do comando desejado nas linhas abaixo e rodar o arquivo main.py.

# Testando a rota de cadastro de projetos com dados válidos e inválidos
#print(executar_rota("/projetos", "POST", {"titulo": "Hub Cultural", "curso": "ADS", "periodo": "2024.1", "descricao": "Projeto de integração para o curso de Análise e Desenvolvimento de Sistemas."})) 
# print(executar_rota("/projetos", "POST", {"titulo": "", "curso": "", "periodo": "", "descricao": ""})) 

# Testando se quando um projeto é cadastrado, ele aparece na lista de projetos
# print(executar_rota("/projetos", "GET"))

#Adicionando mais um projeto para testar a busca por nome e filtro por curso
#print(executar_rota("/projetos", "POST", {"titulo": "Olhos abertos", "curso": "ADS", "periodo": "2024.1", "descricao": "Projeto de integração para o curso de Análise e Desenvolvimento de Sistemas."}))

# Testando se o novo projeto foi adicionado e aparece na lista de projetos
#print(executar_rota("/projetos", "GET"))

# Testando a busca por nome de projeto
#print(executar_rota("/projetos/buscar", "GET", {"titulo": "Olhos abertos"}))

# Testando a função de mostrar descrição de um projeto
# print(executar_rota("/projetos/descricao", "GET", {"titulo": "Olhos abertos"}))

# Testando a atualização da descrição de um projeto
#print(executar_rota("/projetos/atualizar_descricao", "PUT", {"titulo": "Olhos abertos", "descricao": "Nova descrição para o projeto Olhos abertos."}))

# Testando a busca de projetos filtrados por curso
#print(executar_rota("/projetos/filtrar_por_curso", "GET", {"curso": "ADS"}))

# Testando o retorno de uma rota inexistente
#print(executar_rota("/algumarota", "GET"))

