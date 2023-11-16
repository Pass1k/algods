vote = {
    'Pasik': True
}

def vote_cheacker(name):
    if vote.get(name):
        print('Kick him out')
    else:
        vote[name] = True
        print('let them vote')

vote_cheacker('Paparize')
vote_cheacker('Pasik')
vote_cheacker('Azamat')

print()
for kay, value in vote.items():
    print(kay, value)
