import random

HANGMAN = ("9","8","7","6","5","4","3","2","1","0")

MAX_WRONG = len(HANGMAN)-1

WORDS = ("PISAĆ","CZYTAĆ","JEŚĆ","KRAŚĆ")

word = random.choice(WORDS)

so_far = "-" *len(word)

wrong = 0

used = []

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)


    while True:
        guess = input("\n\nWprowadź literę: ")
        guess = guess.upper()
        if len(guess) == 1:
            while guess in used:
                print("Juz wykorzystałeś literę", guess)
                guess = input("Wprowadź literę: ")
                guess = guess.upper()
            used.append(guess)

            if guess in word:
                print(f"Tak! {guess} znajduje się w zagadkowym słowie")
                new = ""
                for i in range(len(word)):
                    if guess == word[i]:
                        new += guess
                    else:
                        new += so_far[i]
                so_far = new
            else:
                print(f"Niestety {guess} nie występuje w zagadkowym słowie")
                wrong += 1
            break
        print("Błąd: Wprowadź dokładnie jeden znak!")


if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Zostałeś powieszony!")
else:
    print("Odgadłeś!")

print(f"Zagadkowe słowo to {word}")
input("Aby zakończyć program, nacisnij klawisz Enter.")
