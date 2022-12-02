from typing import Optional, Tuple

inp: str = open('2022/inputs/d2.txt').read()
rounds = [i.split() for i in inp.split('\n')]

moves = {'X': 1, 'Y': 2, 'Z': 3,}
outcome = {True: 6, None: 3, False: 0,}

# Part 1

def get_outcome(opp: str, me: str) -> Optional[bool]:
    if 'ABC'.index(opp) == 'XYZ'.index(me): 
        status = None
    elif ('ABC'.index(opp) + 1) == 'XYZ'.index(me) or ((opp, me) == ('C', 'X')):
        status = True
    elif ('ABC'.index(opp) - 1) == 'XYZ'.index(me) or ((opp, me) == ('A', 'Z')):
        status = False
    return status  # type: ignore

print(sum((moves.get(me) + outcome.get(get_outcome(opp, me))) for opp, me in rounds))

# Part 2

wins = {'A': 'Y', 'B': 'Z', 'C': 'X',}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y',}

def get_move(opp: str, end: str) -> Tuple[str, Optional[bool]]:  # type: ignore
    result = {'X': False, 'Y': None, 'Z': True}
    end: Optional[bool] = result.get(end)

    if end is None:  # draw
        move = list(moves.keys())['ABC'.index(opp)]
    elif end is True:  # win
        move = wins[opp]
    elif end is False:  # lose
        move = lose[opp]
    return (move, end)

print(sum((moves.get(get_move(opp, end)[0]) + outcome.get(get_move(opp, end)[1])) for opp, end in rounds))
