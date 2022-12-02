shape_scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

outcome_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

round_outcomes = {
    'A': {
        'X': 'C',
        'Y': 'A',
        'Z': 'B',
    },
    'B': {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    },
    'C': {
        'X': 'B',
        'Y': 'C',
        'Z': 'A',
    }
}

tourney = None
with open('input.txt', 'r') as f:
    tourney = f.read().splitlines()

my_score = 0

def calc_score(they_play, outcome):
    round_score = shape_scores[round_outcomes[they_play][outcome]]
    round_score += outcome_scores[outcome]

    return round_score


for round in tourney:
    moves = round.split()
    my_score += calc_score(moves[0], moves[1])

print(my_score)

# Answers
# 15376 - too high
# 14859 - just right
