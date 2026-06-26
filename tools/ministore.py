import newmain
def start():
    while True:
        print("welcome to mini store")
        play_again=input("go back to the menu?[y/n]:")
        if play_again=="y":
            newmain.menu()

if __name__=="__main__":
    start()
    
    
    
    
    
    
    
    