from library import library2
from games import minigames
from tools import ministore

def menu():
    user_option=int(input("🙌 Select one in the menu that you want to enter🙌\n1.games\n2.ministore\n3.exit\n\n[1/2/3]:"))
    if user_option==1:
        minigames.start()
    elif user_option==2:
        ministore.start()
    elif user_option==3:
        library2.exit_menu()
    else:
        print("pilih yg tersedia")
     
def main():
     library2.welcome_message()
     menu()
if __name__=="__main__":
    main()      
    

           