from applemusicpy import AppleMusic

secret_key = 'x'
key_id = 'y'
team_id = 'z'

def apple_get(id):
    x = get('https://api.music.apple.com/v1/catalog/us/songs/{id}')

    return x

print(apple_get(1613600188))