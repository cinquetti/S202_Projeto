'''
Projeto Prático Banco de Dados II

Nome: Lucas Cinquetti Moreira
'''

from database import Database
from task_manager import TaskManager
from cli import CLI

def main():
    # Coloque a sua instância do Neo4j
    db = Database("bolt://localhost", "neo4j", "password")
    task_manager = TaskManager(db)
    cli = CLI(task_manager)
    cli.run()
    db.close()

if __name__ == "__main__":
    main()
