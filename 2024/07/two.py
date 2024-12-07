possible_operators = ['*', '+', '|']
res = 0

def gen_combinations(numbers: list) -> list:
    """
    Generate all possible combinations of operators between the numbers.
    """

    # Recursive function to build expressions
    def combine(current_expr, index):
        if index == len(numbers) - 1:
            combinations.append(current_expr)
            return
        
        for op in possible_operators:
            combine(current_expr + op + numbers[index + 1], index + 1)
    
    combinations = []

    combine(numbers[0], 0)
    return combinations

def evaluate_left_to_right(expression: str) -> int:
    # Split into numbers and operators
    parts, number = [], ''
    for char in expression:
        if char.isdigit():
            number += char
        else:
            parts.append(number)
            parts.append(char)
            number = ''
    if number:
        parts.append(number)

    # Evaluate strictly left-to-right
    cur_res = int(parts[0]) # Start with first number

    for i in range(1, len(parts) - 1, 2): # Iterate over operators and numbers
        cur_res = eval(f'{cur_res}{parts[i] if parts[i] != "|" else ""}{parts[i+1]}')

    return cur_res


for line in open('input.txt', 'r'):

    result = int(line.split()[0][:-1])
    combs = gen_combinations(numbers=line.split()[1:])

    for i in combs:
        out = evaluate_left_to_right(i)

        if out == result:
            res += result
            break

print(res)