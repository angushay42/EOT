from collections import deque



def level(size: int) -> int:
    '''
    Returns the sum of penalties for a level enchantment tree.
    '''
    arr = [(0,x-1) if x > 0 else (0,-1) for x in range(size+1)]
    # arr[0]
    order = []
    q = deque(arr)
    ans = 0
    while len(q) > 1:
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
        order = ([left[1],right[1]])
        q.append((max(x,y)+1, [left[1],right[1]]))

    return (ans,order)


def level_cost(size: int) -> dict:
    '''
    Returns the frequency of additions for an enchantment tree as a dictionary.
    '''
    hmp = {}
    for i in range(1,size + 1):
        count = 0
        n = i
        while n > 0:
            n = n&(n-1)
            count += 1
        if not count in hmp:
            hmp[count] = 0
        hmp[count] += 1
    return hmp


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
