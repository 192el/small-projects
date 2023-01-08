board = [[' ' for _ in range(3)] for _ in range(3)]
def print_board():
    print (" 0 1 2")
    for i in range(3):
        print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
        if i < 2:
            print("  -----")

print_board()

def tie():
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

def win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return f"{board[i][0]} wins!"
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return f"{board[i][0]} wins!"
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return f"{board[i][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return f"{board[i][0]} wins!"
    return False



for i in range(9):
    row = int(input("Row number:\n"))
    column = int(input("Column number:\n"))
    try:
        if board[row][column] == ' ':
            board[row][column] = 'X' if i % 2 == 0 else 'O'
            print_board()
        else:
            print("That space is already taken!")
        if tie():
            print("It's a tie!")
            break
        if win():
            print(win())
            break
    except:
        print("Invalid input, try again")
        i -= 1
