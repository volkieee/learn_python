import main
def start():
    while True:
        print("welcome to Mini store")
        play_again=input("Kembali ke menu utama?[y/n]:")
        if play_again=="y":
            main.menu()
    
if __name__=="__main__":
    start()    