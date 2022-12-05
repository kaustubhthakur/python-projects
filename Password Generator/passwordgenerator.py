import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','i','o','p','q','r','s','t','S','A','T','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','*','(',')']
print("welcome to the password generator")
l_letters  = int(input("how many letter you want\n"))
l_symbols = int(input("how many symbols you want\n"))
l_numbers  = int(input("how many numbers you want\n"))


password = ""
for char in range(1,l_letters+1):
    password+=random.choice(letters)

for char in range(1,l_symbols+1):
    password+=random.choice(symbols)

    for char in range(1,l_numbers+1):
        password+=random.choice(numbers)


    print(password)