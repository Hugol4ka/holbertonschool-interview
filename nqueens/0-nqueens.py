#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Affiche le message d'usage standard et quitte avec le statut 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def parse_arguments():
    """Valide les arguments de la ligne de commande."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """Vérifie si une reine peut être placée sur board[row][col]."""
    # Vérifie la colonne vers le haut
    for i in range(row):
        if board[i] == col:
            return False
        # Vérifie les deux diagonales supérieures
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Utilise le backtracking pour trouver toutes les solutions."""
    if row == n:
        solution = [[r, board[r]] for r in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)



def main():
    n = parse_arguments()
    # board[r] stocke l'indice de colonne de la reine à la ligne r
    board = [-1] * n
    solutions = []
    
    solve_nqueens(n, 0, board, solutions)
    
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()