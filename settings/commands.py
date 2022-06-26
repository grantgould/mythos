from mythos.lib.commands import Command 

class Help(Command):
    name = "help"

    def run(self, _):
       return "".join(command.__doc__ for command in self.application.commands.values())


class Explore(Command):
    name = "explore"

    def run(self, _):
        return "Exploring"

class Attack(Command):
    name = "attack"

    def run(self, args):
        if len(self.application.players) == 0:
            return "No players to attack"
        
        try:
            player = [player for player in self.application.players if player.name == args[0]]
            player[0].health -= 10

            if player[0].health <= 0:
                self.application.players.remove(player[0])
                return f"{player[0].name} has been killed"
        except:
            return "Invalid player"

        return "Attacking"
