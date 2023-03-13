def botInput(game_instance):
    from GameObj import PhysicsCharacter
    for bot in game_instance.get_type(PhysicsCharacter):
        if bot.bot.active == True:
            bot.bot.calculate_move(game_instance)

class bot:
    def __init__(self,avatar):
        self.avatar = avatar
        self.active = True
    def calculate_move(self,game_instance):
        from GameObj import platforms
        self.avatar.moveOnX(game_instance.get_type(platforms),2)
    def deactivate(self):
        self.active = False