inp: str = open('2022/inputs/d4.txt').read()
pairs = [(a.split('-'), b.split('-')) for a, b in (i.split(',') for i in inp.split('\n'))]

# Part 1

print(sum(
    (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]))
    or (int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1]))
    for a, b in pairs
))

# Part 2

print(sum(
    (int(a[1]) >= int(b[0]) and int(a[0]) <= int(b[1]))
    for a, b in pairs
))
