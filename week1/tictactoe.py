def show_board(board):
    print("\n  1   2   3")
    for i in range(3):
        row_str = f"{i+1} "
        for j in range(3):
            row_str += board[i][j] if board[i][j] != " " else "."
            if j < 2:
                row_str += " | "
        print(row_str)
        if i < 2:
            print("  -----------")
    print()


def check_winner(board, mark):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [mark, mark, mark] in lines


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def player_move(player, mark, board):
    while True:
        try:
            raw = input(f"Player {player} ({mark}) - Enter row col: ")
            r, c = map(int, raw.split())
            if 1 <= r <= 3 and 1 <= c <= 3:
                if board[r-1][c-1] == " ":
                    board[r-1][c-1] = mark
                    return
                else:
                    print("That spot is taken!")
            else:
                print("Coordinates must be between 1 and 3.")
        except ValueError:
            print("Enter two numbers separated by space.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = [(1, "X"), (2, "O")]
    turn = 0

    # show empty board at start
    show_board(board)

    while True:
        p, m = players[turn % 2]
        player_move(p, m, board)

        # show updated board
        show_board(board)

        if check_winner(board, m):
            print(f"🎉 Player {p} wins!")
            break
        if board_full(board):
            print("🤝 It's a draw!")
            break

        turn += 1


play_game()
