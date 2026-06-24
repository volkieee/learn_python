import random
import main
def start():
    while True:
        volka=random.randint(1,4)
        bentuk_goa="|_|"
        goa_kosong=[bentuk_goa]*4
        goa=goa_kosong.copy()
        goa[volka-1]="|0_0|"

        goa_kosong=' '.join(goa_kosong)
        goa=' '.join(goa)


        print(f"coba perhatikan goa ini \n {goa_kosong}")
        user_choice=int(input("Dinomor berapa volka berada? [1/2/3/4]: "))
        while user_choice <1 or user_choice>4:
            user_choice=int (input("isi angka yang bener:"))
        if user_choice==volka:
                print(f"{goa}\n selamat kamu menang!")
        else:
                print(f"{goa}\n kamu kalah!")
        
        play_again=input("\n\n apakah ingin melanjutkan gamenya lagi?[y/n]:")
        if play_again=="n":
            main.menu()
            
    
    
if __name__=='__main__':
    start()      