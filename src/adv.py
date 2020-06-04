from room import Room
from player import Player

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
    



