from models.projetos import ProjetoIntegrador


class Observatorio:
    def __init__(self):
        self.projetos = []
        

    

    def adicionar_projeto(self, titulo, curso, periodo, _descricao):
        if titulo == "":
            return {"mensagem": "O título do projeto não pode ser vazio.", "status": "erro"}
        if curso == "":
            return {"mensagem": "Curso não pode ser vazio.", "status": "erro"}
        if periodo == "":
            return {"mensagem": "Periodo não pode ser vazio.", "status": "erro"}
        if _descricao == "":
            return {"mensagem": "Descrição não pode ser vazio.", "status": "erro"}
        projeto = ProjetoIntegrador(titulo, curso, periodo, _descricao)
        self.projetos.append(projeto)
        return {"mensagem": "Projeto adicionado com sucesso.", "status": "successo"}
    
    def listar_projetos(self):
        return [{
            "titulo": p.titulo,
            "curso": p.curso,
            "periodo": p.periodo
        } for p in self.projetos]
    
    def buscar_projeto(self, titulo):
        for projeto in self.projetos:
            if projeto.titulo.lower() == titulo.lower():
                return [{
                    "titulo": projeto.titulo,
                    "curso": projeto.curso,
                    "periodo": projeto.periodo
                }]
        return {"mensagem": "Projeto não encontrado.", "status": "erro"}
    
    def filtrar_projetos_por_curso(self, curso):
        projetos_filtrados = [p.to_dict() 
            for p in self.projetos if p.curso.lower() == curso.lower()]     
        return projetos_filtrados

    def mostrar_descricao(self, titulo):
        for projeto in self.projetos:
            if projeto.titulo.lower() == titulo.lower():
                return {"titulo": projeto.titulo,
                        "descricao": projeto.descricao}
        return {"mensagem": "Projeto não encontrado.", "status": "erro"}
                
    def atualizar_descricao(self, titulo, nova_descricao):
        if nova_descricao == "":
            return {"mensagem": "A nova descrição do projeto não pode ser vazia.", "status": "erro"}
        for projeto in self.projetos:
            if projeto.titulo.lower() == titulo.lower():
                projeto.descricao = nova_descricao
                return {"mensagem": f"Descrição do projeto {titulo} atualizada para: '{nova_descricao}' ", "status": "sucesso"}
        return {"mensagem": "Projeto não encontrado.", "status": "erro"}
    

observatorio = Observatorio()

def get_projetos():
    return observatorio.listar_projetos()

def post_projeto(titulo, curso, periodo, descricao):
    return observatorio.adicionar_projeto(titulo, curso, periodo, descricao )

def get_projeto_por_nome(titulo):
    return observatorio.buscar_projeto(titulo)

def get_projetos_por_curso(curso):
    return observatorio.filtrar_projetos_por_curso(curso)

def get_descricao(titulo):
    return observatorio.mostrar_descricao(titulo)

def put_projeto(titulo, descricao):
    return observatorio.atualizar_descricao(titulo, descricao)

def executar_rota(rota, metodo, dados=None):
    if dados == None:
        dados = {}
    titulo = ""
    curso = ""
    periodo = ""
    descricao = ""
    
    for p in dados:
        if p == "titulo":
            titulo = dados["titulo"]
        if p == "curso":
            curso = dados["curso"]
        if p == "periodo":
            periodo = dados["periodo"]
        if p == "descricao":
            descricao = dados["descricao"]
    
    dados = {"titulo": titulo, "curso": curso, "periodo": periodo, "descricao": descricao}

    if rota == "/projetos" and metodo == "GET":
        return get_projetos()

    if rota == "/projetos" and metodo == "POST":
        return post_projeto(dados["titulo"], dados["curso"], dados["periodo"], dados["descricao"])

    if rota == "/projetos/buscar" and metodo == "GET":
        return get_projeto_por_nome(dados["titulo"])

    if rota == "/projetos/descricao" and metodo == "GET":
        return get_descricao(dados["titulo"])

    if rota == "/projetos/atualizar_descricao" and metodo == "PUT":
        return put_projeto(dados["titulo"], dados["descricao"])
    
    if rota == "/projetos/filtrar_por_curso" and metodo == "GET":
        return get_projetos_por_curso(dados["curso"])

    return {"mensagem" : "Rota não encontrada." , "status" : "erro"}

    


    
    