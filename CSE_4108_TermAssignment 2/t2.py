import random
import string

def generate_random_solution(length=13):
    return [random.choice(string.printable) for _ in range(length)]

def evaluate(solution):
    target = list("Hello, World!")
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff


best = generate_random_solution()
heuristic_value = evaluate(best)

while True:
    
    print('Heuristic Value: ', heuristic_value, 'and the newly found solution', "".join(best))

    if heuristic_value == 0:
        break

    new_solution = generate_random_solution()
    
    score = evaluate(new_solution)
    
    
    if evaluate(new_solution) < heuristic_value:
        best = new_solution
        heuristic_value = score