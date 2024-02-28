#!/bin/python3
import random

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key to win!
The monster could be anywhere, and will kill you.
The goblin will try steal any items you have.
The sword will protect you from any evil, and the potion could be good or bad.

Commands:
  go [direction] moves you north, south, east or west to another location.
  get [item] will get the item in the room, if there is one.
  use [item] will use the item, if it is usable.
''')

def showStatus():
    # print the player's current status
    print('---------------------------')
    print(name + ' is in the ' + currentRoom)
    # print the current inventory
    print("Inventory : " + str(inventory))
    if effectTurns > 0:
        print('You have the ' + activeEffect + ' effect for ' + str(effectTurns) + ' turns')
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        
    findPossibleRoutes()
    print("---------------------------")
    
def findPossibleRoutes():
    possiblerooms = []
    directions = []
    for room in list(rooms[currentRoom].items()):
        w = str(room) # one string herea
        w = w.split(',') # makes it two so that it can be split
        direction = w[0].strip("('")  # Remove leading "('"
        room_name = w[1].strip(" ')")  # Remove leading " '" and trailing "')"
        if direction != 'item':
            directions.append(direction)
            possiblerooms.append(room_name)
    print('Possible Rooms:')
    for x in range(0,len(directions)):
        print('Go ' + directions[x] + ' to find the ' + possiblerooms[x])

# setup the game
name = None
currentRoom = 'Hall'
inventory = []
activeEffect = None
effectTurns = 0
keyLocation = ''
swordLocation = '' 

# a dictionary linking a room to other room positions
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north': 'Stairs',
        'west': 'Living Room'
    },

    'Kitchen': {
        'north': 'Hall',
        'west': 'Kitchen Cupboard'
    },
    
    'Kitchen Cupboard': {
        'east': 'Kitchen'    
    },

    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden'
    },

    'Garden': {
        'north': 'Dining Room'
    },

    'Stairs': {
        'south': 'Hall',
        'north': 'Basement'
    },

    'Basement': {
        'south': 'Stairs',
        'east': 'Basement Cupboard'
    },

    'Basement Cupboard': {
        'west': 'Basement'    
    },
    
    'Living Room': {
        'east': 'Hall',
        'north': 'Study',
        'west': 'Bedroom',
        'south': 'Bathroom'
    },
    
    'Bedroom': {
        'east': 'Living Room',
        'west': 'Ensuite'
    },
    
    'Study': {
        'south': 'Living Room'    
    },
    
    'Bathroom': {
        'north': 'Living Room'    
    },
    
    'Ensuite': {
        'east': 'Bedroom'    
    }
}

# generates the items into random rooms
items = ['key', 'potion', 'sword', 'monster', 'goblin', 'bit of dried blood']
noPickUpItems = ['monster', 'goblin', 'blood']
noItemRooms = ['Hall', 'Study','Garden']
noHostileRooms = ['Stairs', 'Living Room']
noGoblinRooms = ['Living Room']
noMonsterRooms = ['Basement']

for item in items:
    while True:
        roomName = random.choice(list(rooms.keys()))
        if 'item' not in rooms[roomName] and roomName not in noItemRooms and not (
            (item in ['monster', 'goblin'] and roomName in noHostileRooms) or 
            (item != 'monster' and roomName == 'Hall' or (item == 'goblin' and roomName in noGoblinRooms)
             or item == 'monster' and roomName in noMonsterRooms)
        ):
            rooms[roomName]['item'] = item
            if item == 'key':
                keyLocation = roomName
            elif item == 'sword':
                swordLocation = roomName
            break

# ask the player their name
if name is None:
    name = input("What is your name Adventurer? ")
    showInstructions()

# loop forever
while True:
    
    if activeEffect != None and effectTurns > 0:    
        effectTurns = effectTurns - 1
    else:
        activeEffect = ''

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into a list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            effectTurns = effectTurns + 1 # this fixes a bug
            print('You can\'t go that way!')

    # if they type 'get' first
    elif move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] == 'sword':
            print('Solve a problem to get access to the powerful sword')
            a = random.choice(range(1,20))
            b = random.choice(range(1,20))
            answer = a*b
            response = input('What is ' + str(a) + ' times ' + str(b) + '?\n')
            if response == str(answer):
                print('Sword received! You are big brain')
                inventory += [move[1]]
                del rooms[currentRoom]['item']
            else:
                print('Better luck next time... the sword has disappeared.')
                del rooms[currentRoom]['item']
        # if the room contains an item, and the item is the one they want to get
        elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] not in noPickUpItems:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    # if use
    elif move[0] == 'use':
        if 'potion' in inventory:
            effectnum = random.choice(range(1,6))
            if effectnum == 1:
                print('Shield activated for 2 movement turns')
                activeEffect = 'Shield'
                effectTurns = 3 #bc it depreciates at start of turn - set it to one more
            elif effectnum == 2:
                print('The potion was a dud. Nothing happened, except the exquisite taste of pineapple and syrup.')
            elif effectnum == 3:
                print('Shield activated for 3 movement turns')
                activeEffect = 'Shield'
                effectTurns = 4
            elif effectnum == 4:
                if len(inventory) > 0:
                    stolenItem = random.choice(inventory)
                    inventory.remove(stolenItem)
                    print('Uh oh! You dropped one of your items and it is gone, if you are lucky enough to have one...')
                else:
                    print('You had nothing to even drop. Pathetic.')
            elif effectnum == 5:
                print('The potion has revealed the key is in this location: ' + keyLocation )
            else:
                print('The potion has revealed the sword is in this location' + swordLocation)
            if 'potion'in inventory:
                inventory.remove('potion')
        else:
            print('No usable items')
            
    else:
        print('Invalid command')

    # player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'sword' not in inventory and activeEffect != 'Shield':
        print('A monster has got you... GAME OVER!')
        break
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'sword' not in inventory and activeEffect == 'Shield':
        print('You would have died.. but the shield protected you. I advise you run.')
    elif 'item' in rooms[currentRoom] and 'goblin' in rooms[currentRoom]['item'] and 'sword' not in inventory:
        if len(inventory) > 0:
            stolenItem = random.choice(inventory)
            inventory.remove(stolenItem)
            print('One of your items have been stolen.. go to the study to get it back.')
            rooms['Study']['item'] = stolenItem
        else:
            print("The goblin couldn't steal anything.. this time")
        
        
    elif 'sword' in inventory and 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You have slain the monster!')
        del rooms[currentRoom]['item']
    elif 'sword' in inventory and 'item' in rooms[currentRoom] and 'goblin' in rooms[currentRoom]['item']:
        print('You have slain the goblin!')
        del rooms[currentRoom]['item']    

    # player wins if they get to the garden with a key
    if currentRoom == 'Garden' and 'key' in inventory:
        print('You escaped the house... YOU WIN!')
        break
