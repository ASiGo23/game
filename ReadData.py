import json
from GameObj import *
from Weapon import *

def ReadMap(Map):
    gameObjects = []
    levelData = json.load(open('levelData.json'))
    for i in levelData[Map]:
        gameObjects.append(platforms(i["rect"]))
    return gameObjects

def ReadSave():
    squad = []
    saveData = json.load(open('saveData.json'))
    for i in saveData["squad"]:
        squad.append(PhysicsCharacter())
    return squad