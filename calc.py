BASE = 37.5
KEYSTONE_LEVEL = 7.5
AFFIX_LEVEL = 7.5
SEASONAL_AFFIX_LEVEL = 15
import numpy as np
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
print('Here are your options!')
for name, _ in KEYS.items():
    print(name)

key = input("What key are you running?")


if key in KEYS:
    level = int(input("What level are you running?"))
    bonus_score = 0
    if level >= 10:
        bonus_score = AFFIX_LEVEL*3+SEASONAL_AFFIX_LEVEL
    elif level >= 7:
        bonus_score = AFFIX_LEVEL*3
    elif level >= 4:
        bonus_score = AFFIX_LEVEL*2
    score = BASE + KEYSTONE_LEVEL*level + bonus_score
    print("Your score will between: ", score-15, " and ", score+7)
    print("The score for beating it precisely on time is: ", score)
else:
    print("Please enter a valid key")