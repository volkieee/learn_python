from library import welcome_message ,exit_program
from games import volka
from tools import warung

def menu():
    user_option=int(input(f"silahkan pilih menu programnya:\n1.Games\n2.MiniStore\n3.exit\n\nSilahkan dipilih:"))
    if user_option==1:
        volka.start()
    elif user_option==2:
        warung.start()
    elif user_option==3:
        exit_program()
    else:
        print("hanya boleh pilih yang tersedia di menu  ")
    
def main():
    welcome_message()
    menu()
    
if __name__=='__main__':
    main()    
    

        

        

 
            
        

