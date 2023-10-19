from applemusicpy import AppleMusic
from __init__ import init as am

def get(id):
    x = am('https://api.music.apple.com/v1/catalog/us/songs/{id}')

    return x

print(get(1613600188))