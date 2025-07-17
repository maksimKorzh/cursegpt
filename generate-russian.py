import random

adjectives1 = ['ёбаный', 'ебучий']
adjectives2 = ['хуёвый', 'припездиный']
nouns1 = ['пидар', 'хуй', 'долбоёб']
nouns2 = ['уебан', 'сука', 'хуепутало', 'блядь', 'ёбаное всё']
verbs = ['ебать', 'дрочить', 'сосать',]
body_parts = ['пизда', 'жопа', 'хуйня']
places = ['на хуй', 'в пизду', 'к хуям']

templates = [
  'Ты {noun1} {adj1}, {noun2}!',
  'Иди {place}!',
  'Чтоб ты {adj1} {noun1} пошёл {place}.',
  '{verb} ты хотел {place}, {noun1} {adj1}, {noun2}.',
]

with open('input-russian.txt', 'w') as f:
    for _ in range(2000):
        template = random.choice(templates)
        curse = template.format(
            adj1=random.choice(adjectives1),
            adj2=random.choice(adjectives2),
            noun1=random.choice(nouns1),
            noun2=random.choice(nouns2),
            verb=random.choice(verbs),
            body=random.choice(body_parts),
            place=random.choice(places),
        )
        f.write(curse + '\n')
