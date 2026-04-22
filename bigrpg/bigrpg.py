import random
from battlemoves import BattleMoves 
from players import Players

#define opening variables
gamestart = False
currentRoom = 'Front Doorstep'
inventory = []
bossBeaten = False
moveCount = 0 #after x moves u lose?
activeEffect = None
effectTurns = 0

#links rooms to other rooms
rooms = {
    'Front Doorstep': {
        'north': 'Main Hallway',
        'east': 'Vegetable Garden',
        'west': 'Tennis Court'
    },
    'Vegetable Garden': {
        'west': 'Front Doorstep'
    },
    'Tennis Court': {
        'east': 'Front Doorstep',
        'north': 'Pathway'
    },
    'Pathway': {
        'northeast': 'Pool',
        'south': 'Tennis Court'
    },
    'Pool': {
        'southwest': 'Pathway',
        'west': 'Spa',
        'east': 'Changing Rooms',
        'north': 'Prickly Fence',
        'south': 'Back Entrance'
    },
    'Spa': {
        'east': 'Pool'
    },
    'Changing Rooms': {
        'west': 'Pool'
    },
    'Prickly Fence': {
        'south': 'Pool'
    },
    'Main Hallway': {
        # SOUTH NOT ALLOWED COZ TROLOLOLOL
        'north': 'Living Room',
        'stairsup': 'Stairs',
        #'stairsdown': 'Dungeon', #BOSS SPOT BY DEFAULT, LOCKED?
        'east': 'Ball Room',
        'west': 'Dining Room'
    },
    'Living Room': {
        'south': 'Main Hallway',
        'north': 'Back Entrance'
    },
    'Back Entrance': {
        'south': 'Living Room',
        'north': 'Pool'
    },
    'Dining Room': {
        'east': 'Main Hallway',
        'north': 'Kitchen'
    },
    'Kitchen': {
        'south': 'Dining Room',
        'north': 'Cupboard'
    },
    'Cupboard': {
        'south': 'Kitchen'
    },
    'Ball Room': {
        'west': 'Main Hallway'
    },
    'Stairs': {
        'down': 'Main Hallway',
        'up': 'Hallway'
    },
    'Dungeon': {
        #LOCKED FOR NOW
    },
    'Hallway': {
        'stairs': 'Stairs',
        'north': 'Master Bedroom',
        'west': 'Guest Main Room',
        'east': 'Study',
        'south': 'Balcony'
    },
    'Balcony': { #a quick escape option but less health?
        'north': 'Hallway'
    },
    'Study': {
        'west': 'Hallway'
    },
    'Guest Main Room': {
        'east': 'Hallway',
        'north': 'Guest Bathrooms',
        'west': 'Guest Room 1',
        'south': 'Guest Room 2'
    },
    'Guest Bathrooms': {
        'south': 'Guest Main Room'
    },
    'Guest Room 1': {
        'east': 'Guest Main Room'
    },
    'Guest Room 2': {
        'north': 'Guest Main Room'
    },
    'Master Bedroom': {
        'south': 'Hallway',
        'east': 'Ensuite'
    },
    'Ensuite': {
        'west': 'Master Bedroom'
    }
}

def showInstructions():

    print ('''
           no
           ''')

def showStatus():

    # print the player's current status
    print('---------------------------')
    print(player1.name + ' is in the ' + currentRoom)
    # print the current inventory
    print("Health:" + str(player1.getHealth()))
    print("Inventory : " + str(inventory))
    if activeEffect != None:
       print('You have the ' + activeEffect + ' effect for ' + str(effectTurns) + ' turns')
    if 'hostile' in rooms[currentRoom] and activeEffect != "Invis":
        battle(hostiles[rooms[currentRoom]['hostile']])
    elif 'hostile' in rooms[currentRoom] and activeEffect == "Invis":
        print("The hostile didn't see you due to your invisiblity.")
    # print an item if there is one
    if "item" in rooms[currentRoom] and not "hostile" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if not "hostile" in rooms[currentRoom]:
        findPossibleRoutes()
    print("---------------------------")

def findPossibleRoutes():
    possiblerooms = []
    directions = []
    for room in list(rooms[currentRoom].items()):
        w = str(room) # one string here
        w = w.split(',') # makes it two so that it can be split
        direction = w[0].strip("('")  # Remove leading "('"
        room_name = w[1].strip(" ')")  # Remove leading " '" and trailing "')"
        if direction != 'item' and direction != 'hostile':
            directions.append(direction)
            possiblerooms.append(room_name)
    print('Possible Rooms:')
    for x in range(0,len(directions)):
        print('Go ' + directions[x] + ' to find the ' + possiblerooms[x])

#weapons/items add moves
battlemoves = { 
        'Punch' : BattleMoves('Punch',1,20,85,"a",1),
        'Kick': BattleMoves('Kick',5,20,70,"b",1),
        'Tackle': BattleMoves('Tackle',10,25,60,"c",1)
            }
hostilemoves = {
        'Punch' : BattleMoves('Punch',1,10,75,"a",1),
        'Kick': BattleMoves('Kick',5,17,70,"b",1),
        'Tackle': BattleMoves('Tackle',10,20,50,"c",1),
        'Big Punch': BattleMoves('Big Punch',5,20,70,"d",2),
        'Whack': BattleMoves('Whack',10,15,75,"e",2),
        'Spike Kick': BattleMoves('Spike Kick',15,25,60,"f",2),
        'Slash': BattleMoves('Slash',10,20,80,"g",3),
        'Hammer': BattleMoves('Hammer',20,40,50,"h",3),
        'Stab': BattleMoves('Stab',1,50,70,"i",3)
}

