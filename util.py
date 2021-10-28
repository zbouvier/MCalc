BASE = 37.5
KEYSTONE_LEVEL = 7.5
AFFIX_LEVEL = 7.5
SEASONAL_AFFIX_LEVEL = 15
KEYS = {
    "DOS": 43,
    "HOA": 32,
    "MOTS": 30,
    "PF": 38,
    "SD": 41,
    "SOA": 35,
    "NW": 36,
    "TOP": 38
}

def calcScore(level):
    print(level)
    bonus_score = 0
    if level >= 10:
        bonus_score = AFFIX_LEVEL*3+SEASONAL_AFFIX_LEVEL
    elif level >= 7:
        bonus_score = AFFIX_LEVEL*3
    elif level >= 4:
        bonus_score = AFFIX_LEVEL*2
    score = BASE + KEYSTONE_LEVEL*level + bonus_score
    return (score-15, score+7, score, score*0.34)