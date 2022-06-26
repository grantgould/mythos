from mythos.lib.commands import *
from mythos.lib.core import Prompt
from settings.commands import * 

class Open(Command):
    name = "open"

    def run(self, args):
        return "Opening {}".format(args)

class Purse:
    def __init__(self):
        self.gold = 0
    
    def deposit(self, amount):
        self.gold += amount

    def withdraw(self, amount):
        self.gold -= amount

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.purse = Purse()

    def __str__(self):
        return f"{self.name}: health={self.health} gold={self.purse.gold}\n"

class NonPlayableCharacter(Player):
    pass

class PlayersCommand(Command):
    name = "players"

    def run(self, _):
        return "Players:\n" + "\n".join(map(str, self.application.players))

class Join(Command):
    name = "join"

    def run(self, args):
        self.application.players.append(Player(args[0]))

        return "Joining {}".format(args)

class Stats(Command):
    name = "stats"

    def run(self, _):
        return "".join([str(player) for player in self.application.players])

class Spawn(Command):
    name = "spawn"

    def run(self, args):
        self.application.players.append(NonPlayableCharacter(args[0]))

class Kill(Command):
    name = "kill"

    def run(self, args):
        self.application.players.remove(Player(args[0]))

class Heal(Command):
    name = "heal"

    def run(self, args):
        try:
            player = [player for player in self.application.players if player.name == args[0]]
            player[0].health += 100
        except:
            return "Invalid player"

        return "Healing"

class Mine(Command):
    name = "mine"

    def run(self, args):

        if args[0] in "=":
            return "Invalid command"

        return "Healing"
    

class Application:
    running = False
    commands = { }
    players = [ ]

    def register(self, command):
        self.commands[command.name] = command

    def run(self):
        self.running = True

        while self.running:
            prompt = Prompt()

            if prompt.command in self.commands.keys():
                print(self.commands[prompt.command](self).run(prompt.arguments))
                continue 

            if prompt.command == "":
                print("Please enter a command")
                continue

            print(f"Command '{prompt.command}' not found")

    def quit(self):
        self.running = False

class CustomCommand(Command):
    name = "custom"

    def run(self, _):
        lines = ""
        keys = sorted(self.application.commands.keys())

        for key in keys:
            lines += f"{key} - {self.application.commands[key].__doc__}\n"

        return lines

app = Application()


app.register(PlayersCommand)
app.register(CustomCommand)
app.register(Help)
app.register(Quit)
app.register(Explore)
app.register(Attack)
app.register(Open)
app.register(Exit)
app.register(QuitShortCut)
app.register(ExitShortCut)
app.register(Join)
app.register(Stats)
app.register(Spawn)
app.register(Heal)
app.register(Mine)

app.run()