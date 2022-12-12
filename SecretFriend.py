import random

people = ['Ana', 'Bia', 'Cris', 'Duda', 'Eva', 'Fabi', 'Gabi', 'Helo', 'Iara', 'Jana', 'Keli', 'Lili', 'Mara', 'Nana', 'Oana', 'Pati', 'Rita', 'Sara', 'Tati', 'Uana', 'Vana', 'Wana', 'Xana', 'Yana', 'Zana']

random.shuffle(people)

for i, person in enumerate(people):
    if i == len(people) - 1:
        print(f'{person} is the secret friend of {people[0]}')
    else:
        print(f'{person} is the secret friend of {people[i + 1]}')