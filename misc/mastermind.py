from collections import Counter

def estimate(guess, solution):
    
    pseudohits = 0
    hits = 0

    solution_counter = Counter(solution)
    guess_counter = Counter(guess)
    for guess_char in guess_counter:
        pseudohits += min(guess_counter[guess_char], solution_counter[guess_char])

    solution = ''.join(solution).upper()
    for a, b in zip(guess, solution):
        if a == b:
            hits += 1
            pseudohits -= 1

    return (hits, pseudohits)

print estimate('AABB', 'ABCD')
print estimate('AABD', 'AAAD')
