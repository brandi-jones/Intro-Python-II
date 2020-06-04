from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Fill rooms with items
room['outside'].items = [Item("flower", "a flower to pick from the ground"), Item("sword", "a dull broadsword")]
room['foyer'].items = [Item("knife", "a small pocket knife"), Item("banana", "an overripe banana")]
room['overlook'].items = [Item("parachute", "an unopened parachute")]
room['narrow'].items = [Item("water bottle", "a half empty water bottle")]
room['treasure'].items = [Item("a boot", "a lost boot")]

#
# Main
#
name = None
while not name:
    name = input("Welcome! What is your name? ")

gameOver = False

# Make a new player object that is currently in the 'outside' room.
player1 = Player(name, 'outside')


# Write a loop that:
while not gameOver: 

    # * Prints the current room name
    print("You are currently located in room: ", player1.location)

    # * Prints the current description (the textwrap module might be useful here).
    print(room[player1.location].description, "\n")

    # Print out all items available in current room
    print("items available to pickup from this room: ")
    for item in room[player1.location].items:
        print("- ", item.name, '\n')

    #ask if player wants to interact with items in room/inventory
    updateInventory = True
    while updateInventory:
        actionChosen = input("What would you like to do? (ex --> 'take flower', 'drop knife') or press 'c' to continue: ")
        actionChosen = actionChosen.split(" ")

        #stopping condition, user wants to continue to move directions
        if actionChosen[0] == 'c':
            updateInventory = False
        #if user attempts to take item from current room
        elif actionChosen[0] == "take" or actionChosen[0] == 'get':
            if actionChosen[1] in room[player1.location].items:
                #add item to player inventory

                #remove item from room items list
            else:
                print("That item does not exist in this room.")
        elif actionChosen[0] == "drop":
            if actionChosen[1] in room[player1.location].items:
                #remove item from player inventory

                #add item to current room items list
            else:
                print("That item does not exist in this room.")


       
            
            


    # * Waits for user input and decides what to do.
    validDirection = False
    while not validDirection:

        directionToMove = input("What direction would you like to move? \n\nPlease enter n, s, e or w (or press q to quit): ")

        # If the user enters "q", quit the game.
        if directionToMove == "q":
            gameOver = True
            validDirection = True
        #If the user enters a direction other than n, s, e, or w print an error
        elif directionToMove != "n" and directionToMove != "s" and directionToMove != "e" and directionToMove != "w":
            print("That is not a valid direction! please enter n, s, e, or w to move directions.")
        else:
            validDirection = True

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    
    def findNewLocation(nextRoom):
        for key, value in room.items():
            if value == nextRoom:
                return key #which is the new location to move to here

    if directionToMove == "n":
        if room[player1.location].n_to == None:
            print("There is no room available to move to in that direction\n")
        else: 
            player1.location = findNewLocation(room[player1.location].n_to)
    elif directionToMove == "s":
        if room[player1.location].s_to == None:
            print("There is no room available to move to in that direction\n")
        else: 
            player1.location = findNewLocation(room[player1.location].s_to)
    elif directionToMove == "e":
        if room[player1.location].e_to == None:
            print("There is no room available to move to in that direction\n")
        else: 
            player1.location = findNewLocation(room[player1.location].e_to)
    elif directionToMove == "w":
        if room[player1.location].w_to == None:
            print("There is no room available to move to in that direction\n")
        else: 
            player1.location = findNewLocation(room[player1.location].w_to)
    



