'''
Main menu of the program
'''
from colorama import Fore, Style

from todolist import TodoList


def get_user_choice():
    '''
    get users choice and check for any errors
    '''
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid input! Please try again!" + Style.RESET_ALL)
        return -1

    return choice


def mainmenu():
    '''
    main menu
    '''
    todo = TodoList()
    while True:
        print(Fore.LIGHTCYAN_EX + '=' * 80)
        print("📝 TODOLIST".center(80))
        print('=' * 80 + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + "1. ➕ Add task")
        print("2. 📋 Show tasks")
        print("3. 🗑 Delete task")
        print("4. ✅ Mark as done")
        print("5. ⏳ Mark as undone")
        print("6. ✏️ Edit task")
        print("7. 📊 Statistics")
        print("0. 🚪 Exit" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + '=' * 80 + Style.RESET_ALL)
        choice = get_user_choice()
        if choice == 1:
            todo.add_task()
        elif choice == 2:
            todo.show_menu()
        elif choice == 3:
            todo.delete_task()
        elif choice == 4:
            todo.mark_as_done()
        elif choice == 5:
            todo.mark_as_undone()
        elif choice == 6:
            todo.edit_task()
        elif choice == 7:
            todo.statistics()
        elif choice == 0:
            break
        elif choice == -1:
            continue
        else:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Invalid choice! Please Try again!" + Style.RESET_ALL)


if __name__ == "__main__":
    mainmenu()
