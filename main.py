from pprint import pprint
from functions import solve_sudoku

puzzle = [
[-1, -1, 3,     -1, -1, -1,     -1, 8, 7],
[-1, 5, -1,     8, -1, -1,      -1, -1, -1],
[-1, -1, -1,    -1, 7, 4,       3, 9, -1],

[2, -1, 5,      -1, -1, -1,     4, -1, -1],
[3, -1, 1,      4, 5, 6,        -1, 7, 2],
[8, -1, 6,      3, -1, 7,       5, 1, 9],

[-1, 1, 4,      7, -1, 2,       -1, -1, -1],
[-1, 3, -1,     -1, 8, 5,       -1, -1, 1],
[-1, -1, 7,     -1, -1, -1,     9, -1, -1]
]

# for i in range(1, 10):
#    print("Enter the numbers of the ", i, "row")
#    l = [int(input('1: ')), int(input('2: ')), int(input('3: ')),
#    int(input('4: ')), int(input('5: ')), int(input('6: ')),
#    int(input('7: ')), int(input('8: ')), int(input('9: '))]
#    puzzle.append(l)

print(solve_sudoku(puzzle))
pprint(puzzle)
