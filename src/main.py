import itertools

members = [
    'josh',
    'mei',
    'matt',
    'heather',
    'frankie'
]

items = list(itertools.combinations(members, 2))
items = list(itertools.combinations(range(1, 31), 2))


print(len(items))
