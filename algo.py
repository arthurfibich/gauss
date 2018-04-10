"""addiere zur i-ten Zeile das x-fache der j-ten Zeile
    M wird modifiziert"""

def row_mod (M, i, j, x):
    M[i] = [a + x * b for a, b in zip(M[i], M[j])]

def row_echelon (M):
    row = 0
    col = 0
    rows = len(M)
    cols = len(M[0])

    while row < rows and col < cols:
        if M[row][col] == 0:
            # Zeilen unter row durchgehen:
            for r in range(row+1, rows):
                # Zellen links oben != 0 kriegen
                if M[r][col] != 0:
                    row_mod(M, row, r, 1)
                    break
        if M[row][col] == 0:
            col += 1
            continue
        pivot = M[row][col]
        for r in range(row + 1, rows):
            if M[r][col] != 0:
                row_mod(M, r, row, -M[r][col] / pivot)
        row += 1
        col += 1

if __name__ == "__main__":
    M = [[1, 2, 3], [4, 5, 6], [-3, 0, 12]]
    print(M)
    row_echelon(M)
    print(M)
