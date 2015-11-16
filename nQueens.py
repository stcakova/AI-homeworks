import math

def no_conflict(new_row, new_column, solution):
  for row in range(new_row):
    if(solution[row]       == new_column           or
       solution[row] + row == new_column + new_row or
       solution[row] - row == new_column - new_row):
      return False
  return True
             
def queensproblem(rows, columns):
  solutions = [[]]
  for row in range(rows):
    solutions = add_queen(row, columns, solutions)  # generates new solutions with `length++`
  return solutions                                  # based on solutions with `length`  

def add_queen(new_row, columns, prev_solutions):
  result = []
  for solution in prev_solutions:
    for new_column in range(columns):
      if no_conflict(new_row, new_column, solution):
        result.append(solution + [new_column])
  return result

for solution in queensproblem(7, 7):
  print(solution)
