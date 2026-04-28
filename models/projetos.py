class ProjetoIntegrador:
    def __init__(self, titulo, curso, periodo, _descricao):
        self.titulo = titulo
        self.curso = curso
        self.periodo = periodo
        self.descricao = _descricao

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "curso": self.curso,
            "periodo": self.periodo,
            "descricao": self.descricao
        }
    
    



    
