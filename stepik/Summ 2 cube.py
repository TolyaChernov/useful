# Cумма двух кубов двумя разными способами
n = 50
se = []
for a in range(1, n):
    for b in range(1, n):
        for c in range(n, 0, -1):
            for d in range(n, 0, -1):
                if a != b and a != c and a != d and b != c and b != d and c != d and a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    sum = a ** 3 + b ** 3
                    if sum not in se:
                        se.append(sum)
print(sorted(se))
