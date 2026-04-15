import sys
import copy

class SudokuCSP:
    def __init__(self, board):
        self.variables = [(r, c) for r in range(9) for c in range(9)]
        self.domains = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] != 0:
                    self.domains[(r, c)] = {board[r][c]}
                else:
                    self.domains[(r, c)] = set(range(1, 10))
        self.neighbors = {}
        for r in range(9):
            for c in range(9):
                n = set()
                for i in range(9):
                    if i != c: n.add((r, i))
                    if i != r: n.add((i, c))
                br, bc = 3 * (r // 3), 3 * (c // 3)
                for i in range(3):
                    for j in range(3):
                        if (br + i, bc + j) != (r, c):
                            n.add((br + i, bc + j))
                self.neighbors[(r, c)] = n
        self.backtrack_calls = 0
        self.backtrack_failures = 0

def revise(csp, xi, xj):
    revised = False
    to_remove = set()
    for x in csp.domains[xi]:
        if not any(x != y for y in csp.domains[xj]):
            to_remove.add(x)
    for x in to_remove:
        csp.domains[xi].remove(x)
        revised = True
    return revised

def ac3(csp, queue=None):
    if queue is None:
        queue = [(xi, xj) for xi in csp.variables for xj in csp.neighbors[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(csp, xi, xj):
            if not csp.domains[xi]:
                return False
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def select_unassigned_variable(assignment, csp):
    unassigned = [v for v in csp.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(csp.domains[var]))

def forward_check(csp, var, value, assignment):
    csp.domains[var] = {value}
    queue = [(neighbor, var) for neighbor in csp.neighbors[var] if neighbor not in assignment]
    return ac3(csp, queue)

def backtrack(assignment, csp):
    csp.backtrack_calls += 1
    if len(assignment) == 81:
        return assignment
    var = select_unassigned_variable(assignment, csp)
    original_domains = copy.deepcopy(csp.domains)
    for value in csp.domains[var]:
        if forward_check(csp, var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment, csp)
            if result:
                return result
            del assignment[var]
        csp.domains = copy.deepcopy(original_domains)
    csp.backtrack_failures += 1
    return None

def solve_sudoku(filename):
    with open(filename, 'r') as f:
        board = [[int(char) for char in line.strip()] for line in f.readlines()]
    csp = SudokuCSP(board)
    ac3(csp)
    assignment = {}
    for var in csp.variables:
        if len(csp.domains[var]) == 1:
            assignment[var] = list(csp.domains[var])[0]
    result = backtrack(assignment, csp)
    solution = [[0]*9 for _ in range(9)]
    if result:
        for (r, c), val in result.items():
            solution[r][c] = val
    return solution, csp.backtrack_calls, csp.backtrack_failures

if __name__ == "__main__":
    files = ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]
    for file in files:
        print(f"--- Solving {file} ---")
        try:
            solution, calls, failures = solve_sudoku(file)
            for row in solution:
                print("".join(map(str, row)))
            print(f"Calls: {calls} | Failures: {failures}\n")
        except FileNotFoundError:
            print(f"File {file} not found.")
