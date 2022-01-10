import random
class Knight:
    def __init__(self, name, lifepoint):
        self.name = name
        self.lifepoint = lifepoint
        self.next = None
    
class Game:
    def play(self):
        knights = []
        for i in range(6):
            knights.append(Knight("K"+str(i+1), 10))

        for i in range(6):
            knights[i].next = knights[(i+1)%6]

        # Player    
        player = knights[0]

        while player.next != player:
            next_player = player.next
            hit = random.randrange(1,6)
            print("{} hits {} for {}".format(player.name, next_player.name, hit))
            
            # Game
            next_player.lifepoint -= hit
            if next_player.lifepoint <= 0:
                player.next = next_player.next
                print(next_player.name + "dies")

            player = player.next
        print(player.name + "Wins")

game = Game()
game.play()
