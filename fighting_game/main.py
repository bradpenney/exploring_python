#!/usr/bin/python

import enemy

bruce = enemy.Enemy()

bruce.type_of_enemy = "Zombie"

print(
    f"{bruce.type_of_enemy} has {bruce.health_points} health points "
    + f"and can do attack damage of {bruce.attack_damage}"
)
