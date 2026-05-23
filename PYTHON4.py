name =(input("Please Enter your Name :- "))
age= int(input("Please Enter Your Age :- "))


if age >=18:
    print (f"{name}You are eligible to vote gng")
else:
    print(f"{name} You are not eligible to vote You have to wait {18-age} years")