from os import system
import sys

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
                pass
                system("clear||cls")
            case "2":
                pass
                system("clear||cls")
            case "3":
                pass
                system("clear||cls")
            case "4":
                pass
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
                pass
                system("clear||cls")
            case "2":
                pass
                system("clear||cls")
            case "3":
                pass
                system("clear||cls")
            case "4":
                pass
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
                pass
                system("clear||cls")
            case "2":
                pass
                system("clear||cls")
            case "3":
                pass
                system("clear||cls")
            case "4":
                pass
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

mainMenu()