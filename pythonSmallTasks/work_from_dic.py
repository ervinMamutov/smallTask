elect_table = {}
def elect(m, n):
    if (m, n) in elect_table:
        return elect_table[(m, n)]
    else:
        for m in 5:
            for n in 5:

