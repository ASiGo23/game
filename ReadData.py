import json
from GameObj import *
from Weapon import *

def ReadMap(Map):
    game_objects = []
    levelData = json.load(open('levelData.json'))
    for i in levelData[Map]["environment_objects"]:
        game_objects.append(platforms(i["rect"]))
    for i in levelData[Map]["enemy_players"]:
        buffer_character = PhysicsCharacter(
            pWeapon = Weapon(
                isAuto      = i["weapon"]["isAuto"],
                fireRate    = i["weapon"]["fireRate"],
                damage      = i["weapon"]["damage"],
                speed       = i["weapon"]["speed"],
                size        = i["weapon"]["size"],
                range       = i["weapon"]["range"],
                tracerColor = i["weapon"]["tracerColor"]
            )
        )
        buffer_character.team = 2
        game_objects.append(buffer_character)
    return game_objects

def ReadSave():
    squad = []
    saveData = json.load(open('saveData.json'))
    for i,object in enumerate(saveData["squad"]):
        buffer_character = PhysicsCharacter(
            pWeapon = Weapon(
                isAuto      = saveData["squad"][i]["weapon"]["isAuto"],
                fireRate    = saveData["squad"][i]["weapon"]["fireRate"],
                damage      = saveData["squad"][i]["weapon"]["damage"],
                speed       = saveData["squad"][i]["weapon"]["speed"],
                size        = saveData["squad"][i]["weapon"]["size"],
                range       = saveData["squad"][i]["weapon"]["range"],
                tracerColor = saveData["squad"][i]["weapon"]["tracerColor"]
            )
        )
        buffer_character.team = 1
        squad.append(buffer_character)
    return squad