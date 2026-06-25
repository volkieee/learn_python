import random
import newmain
from time import sleep
def start():
    while True:
        volka_position=random.randint(1,4)
        
        shape_cave="|_|"
        empty_cave=[shape_cave]*4
        cave=empty_cave.copy()
        cave[volka_position-1]="|0_0|"
        
        empty_cave=' '.join(empty_cave)
        cave=' '.join(cave)
        
        user_option=int(input(f"Look at this cave\n{empty_cave}\n\nguess where the volka is[1/2/3/4]:"))
        while user_option <1 or user_option>4:
            user_option=int(input("please answer according to the instructions provided:"))
        if user_option==volka_position:
            print(f"\ncongrat ur right 🙌🙌🙌 volka is in {cave}")    
        else:
            print(f"\nwrong answer volka is in {cave} ")
        exit_volka=input("do u want to continue?[y/n]:")
        if exit_volka=="n":
            newmain.menu()
if __name__=="__main__":
    start()    