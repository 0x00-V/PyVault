from os import system
import sys
from .manager import *


def notesMenu():
    system("clear||cls")
    while True:
        print("=== PyVault - Notes ===")
        print("1. List Notes")
        print("2. Add Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Back")
        print("6. Exit")
        print("===============")
        userInput = input("Input: ")

        match userInput:
            case "1":
                system("clear||cls")
                entries = manager.get_entries_by_category("note")
                for entry in entries:
                    print(f"ID: {entry.id} | Created At: {entry.created_at} | Title: {entry.title} | Content: {entry.content}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "2":
                system("clear||cls")
                title = input("Title: ")
                content = input("Content:")
                manager.add_note(title=title, content=content)
                system("clear||cls")
                print(f"Note added.\n\nTitle: {title}\nContent: {content}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "3":
                system("clear||cls")
                id = int(input("Enter the ID of the note you'd like to edit: "))
                title = input("Enter a new title, or leave blank to leave unchanged: ")
                content = input("Enter new content, or leave blank to leave unchanged:")
                print(manager.edit_entry("note" , id, title, content, "", "", ""))
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "4":
                system("clear||cls")
                entry_id = input("Enter the entry id: (Or type 'x' to cancel): ")
                try:
                    if entry_id != "x":
                        print(manager.delete_entry(int(entry_id)))
                except:
                    print("Invalid ID.")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "5":
                break
            case "6":
                system("clear||cls")
                print("Goodbye.")
                sys.exit()
            case _:
                system("clear||cls")
                print("!!!---Invalid input---!!!")


def tasksMenu():
    system("clear||cls")
    while True:
        print("=== PyVault - Tasks ===")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Back")
        print("6. Exit")
        print("===============")
        userInput = input("Input: ")

        match userInput:
            case "1":
                system("clear||cls")
                entries = manager.get_entries_by_category("task")
                for entry in entries:
                    print(f"ID: {entry.id} | Title: {entry.title} | Created At: {entry.created_at} | Content: {entry.content} | Completed: {entry.is_completed} | Due Date: {entry.due_date} | Priority: {entry.priority}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "2":
                system("clear||cls")
                title = input("Title: ")
                content = input("Content:")
                due_date = input("Due Date: ")
                priority = input("Priority: ")
                manager.add_task(title=title, content=content, is_completed=0, due_date=due_date, priority=priority)
                system("clear||cls")
                print(f"Task added.\n\nTitle: {title}\nContent: {content}\nDue Date: {due_date}\nPriority: {priority}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "3":
                system("clear||cls")
                id = int(input("Enter the ID of the task you'd like to edit: "))
                title = input("Enter a new title, or leave blank to leave unchanged: ")
                content = input("Enter new content, or leave blank to leave unchanged:")
                due_date = input("Enter new due date, or leave blank to leave unchanged: ")
                priority = input("Enter new priority, or leave blank to leave unchanged: ")
                print(manager.edit_entry("task" ,id, title, content, due_date, priority, ""))
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "4":
                system("clear||cls")
                entry_id = input("Enter the entry id: (Or type 'x' to cancel): ")
                try:
                    if entry_id != "x":
                        print(manager.delete_entry(int(entry_id)))
                except:
                    print("Invalid ID.")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "5":
                break
            case "6":
                system("clear||cls")
                print("Goodbye.")
                sys.exit()
            case _:
                system("clear||cls")
                print("!!!---Invalid input---!!!")


def bookmarksMenu():
    system("clear||cls")
    while True:
        print("=== PyVault - Bookmarks ===")
        print("1. List Bookmarks")
        print("2. Add Bookmark")
        print("3. Edit Bookmark")
        print("4. Delete Bookmark")
        print("5. Back")
        print("6. Exit")
        print("===============")
        userInput = input("Input: ")

        match userInput:
            case "1":
                system("clear||cls")
                entries = manager.get_entries_by_category("bookmark")
                for entry in entries:
                    print(f"ID: {entry.id} | Title: {entry.title} | Content: {entry.content} | Created At: {entry.created_at} | URL: {entry.url}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "2":
                system("clear||cls")
                title = input("Title: ")
                content = input("Content:")
                url = input("URL: ")
                manager.add_bookmark(title=title, content=content, url=url)
                system("clear||cls")
                print(f"Bookmark added.\n\nTitle: {title}\nContent: {content}\nURL: {url}")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "3":
                system("clear||cls")
                id = int(input("Enter the ID of the bookmark you'd like to edit: "))
                title = input("Enter a new title, or leave blank to leave unchanged: ")
                content = input("Enter new content, or leave blank to leave unchanged:")
                url = input("Enter new url, or leave blank to leave unchanged: ")
                print(manager.edit_entry("bookmark", id, title, content, "", "", url))
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "4":
                system("clear||cls")
                entry_id = input("Enter the entry id: (Or type 'x' to cancel): ")
                try:
                    if entry_id != "x":
                        print(manager.delete_entry(int(entry_id)))
                except:
                    print("Invalid ID.")
                input("\n------------------------\nPress Enter to continue\n------------------------\n")
                system("clear||cls")
            case "5":
                break
            case "6":
                system("clear||cls")
                print("Goodbye.")
                sys.exit()
            case _:
                system("clear||cls")
                print("!!!---Invalid input---!!!")


manager = Manager()
def mainMenu():
    system("clear||cls")
    while True:
        print("=== PyVault ===")
        print("1. Notes")
        print("2. Tasks")
        print("3. Bookmarks")
        print("4. Exit")
        print("===============")
        userInput = input("Input: ")

        match userInput:
            case "1":
                notesMenu()
                system("clear||cls")
            case "2":
                tasksMenu()
                system("clear||cls")
            case "3":
                bookmarksMenu()
                system("clear||cls")
            case "4":
                system("clear||cls")
                print("Goodbye.")
                sys.exit()
            case _:
                system("clear||cls")
                print("!!!---Invalid input---!!!")
