int_secret = 15
bln_Erfolgreich = False

while not bln_Erfolgreich:
    int_guess = int(input("Guess the number!"))
    if int_secret == int_guess:
        print("Perfect, you guessed right, the number really was " + str(int_secret) + " !")
        bln_Erfolgreich = True
    else:
        bln_Erfolgreich=False
        if int_secret>int_guess:
            print("Guess again, the secret number is HIGHER than " + str(int_guess) + "!")
        else:
           print("Guess again, the secret number is LOWER than " + str(int_guess) + "!")