import socket
from time import sleep
pc_name=socket.gethostname()

def welcome_message():
    style="*"*(len(pc_name)+6)
    print(f"{style}")
    print(f"** {pc_name} **")
    print(f"{style}")
    
    
def exit_menu():
    sleep(1)
    print("3..")
    sleep(1)
    print("2..")
    sleep(1)
    print("1..")
    print("program dihentikan")
    exit()
if __name__=="__main__":
    welcome_message()  
    exit_menu()  