from string import ascii_letters as priorities

inp: str = open('2022/inputs/d3.txt').read()
rucksacks = inp.split('\n')

def get_priority(char: str) -> int:
    return priorities.index(char) + 1

def half(text: str, *, reverse: bool = False) -> str:
    res = len(text) // 2
    return text[:res] if not reverse else text[res:]

# Part 1
print(sum(
    get_priority(
        list(set(half(r)) & set(half(r, reverse=True)))[0]
    ) for r in rucksacks
))

# Part 2
print(sum(
    get_priority(
        list(set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2]))[0]
    ) for i in range(0, len(rucksacks) - 2, 3)
))
