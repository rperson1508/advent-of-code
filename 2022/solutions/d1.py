inp: str = open('2022/inputs/d1.txt').read()

elfs = [i.strip() for i in inp.split('\n\n')]
cals = sorted([sum(int(i) for i in e.split('\n')) for e in elfs])

# Part 1
print(cals[-1])

# Part 2
print(cals[-1] + cals[-2] + cals[-3])
