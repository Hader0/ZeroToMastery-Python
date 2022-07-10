dictionaryList = [
  {
    'age': [21,22,23,24,25],
    'greeting': "Good morning!",
    'temperature': 16.2
}, {
    'car': 'ford',
    'carStatus': 'broken',
    'repairable': 'no',
    ('damage'): ['headlight','bumper']
}
]


dictionaryList[1]['car'] = dictionaryList[1]['car'].capitalize()

print(f"Your {dictionaryList[1]['car']} is {dictionaryList[1]['carStatus']} and cannot be repaired")

print(dictionaryList[1][('damage')])