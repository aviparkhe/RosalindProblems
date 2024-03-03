from functools import reduce

def mortal_rabbits(n, m):
    # set up population dict
    p = {1: 1}  # {1: _, 2: _, 3: _, ... m: _} the numbers are the stages (1 - baby, 2 - mature1, 3 - mature2 ...)
    for i in range(2, m + 1):
        p[i] = 0

    for gen in range(2, n + 1):
        p2 = {}

        # move everyone up 1 stage
        for i in range(1, m):
            p2[i + 1] = p[i]
        p2[1] = 0
        for j in p:
            if j != 1:
                p2[1] += p[j]

        p = p2

    sum = reduce(lambda x, y: x + y, p.values())
    print(sum)

n, m = 82, 20
mortal_rabbits(n, m)


def mendel(x, y, z):  # returns prob of offspring having dominant allele (x --> homo-d, y --> hetero, z --> homo-r)
    total = x + y + z
    two_recess = (z / total) * ((z - 1) / (total - 1))
    two_hetero = (y / total) * ((y - 1) / (total - 1))
    hetero_recess = (z / total) * (y / (total - 1)) + (y / total) * (z / (total - 1))

    recess_prob = two_recess + two_hetero * 0.25 + hetero_recess * 0.5
    return 1 - recess_prob  # complement

