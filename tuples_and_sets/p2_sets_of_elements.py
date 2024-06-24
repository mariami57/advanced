n, m = input().split()

n_set = {input() for _ in range(int(n))}
m_set = {input() for _ in range(int(m))}
both_sets_intersection = n_set.intersection(m_set)

print(*both_sets_intersection, sep="\n")