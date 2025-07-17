import random

adjectives1 = ['fucking', 'dodgy', 'silly']
adjectives2 = ['shitty', 'bloody']
nouns = ['fuck', 'dick', 'knobhead', 'wanker', 'moron', 'blimey']
verbs = ['fuck', 'shit', 'piss',]
body_parts = ['cunt', 'arse', 'bollocks']
places = ['hell', 'arsewhole']

templates = [
  'You {adj1} {noun}!',
  'You are such a {noun}...',
  'You\'re as {adj1} as a {noun} in a {adj2} {place}.',
  'I am {verb}ed as {noun}!',
  'You {verb} like a {adj1} {body}.',
  'I\'ve seen {noun}s with more charm than your {body}.',
  'May a {adj1} {noun} haunt your dreams.',
]

with open('input.txt', 'w') as f:
    for _ in range(2000):
        template = random.choice(templates)
        curse = template.format(
            adj1=random.choice(adjectives1),
            adj2=random.choice(adjectives2),
            noun=random.choice(nouns),
            verb=random.choice(verbs),
            body=random.choice(body_parts),
            place=random.choice(places),
        )
        f.write(curse + '\n')
