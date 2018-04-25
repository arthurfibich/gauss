"""addiere zur i-ten Zeile das x-fache der j-ten Zeile
    M wird modifiziert"""


def row_mod (M, i, j, x):
    M[i] = [a + x * b for a, b in zip(M[i], M[j])]
    print(M)


"""Bringe die Matrix in Reihen-Stufen-Form"""


def row_echelon(M):
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


"""Stufen oben rechts (nur Diagonale bleibt stehen))"""


def jordan(M):
    rows = len(M)
    cols = len(M[0])
    row = rows-1
    col = cols-2

    while row > 0 and col > 0:
        if M[row][col] == 0:
            # Zeilen über row durchgehen:
            for r in range(row):
                # Zellen rechts unten != 0 kriegen
                if M[r][col] != 0:
                    row_mod(M, row, r, 1)
                    break
        if M[row][col] == 0:
            col -= 1
            continue
        pivot = M[row][col]
        for r in range(row):
            if M[r][col] != 0:
                row_mod(M, r, row, -M[r][col] / pivot)
        row -= 1
        col -= 1


"""Kürzen auf 1 und Ausgabe der Ergebnisse in einen neuen Array"""


def onone(M):
    N = []
    for i in range(len(M[0])-1):
        N.append(M[i][len(M[0])-1] / M[i][i])
    return N

"""Gesamtablauf"""


def process(M):
    print(M)
    row_echelon(M)
    jordan(M)
    N = onone(M)
    print(N)
    return N


if __name__ == "__main__":
    M = [[1, 2, 3, 4],
         [4, 5, 6, 7],
         [-3, 0, 12, 15]]
    print(process(M))

"""Anmerkungen:
    M ist die Matrix, die letzte Stelle ist jeweils 'hinter dem Strich'
    Der Algorithmus funktioniert mit n-dimensionalen linearen Gleichungssystemen, solange gilt:
    n(Reihen) = n(Spalten) -1 , also 'links vom Strich ein Quadrat' ist.
    
    Genommen wurde das Gauss-Jordan-Verfahren.
    Dieses ist eine Erweiterung des Gauss-Verfahrens zur Lösung von LGS.
    Es lässt nicht nur die Stellen links, sondern auch die Stellen rechts der Diagonale 0 werden.
    Dadurch können die Werte direkt aus der Matrix abgelesen werden, was den gesamten Prozess einfacher macht.
    
    Das Vorgängermodell, das als normaler Gauss-Algorithmus konzipiert war hatte nicht berücksichtigt, dass die 
    Pivot-Elemente nicht 0 sein dürfen, was sie sehr oft werden, weshalb der Algorithmus in den Hausaufgaben die 
    falschen Ergebnisse geliefert hat. Komischerweise war dies bei meiner zufälligen Testmatrix nicht der Fall und das 
    Ergebnis war korrekt.
    
    Ich möchte mich nochmals dafür entschuldigen, die Hausaufgaben nicht gleich von Hand gemacht zu haben.
"""
