from collections import deque



def level_cost(vals: list[int]) -> dict:
    '''
    Returns the cost of a level-order list of enchantments, excluding the sum of penalties
    (decremented)
    Returns the frequency of additions for an enchantment tree as a dictionary.
    '''
    size = len(vals)
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
            total += vals[i] * key
            i += 1
            value -= 1 # Decrement while loop
    return total

def level(size: int) -> int:
    '''
    Returns the sum of penalties for a level enchantment tree.\n
    Returns (total_cost, order_of_indices)
    '''
    arr = [(0,x-1) if x > 0 else (0,-1) for x in range(size+1)]
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
        q.append((max(x,y)+1, [left[1],right[1]]))

    return (ans, q[0][1])


def optimal(vals: list[int])-> tuple[int, list[int]]:
    '''
    Finds the optimal enchantment order to minimise cost. \n
    Returns (total_cost, order_of_indices)
    '''
    if not vals:
        return (0,[])
    total = vals[0]
    penalties = 1
    
    order = [0] 
    l,r = 1, len(vals) - 1
    while l <= r: 
        # If both pointers point to the same enchantment there can be no more to pair, 
        # so add with 0 penalty (no prior work for a bare book).
        if l == r:
            total += vals[r]
            order.append(r)
        else:
            # Each pair will have the smaller (r) of the books cost twice, whereas 
            # the bigger number will only be counted once. 
            # Add one for each penalty for the combined book.
            total += ((2*vals[r]) + vals[l] + 1)
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


def display_level(order: list[list, int], e: list) -> None:
    def helper(order):
        if type(order) == int:
            return order
        l = helper(order[0])
        r = helper(order[1])
        if l == -1:
            print("Add {} to item".format(e[r]))
            return l
        else:
            print("Add {} to {}".format(e[r],e[l]))
            e[l] = "{}, {}".format(e[l],e[r])
            return l
    helper(order)
    

def display_optimal(order: list[list, int], e: list[int]) -> None:
    order.reverse()
    st = order[::]
    while st:
        item = st.pop()
        if type(item) == list:
            l,r = item
            print("Add {} to {}".format(e[r],e[l]))
            e[l] = "{}, {}".format(e[l],e[r])
            st.append(l)
        else:
            print("Add {} to item".format(e[item]))
