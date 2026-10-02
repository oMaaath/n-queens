def is_safe(solution, row, column):
    #Check same row
    if row in solution:
        return 0
    
    #Check upper left
    for index, r in enumerate(solution):
        if column-index == row-r:
            return 0

    #Check lower left
    for index, r in enumerate(solution):
        if column-index == r-row:
            return 0

    return 1

def dfs_n_queens(n):
    if n < 1:
        return []
    elif n == 1:
        return [[0]]
    solutions = []
    stack = []
    stack.append(0)
    while stack:
        row = stack.pop()
        if(row >= n):
            #print(f"Queen reached out of boundaries; Popped stack: {stack} and moved down")
            if not stack:
                break
            stack[-1] += 1
        elif(is_safe(stack, row, len(stack))):
            #print(f"Queen is safe: reappend '{row}' and append new queen '0' to stack {stack}")
            stack.append(row)
            if(len(stack) >= n):
                #print(f"Solution found: taking down two queens")
                solutions.append(stack.copy())
                stack.pop()
                stack[-1] += 1
            else:
                stack.append(0)
        else:
            #print(f"Queen is not safe: reappend as '{row+1}' to stack {stack}")
            stack.append(row+1)
        #print(stack)
        #input("Next")
    return solutions

#Solutions for fact-checking it works
print("4 queens solutions:")
print(len(dfs_n_queens(4)))
for sol in dfs_n_queens(4):
    print(sol)

print('\n5 queens solutions:')
print(len(dfs_n_queens(5)))
for sol in dfs_n_queens(5):
    print(sol)

print('\n6 queens solutions:')
print(len(dfs_n_queens(6)))
for sol in dfs_n_queens(6):
    print(sol)

print('\n7 queens solutions:')
print(len(dfs_n_queens(7)))
for sol in dfs_n_queens(7):
    print(sol)

print('\n8 queens solutions:')
print(len(dfs_n_queens(8)))
for sol in dfs_n_queens(8):
    print(sol)