#generate items into random rooms. includes some hostile people. 
#future have many hostiles and weapons and rotate them in? like only 3-4 hostiles every run
#future make dungeon not only boss room?
items = ['Health Potion','Rusty Dagger']
weapons = []
hostiles = {
    'Evil Droid': Players('Evil Droid',1,50),
    'Goblin': Players('Goblin',1,30),
    'Crow': Players('Crow',2,60),
    'Ghost': Players('Ghost',2,49)
    }
noHostileOrItemRooms = ['Main Hallway','Dungeon','Front Doorstep']

def generateRandomLocations():
    for item in items:
        while True:
            roomName = random.choice(list(rooms.keys()))
            if 'item' not in rooms[roomName] and roomName not in noHostileOrItemRooms:
                rooms[roomName]['item'] = item
                break
    for hostile in hostiles:
        while True:
            roomName = random.choice(list(rooms.keys()))
            if 'hostile' not in rooms[roomName] and roomName not in noHostileOrItemRooms and 'item' not in rooms[roomName]:
                rooms[roomName]['hostile'] = hostile
                break

def printMoves():
    a = 1
    for m in battlemoves:
        print(str(a) + ") Move Name: " + battlemoves[m].getName(), " Description: " + battlemoves[m].getDescription())
        a = a+1

def battle(hostile):
    print("Battle against " + hostile.getName())

    print("Your Health: " + str(player1.getHealth()))
    print(hostile.getName() + " Health: " + str(hostile.getHealth()))

    fight_turn = 1
    while hostile.getHealth() > 0 and player1.getHealth() > 0:
        #PLAYER TURN
        printMoves()
        while True:
            try:
                moveid = int(input("Select the number of your move: "))
                if 1 <= moveid <= len(battlemoves):
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a number.")

        min = list(battlemoves.values())[moveid-1].getLowDamage()
        max = list(battlemoves.values())[moveid-1].getHighDamage()
        damage = random.randint(min,max)
        accurate = random.randint(1,100)
        if accurate > list(battlemoves.values())[moveid-1].getAccuracy():
            print("Your attack missed!")
        else:
            hostile.adjustHealth(damage,False)
            print("You used " + list(battlemoves.values())[moveid-1].getName() + " to do " + str(damage) + " damage!")
        print("Hostile turn")
        #HOSTILE TURN

        possibleMoves = [move for move in hostilemoves.values() if move.level <= hostile.getLevel()]
        hostilemove = random.choice(possibleMoves)
        min = hostilemove.getLowDamage()
        max = hostilemove.getHighDamage()
        damage = random.randint(min,max)
        accurate = random.randint(1,100)
        
        if accurate > hostilemove.getAccuracy():
            print("Their attack missed!")
        else:
            player1.adjustHealth(damage,False)
            print("They used " + hostilemove.getName() + " to do " + str(damage) + " damage!")

        if player1.getHealth() < 1:
            loseGame()
        elif hostile.getHealth() < 1:
            print("The " + hostile.getName() + " has been defeated!")
            del rooms[currentRoom]['hostile']
            gainReward()
            showStatus()
            return
        else:
            print("Your Health: " + str(player1.getHealth()))
            print("Their Health: " + str(hostile.getHealth()))

def gainReward():
    pick = random.randint(3,3)
    if pick == 1:
        heal = random.randint(10,40)
        print("You have healed for " + str(heal))
        player1.adjustHealth(heal,True)
    elif pick == 2:
        if 'Bow' not in battlemoves:
            print("You have gained the special bow to use in battle!")
            battlemoves.update({'Bow' : BattleMoves('Bow',10,35,70,"bow",3)})
        elif 'Scythe' not in battlemoves:
            print("You have gained the special scythe to use in battle!")
            battlemoves.update({'Scythe' : BattleMoves('Scythe',15,45,57,"scythe",3)})
    elif pick == 3:
        print("You have gained invisibility for 3 turns! Hostiles will not attack you, but you cannot fight them.")
        global activeEffect,effectTurns
        activeEffect = "Invis"
        effectTurns = 4


def loseGame():
    print("LOLOL U LOSE")
    quit()

if gamestart == False:
    name = input("What is your name?")
    player1 = Players(name,1)
    generateRandomLocations()
    showInstructions()
    print(rooms) #debug only

while not bossBeaten:
    print('Move '+ str(moveCount))
    if effectTurns > 0:
        effectTurns -= 1
    if effectTurns == 0:
        activeEffect = None
    showStatus()
        #moveCount+=1
        #continue

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #FIRST CHECK IF HOSTILE IS IN ROOM. IF SO, FIGHT.

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            moveCount+=1
        else:
            print('You can\'t go that way!')
    elif move[0] == 'get':
        item_name = ' '.join(move[1:])
        if 'item' in rooms[currentRoom] and item_name.lower() == rooms[currentRoom]['item'].lower():
            inventory.append(rooms[currentRoom]['item'])
            print("Got " + rooms[currentRoom]['item'])
            del rooms[currentRoom]['item']
            moveCount+=1
        else:
            print("Cannot get item.")
    elif move[0] == 'use':
        if inventory.count == 0:
            print('You have no items to use.')
        else:
            item_to_use = ' '.join(move[1:]).lower()
            if item_to_use == "health potion":
                player1.adjustHealth(50,True)
            elif item_to_use == "rusty dagger":
                print("Dagger added to move list.")
                battlemoves.update({'Rusty Dagger': BattleMoves('Rusty Dagger',10,20,80,"a",2)})
            moveCount+=1
    else:
        print('bozo')
    
