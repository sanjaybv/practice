def game(coins, i, j, cache):
    if i >= len(coins) or j < 0 or i > j:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]

    option_1 = coins[i] + min(
            game(coins, i+2, j, cache),
            game(coins, i+1, j-1, cache))
    option_2 = coins[j] + min(
            game(coins, i, j-2, cache),
            game(coins, i+1, j-1, cache))
    result = max(option_1, option_2)
    
    cache[i][j] = result
    return result


cache = [[-1]*4 for _ in xrange(4)]
print game([8, 15, 3, 7], 0, 3, cache)            
