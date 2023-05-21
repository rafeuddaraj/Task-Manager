from uuid import uuid1
from time import ctime


class Task_Manager:
    complete_task = []
    incomplete_task = []
    tasks = []
    def add_new_task(self,task_text):
        id = uuid1()
        if task_text != '':
            obj = {'id':id,'task': task_text,'created_time':ctime(),'updated_time': 'N/A','complete': False, 'complete_time': 'N/A'}
            Task_Manager.tasks.append(obj)
            Task_Manager.incomplete_task.append(obj)
            print('Task Created Successfully')
        else:
            pass
    def show_all_task(self):
        if Task_Manager.tasks:
            for i in range(len(Task_Manager.tasks)):
                mess = f"""\nTask No - {i+1}\nID - {Task_Manager.tasks[i]['id']}\nTask - {Task_Manager.tasks[i]['task']}\nCreated Time - {Task_Manager.tasks[i]['created_time']}\nUpdated time - {Task_Manager.tasks[i]['updated_time']}\nComplete - {Task_Manager.tasks[i]['complete']}\nComplete time - {Task_Manager.tasks[i]['complete_time']}
                """
                print(mess)
        else:
            print('No Task Available')
    def show_incomplete_task(self):
        if Task_Manager.incomplete_task:
            for i in range(len(Task_Manager.incomplete_task)):
                mess = f"""\nTask No - {i+1}\nID - {Task_Manager.incomplete_task[i]['id']}\nTask - {Task_Manager.incomplete_task[i]['task']}\nCreated Time - {Task_Manager.incomplete_task[i]['created_time']}\nUpdated time - {Task_Manager.incomplete_task[i]['updated_time']}\nComplete - {Task_Manager.incomplete_task[i]['complete']}\nComplete time - {Task_Manager.incomplete_task[i]['complete_time']}
                """
                print(mess)
        else:
            print('No Task Available')
    def show_complete_task(self):
        if not Task_Manager.complete_task:
            print('No Task Available')
        else:
            for i in range(len(Task_Manager.complete_task)):
                mess = f"""\nTask No - {i+1}\nID - {Task_Manager.complete_task[i]['id']}\nTask - {Task_Manager.complete_task[i]['task']}\nCreated Time - {Task_Manager.complete_task[i]['created_time']}\nUpdated time - {Task_Manager.complete_task[i]['updated_time']}\nComplete - {Task_Manager.complete_task[i]['complete']}\nComplete time - {Task_Manager.complete_task[i]['complete_time']}
                """
                print(mess)
    def update_task(self,task_no,task_text):
        task_no = task_no - 1
        if Task_Manager.tasks:
            if len(Task_Manager.tasks) >= task_no:
                    Task_Manager.tasks[task_no]['task'] = task_text
                    Task_Manager.tasks[task_no]['updated_time'] = ctime()
                    Task_Manager.incomplete_task[task_no]['updated_time'] = ctime()
                    print('Task Updated Successfully')
            else:
                print('Wrong Task no!')
        else:
            print('No Task Available')
    def mark_a_complete_task(self,task_no):
        task_no = task_no - 1
        if Task_Manager.incomplete_task:
            if task_no <= len(Task_Manager.incomplete_task):
                
                Task_Manager.tasks[task_no]['complete'] = True
                Task_Manager.tasks[task_no]['complete_time'] = ctime()
                Task_Manager.complete_task.append(Task_Manager.tasks[task_no])
                Task_Manager.incomplete_task.pop(task_no)
                print('Successfully completed')
            else:
                print('Worng Task no!')
        else:
            print('No Task Available')
task = Task_Manager()


while True:
    print("""1. Add New Task\n2. Show All Task\n3. Show Incomplete Tasks\n4. Show Complete Tasks\n5. Update Task\n6. Mark A Task Complete""")
    option = int(input('Enter Option: '))
    if option == 1:
        task_text = input('Enter New Task: ')
        task.add_new_task(task_text)
    elif option == 2:
        task.show_all_task()
    elif option == 3:
        task.show_incomplete_task()
    elif option == 4:
        task.show_complete_task()
    elif option == 5:
        task_no = int(input('Enter Task no: '))
        task_text = input('Enter New Task: ')
        task.update_task(task_no,task_text)
    elif option == 6:
        task_no = int(input('Enter Task no: '))
        task.mark_a_complete_task(task_no)