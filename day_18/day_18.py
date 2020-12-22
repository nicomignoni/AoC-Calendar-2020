with open("day_18.txt") as f:
    expressions = f.read().splitlines()

final_result = 0

def brackets_result_2(expression):
    result = [int(expression[0])]
    for i in range(1, len(expression) - 1, 1):
        if expression[i] == '+':
            result[-1] += int(expression[i + 1])
        elif expression[i] == '*':
            result.append(int(expression[i + 1]))
    prod = 1
    for n in result: prod *= n
    return str(prod)

def brackets_result(expression):
    result = int(expression[0])
    for i in range(1, len(expression) - 1, 1):
        if expression[i] == '+':
            result += int(expression[i + 1])
        elif expression[i] == '*':
            result *= int(expression[i + 1])
    return str(result)

for expression in expressions:
    current_exp = [s for s in expression if s != ' '] # Removing spaces and separating brakets from numbers
    
    still_work_to_do = True
    while still_work_to_do:
        still_work_to_do = False
        next_exp = list()
        i = 0
        
        while i < len(current_exp):
            # Finds an open bracket, mark it as the last open bracket founded
            if current_exp[i] == '(':
                open_brk = i
                next_exp.append(current_exp[i])
                last_brk = len(next_exp) - 1
                i += 1

            # Finds a close bracket and we still have an open bracket. Means that we have to
            # calculate what is inside the brackets (Modify the function with respect to part 1 or 2)
            elif current_exp[i] == ')' and open_brk is not None:
                del next_exp[last_brk:]
                next_exp.append(brackets_result_2(current_exp[open_brk + 1: i]))
                open_brk = None
                i = close_brk + 1

            # Finds a close bracket, but we dont have any open bracket. 
            elif current_exp[i] == ')' and open_brk is None:
                next_exp.append(current_exp[i])
                still_work_to_do = True
                i += 1
            else:
                next_exp.append(current_exp[i])
                i += 1
        current_exp = next_exp
    final_result += int(brackets_result_2(current_exp))



            
