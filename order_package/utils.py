from collections import deque



def level(size: int) -> int:
    '''
    Returns the sum of penalties for a level enchantment tree.\n
    Size represents the number of books the user desires, 
    so do not include the base item in the count.
    '''
    arr = [(0,x-1) if x > 0 else (0,-1) for x in range(size+1)]
    # arr[0]
    order = []
    q = deque(arr)
    ans = 0
    while len(q) > 1:
        if ans == 10:
            pass
        # pop first 2 elements
        left,right = q.popleft(), q.popleft()
        x,y = left[0], right[0]

        pwp = 2**(max(x,y)) - 1
        if x == y:
            ans += 2*pwp
        elif x < y:
            q.appendleft(max(left,right))
            q.append(min(left,right))
            continue
        else:
            o_pwp = 2**min(x,y) - 1
            ans += pwp + o_pwp
        # order = ([left[1],right[1]])
        q.append((max(x,y)+1, [left[1],right[1]]))

    return (ans, q[0][1])



def level_cost(enchants: int) -> dict:
    '''
    Returns the frequency of additions for an enchantment tree as a dictionary.
    '''
    size = len(enchants)
    hmp = {}
    # We start from 1 to avoid adding a 0 (base item gets added 0 times)
    # We loop until size + 1 to offset the base item.
    for i in range(1,size+1):
        count = 0
        
        n = i
        # Loop to count flips of 1 to 0.
        while n > 0:
            n = n&(n-1)
            count += 1
        # Avoid KeyError.
        if not count in hmp:
            hmp[count] = 0
        hmp[count] += 1
    total = 0

    i = 0 # Increment through sorted(non-increasing) enchantments
    for key, value in hmp.items():
        while value > 0: # Values represent the count of enchantments that get added key times.
            total += enchants[i] * key
            i += 1
            value -= 1 # Decrement while loop
    return total


def optimal(enchants: list[int])->tuple[int, list[int]]:
    '''
    Finds the optimal enchantment order to minimise cost. \n
    Returns (total_cost, order_of_indices)
    '''
    if not enchants:
        return (0,[])
    total = enchants[0]
    penalties = 1
    
    order = [[-1,0]] 
    l,r = 1, len(enchants) - 1
    while l <= r: 
        # If both pointers point to the same enchantment there can be no more to pair, 
        # so add with 0 penalty (no prior work for a bare book).
        if l == r:
            total += enchants[r]
            order.append(r)
        else:
            # Each pair will have the smaller (r) of the books cost twice, whereas 
            # the bigger number will only be counted once. 
            # Add one for each penalty for the combined book.
            total += ((2*enchants[r]) + enchants[l] + 1)
            order.append([r,l])

        # Only calculating the base item's penalties as the cost for the other enchants
        # are included in the addition to total
        total += (2**penalties)-1  # Anvil penalty formula from the wiki.
        penalties += 1

        # Maximum enchantment cost for one anvil use is 39. 2^5 = 32,
        # any additional enchantments are likely to tip the scale.
        if penalties > 5:
            # Return same tuple format
            return (0, [])
        l += 1
        r -= 1
    return (total, order)


