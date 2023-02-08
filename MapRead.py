import json
from GameObj import *
from Weapon import *

def ReadMap(Map):
    gameObjects = []
    levelData = json.load(open('levelData.json'))
    for i in levelData[Map]:
        if (i["type"] == "Platform"):
            gameObjects.append(platforms(i["rect"]))
        else:
            gameObjects.append(PhysicsCharacter())
    return gameObjects