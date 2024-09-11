from collections import deque
def freq(size: int) -> dict:
    '''
    Returns the frequency of additions for an enchantment tree.
    '''
    hmp = {}
    for i in range(1,size):
        count = 0
        n = i
        while n > 0:
            n = n&(n-1)
            count += 1
        if not count in hmp:
            hmp[count] = 0
        hmp[count] += 1
    return hmp

def pens(n):
    arr = [0]*n
    q = deque(arr)
    ans = 0
    while len(q) > 1:
        # pop first 2 elements
        x,y = q.popleft(), q.popleft()

        pwp = 2**(max(x,y)) - 1
        if x == y:
            ans += 2*pwp
        elif x < y:
            q.appendleft(max(x,y))
            q.append(min(x,y))
            continue
        else:
            o_pwp = 2**min(x,y) - 1
            ans += pwp + o_pwp
        q.append(max(x,y)+1)

    return ans