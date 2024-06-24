n = int(input())
board = []
gambler_pos = []
total_amount = 100
flag = False
directions = {
   "up": (-1, 0),
   "down": (1, 0),
   "left": (0, -1),
   "right": (0, 1)
}

for row in range(n):
    board.append(list(input()))
    if "G" in board[row]:
        gambler_pos = [row, board[row].index("G")]
        board[gambler_pos[0]][gambler_pos[1]] = "-"



command = input()

while command != "end":
    if command in directions:
        gambler_pos[0] = gambler_pos[0] + directions[command][0]
        gambler_pos[1] = gambler_pos[1] + directions[command][1]
        if 0 <= gambler_pos[0] < n and 0 <= gambler_pos[1] < n:
            if board[gambler_pos[0]][gambler_pos[1]] == "W":
                total_amount += 100
            elif board[gambler_pos[0]][gambler_pos[1]] == "P":
                total_amount -= 200
            elif board[gambler_pos[0]][gambler_pos[1]] == "J":
                total_amount += 100000
                print(f"You win the Jackpot! \nEnd of the game. Total amount: {total_amount}$")
                board[gambler_pos[0]][gambler_pos[1]] = "G"
                [print("".join(b)) for b in board]
            board[gambler_pos[0]][gambler_pos[1]] = "-"
            if 0 >= total_amount or total_amount >= 100000:
                break
        else:
            break
    command = input()

board[gambler_pos[0]][gambler_pos[1]] = "G"

if 0 < total_amount < 100000:
    print(f"End of the game. Total amount: {total_amount}$")
    [print("".join(b)) for b in board]

if total_amount <= 0 or not (0 <= gambler_pos[0] < n and 0 <= gambler_pos[1] < n):
    print("Game over! You lost everything!")

