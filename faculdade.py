
class Faculdade():
    def __init__(self):
        self.alunos = list ()
        self.matriculas = list()
        self.cursos = list()
        self.modalidades = list()
        self.estagios = list()
        self.cargos = list()

       
    def inserirCargo(self,cargo):
        self.cargos.append(cargo)
    
    def inserirAluno(self,aluno):
        self.alunos.append(aluno)
        

    def inserirMatricula(self, matricula):
        self.matriculas.append(matricula)


    def inserirCurso(self, curso):
        self.cursos.append(curso)


    def inserirModalidade(self, modalidade):
        self.modalidades.append(modalidade)

    def imprimir(self):
        print(f'Aluno {self.alunos} da matricula {self.matriculas} do curso {self.cursos} esta na modalidade {self.modalidades} status Cursando ')


    def InserirEstagio(self,estagio):
        self.estagios.append(estagio)  


class Pessoa(Faculdade):
    def __init__(self,nome,data_nascimento,cpf):
       self.nome = nome 
       self.data_nascimento = data_nascimento
       self.cpf = cpf 



class Aluno(Pessoa,Faculdade):
    def __init__(self,matricula,curso,modalidade):
       self.matricula = matricula
       self.curso = curso
       self.modalidade = modalidade


    def logarAluno(self, aluno):   

        if aluno not in self.alunos:
            print(f'Nome ou matricula incorretos ! {self.alunos}')
        else:
            print(f'Acesso liberado !')

    def imprimirAluno(self):
        print(f'lista de aluno {self.alunos}')


class Funcionario(Pessoa,Faculdade):
     def __init__(self,cargo):
        self.cargos = cargo 
    