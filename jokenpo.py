import random
moves = ["r", "p", "s"]
movenames = ["Rock", "Paper", "Scissors"]

computer_score = 0
player_score = 0

while True:
    print("choose your move: (r)ock (p)aper (s)cissors or (q)uit")
    player_move = input(">>>").lower()
    if player_move == "q":
        print("Thanks for playing!")
        break
    if player_move not in "rps":
        print("Invalid input, try again")
        continue
    computer_move = random.choice(moves)
    print(f"Computer chose {movenames[moves.index(computer_move)]}")
    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == "r":
        if computer_move == "paper":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player_move == "p":
        if computer_move == "scissors":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player_move == "s":
        if computer_move == "rock":
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
