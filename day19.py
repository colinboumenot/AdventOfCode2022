from collections import deque
import re

def dfs(blueprint, maxspend, cache, time, bots, amount):
    if time == 0:
        return amount[3]

    key = tuple([time, *bots, *amount])
    if key in cache:
        return cache[key]

    maxval = amount[3] + bots[3] * time

    for bot, recipe in enumerate(blueprint):
        if bot != 3 and bots[bot] >= maxspend[bot]:
            continue
        wait = 0
        for resource, type in recipe:
            if bots[type] == 0:
                break
            wait = max(wait, -(-(resource - amount[type]) // bots[type]))
        else:
            time_remaining = time - wait - 1
            if time_remaining <= 0:
                continue
            bots_ = bots[:]
            amount_ = [x + y * (wait + 1) for x, y in zip(amount, bots)]
            for resource, type in recipe:
                amount_[type] -= resource
            bots_[bot] += 1
            for i in range(3):
                amount_[i] = min(amount_[i], maxspend[i] * time_remaining)
            maxval = max(maxval, dfs(blueprint, maxspend, cache, time_remaining, bots_, amount_))
    cache[key] = maxval
    return maxval


total = 0
for i, line in enumerate(open('inputtxt/day19input.txt', 'r')):
    blueprint = []
    maxspend = [0,0,0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x,y))
            maxspend[y] = max(maxspend[y], x)
        blueprint.append(recipe)
    value = dfs(blueprint, maxspend, {}, 24, [1,0,0,0], [0,0,0,0])
    total += (i + 1) * value
print(total)

total = 1
for line in (list(open('inputtxt/day19input.txt', 'r')))[:3]:
    blueprint = []
    maxspend = [0,0,0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x,y))
            maxspend[y] = max(maxspend[y], x)
        blueprint.append(recipe)
    value = dfs(blueprint, maxspend, {}, 32, [1,0,0,0], [0,0,0,0])
    total *= value
print(total)
