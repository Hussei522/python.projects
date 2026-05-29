import random 

words = [ "python", "computer", "keyboard", "program", "internet", "variable", "function", "developer", "monitor", "network", "science","library", "package", "database", "algorithm", "software", "hardware", "terminal", "project", "debugging", "compiler", "framework", "machine", "security", "app", "storage", "gaming", "browser", "system", "automation"]
word = random.choice(words)

display = []
for letter in word :
    display.append("_")
print(" ".join(display))

guess = input("enter a letter:").lower()
for position in range(len(word)):
    letter = word[position]
    if letter == guess:
        display[position] = letter
        print(display[position])
    else:
        print("wrong")



















#for distance in word:
    print("_", end=" ")
#uess = input("Please guess a letter:").lower()
#while guess in distance:
 #       print(guess.join(distance))
                     
