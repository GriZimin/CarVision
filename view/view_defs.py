import webbrowser
def check():
    print("Hello World")

def openGitHub():
    webbrowser.open("https://github.com/GriZimin/ComputerVision")

def openDocumentation():
    webbrowser.open("grizimin.github.io/ComputerVision/")

def FileMenuHandler(choice):
    if (choice == "Импорт"):
        pass
    if (choice == "Экспорт"):
        pass
    if (choice == "Выйти"):
        exit(0)

def HelpMenuHandler(choice):
    if (choice == "Документация"):
        openDocumentation()
    if (choice == "GitHub"):
        openGitHub()


