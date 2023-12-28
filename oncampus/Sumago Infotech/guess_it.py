def guess_it():
    remaining_chances = 5
    is_true = True
    find_me = 27

    while is_true and remaining_chances > 0:
        guess = int(input("Enter number to guess: "))
        if guess == 27:
            remaining_chances -= 1
            print("The no is found, congratulations")
            print("Remaining chances: ", remaining_chances)
            is_true = False
            break
        elif guess < find_me - 5:
            remaining_chances -= 1
            print("you have to go up, it's too far")
            print("Remaining chances: ", remaining_chances)
            continue
        elif guess <= find_me - 1:
            remaining_chances -= 1
            print("you are about to reach, keep going")
            print("Remaining chances: ", remaining_chances)
            continue
        elif guess > find_me + 3:
            remaining_chances -= 1
            print("you are going too far")
            print("Remaining chances: ", remaining_chances)
            continue
        elif guess >= find_me + 1:
            remaining_chances -= 1
            print("you are going too far")
            print("Remaining chances: ", remaining_chances)
            continue

guess_it()