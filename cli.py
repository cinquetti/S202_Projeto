from task_manager import TaskManager

class CLI:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def display_menu(self):
        print("Gerenciador de Tarefas")
        print("======================")
        print("1. Criar uma tarefa")
        print("2. Ler uma tarefa")
        print("3. Atualizar uma tarefa")
        print("4. Deletar uma tarefa")
        print("5. Sair")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_task()
            elif choice == '2':
                self.read_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_task(self):
        title = input("Digite o título da tarefa: ")
        description = input("Digite a descrição da tarefa: ")
        data = input("Digite a data da tarefa: ")
        self.task_manager.create_task(title, description, data)
        print("Tarefa criada com sucesso!")

    def read_task(self):
        title = input("Digite o título da tarefa a ser lida: ")
        task = self.task_manager.get_task(title)
        if task:
            print("Tarefa encontrada:", task)
        else:
            print("Tarefa não encontrada.")

    def update_task(self):
        title = input("Digite o título da tarefa a ser atualizada: ")
        new_title = input("Digite o novo título da tarefa (ou deixe vazio para não alterar): ")
        new_description = input("Digite a nova descrição da tarefa (ou deixe vazio para não alterar): ")
        new_date = input("Digite a nova data (ou deixe vazio para não alterar): ")
        self.task_manager.update_task(title, new_title if new_title else None, new_description if new_description else None, new_date if new_date else None)
        print("Tarefa atualizada com sucesso!")

    def delete_task(self):
        title = input("Digite o título da tarefa a ser deletada: ")
        self.task_manager.delete_task(title)
        print("Tarefa deletada com sucesso!")
