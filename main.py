from Ui.Meniu import UI
from Repository.StudentRepo import StudentRepository
from Domain.StudentValidator import StudentValidator
from Controller.StudentService import StudentService
from Repository.DisciplinaRepo import DisciplinaRepository
from Domain.DisciplinaValidator import DisciplinaValidator
from Controller.DisciplinaService import DisciplineService
from Domain.NotaValidator import NotaValidator
from Repository.NoteRepo import NotaRepository
from Controller.NotaService import NotaService
from Repository.StudentRepo import StudentRepoFisier
from Repository.DisciplinaRepo import DisciplinaRepoFisier
from Repository.NoteRepo import NotaRepoFisier

repo = StudentRepoFisier('Data/Stud.txt')
repo1 = DisciplinaRepoFisier('Data/Disc.txt')
repo2 = NotaRepoFisier('Data/Note.txt')
validator = StudentValidator()
validator1 = DisciplinaValidator()
validator2 = NotaValidator()
service = StudentService(repo, validator)
service1 = DisciplineService(repo1, validator1)
service2 = NotaService(repo2, validator2, repo, repo1)
console = UI(service, service1, service2)
console.run()
