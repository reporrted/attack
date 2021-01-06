import random


playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 0:
        playerhp = 0

    print("Enemy Strikes for", dmg, "points of damage. Current HP is", playerhp)
