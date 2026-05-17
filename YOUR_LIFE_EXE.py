M = "Male"
F = "Female"
Y = "Yes"
N = "No"

s = (input("Please choose your Gender (M/F):- ")).lower()

if s in ("m","male"):
    print (f"Confirm Your Gender {M}")
elif s in ("f","female"):
    print (f"Confirm Your Gender {F}")
else:
    print("Invalid Option")
 
if s in ("m","male"):
    confirm = input("(Yes/No): ").lower()
    
    if confirm == "y":
        print(f"Your Gender Is Saved As {M}")
    else:
        print("Cancelled")

elif s in ("f","female"):
    confirm = input("(Y/N): ").lower()
    
    if confirm == "y":
        print(f"Your Gender Is Saved As {F}")
    else:
        print("Cancelled")
        
        
n = (input("Please Enter Your Name :- "))
print(f"\033[1mName Saved As {n}\033[0m")

print("\033[3m Every life is a series of choices carefully...There Is no going back..\033[0m")
input("... ")

print("\033[3m They say reality is stable… predictable… safe \033[0m")
input("... ")

print("\033[3m You open your eyes...\033[0m")
input("... ")

print("\033[3m what if nothing around me is actually real? \033[0m")
o = input("[Y] Look For Purpose Or [N] Just Start Living Around (Y/N) :- ").lower()


if o in ("y"):
    print("\033[3m You follow the thought \033[0m")
    input("... ")
    
    print("\033[3m 'Your senses are lying to you' \033[0m")
    input("... ")
    
    c1 = input("[Y] Follow others Or [N] Follow Your Own Path (Y/N): ").lower()
    
    if c1 == "y":
        print("\033[3m You become what they expect... safe, but empty. \033[0m")
    else:
        print("\033[3m You walk alone... truth feels heavy. \033[0m")
    
    print("\033[3m Life gets harder... nothing changes. \033[0m")



elif o in ("n"):
    print("\033[3m Just start living \033[0m")
    input("... ")
    
    print("\033[3m Life gets harder... Nothing feels certain... \033[0m")
    
    c2 = input("[Y] Give up Or [N] Keep pushing forward :- ").lower()
    
    if c2 == "y":
        print("\033[3m You let go... everything fades quietly. \033[0m")
    else:
        print("\033[3m You resist... even without meaning. \033[0m")
    
    print("\033[3m You meet some people \033[0m")
    
    c3 = input("[Y] Trust them Or [N] Stay distant :- ").lower()
    
    if c3 == "y":
        print("\033[3m You feel warmth... but fear losing it. \033[0m")
    else:
        print("\033[3m You stay cold... but safe. \033[0m")

print("\033[3m You keep your distance… but life keeps moving...\033[0m")


print (f" Thanks for Playing This game {n}")
print (f" Thanks for Playing This game {n}")
print (f" Thanks for Playing This game {n}")
print (f" Thanks for Playing This game {n}")



credits=" Shitty ass code wriiten by                                                                                                                                                 @imnotdrunkyawr//juniorcantcode"

print(credits * 7)