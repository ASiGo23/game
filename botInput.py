def botInput(game_instance):
    for bot in game_instance.get_bots():
        bot.calculate_move(game_instance)

class bot:
    def __init__(self,avatar):
        self.avatar = avatar
    def calculate_move(self,game_instance):
        self.avatar.moveOnX(game_instance.get_environmentObjects(),5)