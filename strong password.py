import random
import string


print("Welcome to the password generator!")
total = int(input("Enter the total number of charcters in the password:"))
letters = int(input("Enter the number of letters in the password:"))
number = int(input("Enter the number of numbers in the password:"))
symbols = int(input("Enter the number of symbols in the password:"))

tatol = letters + number + symbols  


if tatol <= total:
        random_letters = random.choices(string.ascii_letters, k=letters)
        random_numbers = random.choices(string.digits, k=number)
        random_symbols = random.choices(string.punctuation, k=symbols)
        password = random_letters + random_numbers + random_symbols
      
        
        random.shuffle(password)
        password = "".join(password)
        
        print("Generated password ->:", password, ":<-")    
       


     
else:
    print("Invalid input, the total number of characters in the password is ", total , "and you have entered", tatol)
    