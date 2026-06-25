from library.library2 import welcome_message,exit_menu
from games import games
from tools import ministore
welcome_message()

def menu():
    user_option=int(input("\nselect one in the menu that you want to enter\n1.games\n2.ministore\n3.exit\n\n[1/2/3]:"))
    if user_option==1:
        games.start()
    elif user_option==2:
        ministore.start()
    elif user_option==3:
        exit_menu()
        
if __name__=="__main__":
    menu()        
    

           