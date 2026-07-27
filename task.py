'''
Module which has the Task class
'''
from colorama import Fore, Style


class Task:
    '''
    Task class
    '''
    def __init__(self, task_id, title, description, priority='Medium', status=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def to_row(self):
        '''
        returns the Task for showing it
        '''
        status = Fore.LIGHTGREEN_EX + "✅ Done" + Style.RESET_ALL if self.status else \
            Fore.LIGHTYELLOW_EX + "⏳ Undone" + Style.RESET_ALL
        if self.priority == "High":
            priority = "🔴 High"
        elif self.priority == "Medium":
            priority = "🟠 Meduim"
        elif self.priority == "Low":
            priority = "🟢 Low"
        spliter = Fore.LIGHTCYAN_EX + "|" + Style.RESET_ALL
        return f"{Fore.LIGHTWHITE_EX}{self.task_id:<5}{spliter}{Fore.LIGHTWHITE_EX}" \
        f"{self.title:<20}{spliter}{Fore.LIGHTWHITE_EX}{self.description:<30}{spliter}" \
        f"{Fore.LIGHTWHITE_EX}{priority:<10}{spliter}{Fore.LIGHTWHITE_EX}" \
        f"{status:<10}{spliter}"

    def mark_done(self):
        '''
        for marking a task done
        '''
        if self.status:
            return False
        self.status = True
        return True

    def mark_undone(self):
        '''
        for unmarking a task done
        '''
        if not self.status:
            return False
        self.status = False
        return True

    def edit(self, title, description):
        '''
        checks the final edit
        '''
        changed = False

        if title:
            self.title = title
            changed = True
        if description:
            self.description = description
            changed = True
        return changed

    def to_dict(self):
        '''
        Task to dict
        '''
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        '''
        dict to Task
        '''
        return cls(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("priority", "Medium"),
            data["status"]
        )
