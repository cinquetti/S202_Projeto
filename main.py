'''
Projeto Prático Banco de Dados II

Nome: Lucas Cinquetti Moreira
Matrícula: 330
'''

from database import Database
from task_manager import TaskManager
from cli import CLI

def main():
    db = Database("bolt://34.227.142.138:7687", "neo4j", "bead-orange-belief")
    task_manager = TaskManager(db)
    cli = CLI(task_manager)
    cli.run()
    db.close()

if __name__ == "__main__":
    main()
