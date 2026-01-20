
number = int(input("Enter a number to generate the random number (1-100): "))
random_number = (number * 7) % 100 + 1  # Generates a number between 1-100
print("Number has been set! 🎯")

while True:
    guess = int(input("Enter your guess: "))

    if guess != random_number:
        print("So close! Try again! ⬆️⬇️")
    else:
        print("🎉 CONGRATULATIONS! YOU GUESSED IT RIGHT! 🎊")
        break 
