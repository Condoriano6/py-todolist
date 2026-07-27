'''
Module that main actions happen
'''
from colorama import Fore, Style
from task import Task
from storage import save_tasks, load_tasks

class TodoList:
    """
    Class that do everything for a task
    """

    def __init__(self):
        self.tasks = load_tasks()
        if self.tasks:
            self.next_id = max(task.task_id for task in self.tasks) + 1
        else :
            self.next_id = 1
    
    def get_header(self, prompt):
        print(Fore.LIGHTCYAN_EX + '=' * 80)
        print(prompt.center(80))
        print('=' * 80 + Style.RESET_ALL)

    def get_user_choice(self):
        '''
        get users choice and check for any errors
        '''
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid input! Please try again!" + Style.RESET_ALL)
            return -1
        return choice

    def get_task_id(self):
        '''
        Get task id from user and checks for errors
        '''
        try:
            search = int(input("Enter Task ID: "))
        except ValueError:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid input! Please try again!" + Style.RESET_ALL)
            return -1
        return search

    def add_task(self):
        '''
        Adding a task
        '''
        self.get_header("➕ ADD TASK")
        task_id = self.next_id
        title = input("Enter title: ")
        description = input("Enter description: ")
        while True:
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            if priority in ("High", "Medium", "Low"):
                break
            print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid priority! Please try again!" + Style.RESET_ALL)
        t = Task(task_id, title, description, priority)
        self.next_id += 1
        self.tasks.append(t)
        print(Fore.LIGHTGREEN_EX + "✅ Task added successfully!" + Style.RESET_ALL)
        save_tasks(self.tasks)
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)

    def find_by_id(self, search):
        '''
        Find the task
        '''
        for task in self.tasks:
            if task.task_id == search:
                return task
        print(Fore.LIGHTRED_EX + "❌ No task found!" + Style.RESET_ALL)
        return None

    def search_by_title(self, keyword):
        '''
        Find task by title
        '''
        results = []
        for task in self.tasks:
            if task.title.lower() in keyword.lower():
                results.append(task)
        return results

    def search_task(self):
        keyword = input("Search title (leave blank for canceling the search): ")
        if not keyword:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Search canceled!" + Style.RESET_ALL)
            return
        results = self.search_by_title(keyword)
        if not results:
            print(Fore.LIGHTRED_EX + "❌ No task found!" + Style.RESET_ALL)
            return
        self.show_task(results)
    
    def show_menu(self):
        while True:
            self.get_header("📋 SHOW TASKS")
            print(Fore.LIGHTWHITE_EX + "1. Sort task")
            print("2. Filter task")
            print("3. Back" + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)
            choice = self.get_user_choice()
            if choice == 1:
                self.sort_task()
            if choice == 2:
                pass
            if choice == 0:
                break
            if choice == -1:
                continue
            else:
                print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid choice! Please Try again!" + Style.RESET_ALL)
            
    def sort_task(self):
        while True:
            self.get_header("📋 SHOW TASKS")
            print(Fore.LIGHTWHITE_EX + "1. 🔥 Sort by Priority")
            print("2. ✅ Sort by Status")
            print("3. 🔤 Sort by Title")
            print("4. 🆔 Sort by ID")
            print("0. 🔙 Back" + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)
            choice = self.get_user_choice()
            if choice == 1:
                priority_order = {
                    "High": 1,
                    "Medium": 2,
                    "Low": 3
                }
                sorted_tasks = sorted(self.tasks, key= lambda task: priority_order[task.priority])
                self.show_task(sorted_tasks)
            elif choice == 2:
                sorted_tasks = sorted(self.tasks, key=lambda task: not task.status)
                self.show_task(sorted_tasks)
            elif choice == 3:
                sorted_tasks = sorted(self.tasks, key=lambda task: task.title.lower())
                self.show_task(sorted_tasks)
            elif choice == 4:
                sorted_tasks = sorted(self.tasks, key=lambda task: task.task_id)
                self.show_task(sorted_tasks)
            elif choice == 0:
                break
            elif choice == -1:
                continue
            else:
                print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid choice! Please Try again!" + Style.RESET_ALL)

    def show_task(self, tasks=None):
        '''
        Show the tasks
        '''
        if not tasks:
            print(Fore.LIGHTBLUE_EX + "📭 Task list is empty!" + Style.RESET_ALL)
            return
        self.get_header(f"Total Tasks: {len(tasks)}")
        spliter = Fore.LIGHTCYAN_EX + "|" + Style.RESET_ALL
        print(f"{Fore.LIGHTWHITE_EX}{'Id':<5}" \
              f"{spliter}{Fore.LIGHTWHITE_EX}{'Title':<20}" \
              f"{spliter}{Fore.LIGHTWHITE_EX}{'Description':<30}" \
              f"{spliter}{Fore.LIGHTWHITE_EX}{'Priority':<10}" \
              f"{spliter}{Fore.LIGHTWHITE_EX}{'Status':<10}{spliter}")
        print(Fore.LIGHTCYAN_EX + '-' * 80 + Style.RESET_ALL)
        for task in tasks:
            print(task.to_row())
        print(Fore.LIGHTCYAN_EX + '-' * 80 + Style.RESET_ALL)
        self.search_task()
        
    def delete_task(self):
        '''
        Delete the task
        '''
        if not self.tasks:
            print(Fore.LIGHTBLUE_EX + "📭 Task list is empty!" + Style.RESET_ALL)
            return
        self.get_header("🗑  DELETE TASK")
        search = self.get_task_id()
        if search == -1:
            return
        task = self.find_by_id(search)
        if task is None:
            return
        while True:
            confrim = input(f"Are you sure you want do delete \"{task.title}\"? (y/n): ").lower()
            if confrim == 'y':
                self.tasks.remove(task)
                print(Fore.LIGHTGREEN_EX + f'✅ Task \"{task.title}\" is deleted!' + Style.RESET_ALL)
                save_tasks(self.tasks)
                break
            if confrim =='n':
                print(Fore.LIGHTRED_EX + "❌ Deleting process canceled!" + Style.RESET_ALL)
                break
            print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid input! Please try again!" + Style.RESET_ALL)
            continue
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)

    def mark_as_done(self):
        '''
        Marks tasks as done
        '''
        if not self.tasks:
            print(Fore.LIGHTBLUE_EX + "📭 Task list is empty!" + Style.RESET_ALL)
            return
        self.get_header("✅ MARKING A TASK AS DONE")
        search = self.get_task_id()
        if search == -1:
            return
        task = self.find_by_id(search)
        if task is None:
            return
        if task.mark_done():
            save_tasks(self.tasks)
            print(Fore.LIGHTGREEN_EX + "✅ Task marked as done!" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Task is already done!" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)

    def mark_as_undone(self):
        '''
        Marks tasks as undone
        '''
        if not self.tasks:
            print(Fore.LIGHTBLUE_EX + "📭 Task list is empty!" + Style.RESET_ALL)
            return
        self.get_header("⏳ MARKING A TASK AS UNDONE")
        search = self.get_task_id()
        if search == -1:
            return
        task = self.find_by_id(search)
        if task is None:
            return
        if task.mark_undone():
            save_tasks(self.tasks)
            print(Fore.LIGHTGREEN_EX + "✅ Task marked as undone!" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Task is already undone!" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)

    def edit_task(self):
        '''
        Edit the task
        '''
        if not self.tasks:
            print(Fore.LIGHTBLUE_EX + "📭 Task list is empty!" + Style.RESET_ALL)
            return
        self.get_header("✏️ EDIT TASK")
        search = self.get_task_id()
        if search == -1:
            return
        task = self.find_by_id(search)
        if task is None:
            return
        new_title = input("Enter new title (leave blank to keep current): ")
        new_description = input("Enter new description (leave blank to keep current): ")
        if task.edit(new_title, new_description):
            save_tasks(self.tasks)
            print(Fore.LIGHTGREEN_EX + "✅ Task updated!" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nothing changed!" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)

    def statistics(self):
        total = len(self.tasks)
        done = 0
        for task in self.tasks:
            if task.status:
                done += 1
        undone = total - done
        if total == 0:
            percent = 0
        else: 
            percent = (done / total) * 100
        bar_length = 20
        filled = int((percent / 100) * bar_length)
        bar = '█' * filled + '-' * (bar_length - filled)
        self.get_header("📊 STATISTICS")
        print(Fore.LIGHTWHITE_EX + f"📌 Total Tasks: {total}")
        print(Fore.LIGHTWHITE_EX + f"✅ Done: {done}")
        print(Fore.LIGHTWHITE_EX + f"⏳ Undone: {undone}")
        print(Fore.LIGHTWHITE_EX + f"📈 Progress: {bar} {percent:.2f}%")
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)
        