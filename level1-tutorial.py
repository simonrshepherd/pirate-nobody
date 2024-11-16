from adventurelib import *

Room.items = Bag()

Room_1 = Room("""
type"take key" then type"south"
""")

wierd_key = Item('wierd key', 'key')
Room_1.items = Bag({wierd_key})
current_room = Room_1

Room_2 = Room("""
find small key(by cheking in the rooms east and west of you) and go into this room then type"south"(clue:
what is the left letter of a compas)
""")
Room_3 = Room("""
sorry, try again
""")
Room_4 = Room("""
CONGATULATIONS you found the key.  Go to Room_2 and then go south
""")
small_key = Item('small key', 'key')
Room_4.items = Bag({small_key})

Room_5 = Room("""
you now know what to do.
""")
Room_6 = Room("""
keep on going
""")
Room_7 = Room("""
go north
""")
Room_8 = Room("""
go on the direction of the top of the compass
""")
Room_9 = Room("""
go in the direction of the left of the compass
""")
Room_10 = Room("""
you found the good key!
""")
good_key = Item('good key', 'key')
Room_10.items = Bag({good_key})

Room_11 = Room("""
sorry try again
""")
Room_12 = Room("""
find a magic key AND a fuzzed sword AND a magic wand
""")
Room_13 = Room("""
please take the wand
""")
magic_wand = Item('magic wand','wand')
Room_13.items = Bag({magic_wand})

Room_14 = Room("""
go east to find a magic key AND a fuzzed sword(and west if not found wand)
""")
Room_15 = Room("""
take the sword please!
""")
fuzzed_sword = Item('fuzzed sword','sword')
Room_15.items = Bag({fuzzed_sword})

Room_16 = Room("""
keep on going!
""")
Room_17 = Room("""
you've got it
""")
Room_18 = Room("""
just 10 more rooms to go(north)6(south)
""")
Room_19 = Room("""
9(north)7(south)
""")
Room_20 = Room("""
8(west/south)
""")
Room_21 = Room("""
7(west)8(east)
""")
Room_22 = Room("""
6(west)10(east)
""")
Room_23 = Room("""
5(west)11(east)
""")
Room_24 = Room("""
4(south)12(east)
""")
Room_25 = Room("""
3(south)13(north)
""")
Room_26 = Room("""
2(south)14(north)
""")
Room_27 = Room("""
1(east)15(north)
""")
Room_28 = Room("""
take magic key
""")
magic_key = Item('magic key', 'key')
Room_28.items = Bag({magic_key})

Prison_cell = Room("""
congrats! you beet the toturial leavle
""")




Room_1.south = Room_2
Room_2.south = Room_5
Room_2.east = Room_3
Room_2.west = Room_4
Room_5.east = Room_6
Room_6.east = Room_7
Room_7.north = Room_8
Room_8.north = Room_9
Room_9.west = Room_10
Room_5.west = Room_11
Room_12.east = Room_13
Room_13.east = Room_14
Room_14.east = Room_15
Room_15.north = Room_16
Room_16.north = Room_17
Room_17.north = Room_18
Room_18.north = Room_19
Room_19.west = Room_20
Room_20.west = Room_21
Room_21.west = Room_22
Room_22.west = Room_23
Room_23.west = Room_24
Room_24.south = Room_25
Room_25.south = Room_26
Room_26.south = Room_27
Room_27.east = Room_28
Room_28.east = Room_12
Room_5.south = Room_12
Room_12.south = Prison_cell









inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    new_room = current_room.exit(direction)
    if new_room:

        if new_room == Room_2:
            if inventory.find('wierd key'):
                say('You put the key in the lock. The door opens')
            else:
                say('There is a arched door, and you need a key to enter it')
                return


        if new_room == Room_5:
            if inventory.find('small key'):
                say('You put the key in the lock. The door opens')
            else:
                say('There is a arched door, and you need a key to enter it')
                return

        if new_room == Room_12:
            if inventory.find('good key'):
                say('You put the key in the lock. The door opens')
            else:
                say('There is a arched door, and you need a key to enter it')\
                return

        if new_room == Prison_cell:
            if inventory.find('magic key'):
                say('You put the key in the lock. The door opens')
            else:
0 23
3say('There is a arched door, and you need a key to enter')
   0.
0r....eturn

            if new_room == Prison_cell:
                if inventory.find('magic wand'):
                    say('You put the key in the lock. The door opens')
                else:
                    say('There is a arched door, and you need a key to enter')
                    return

            if new_room == Prison_cell:
                if inventory.find('fuzzed sword'):
                    say('You put the key in the lock. The door opens')
                else:
                    say('There is a arched door, and you need a key to enter')
                    return

        current_room = new_room


        say('You creep %s.' % direction)
        look()
        set_context('default')
    else:
        say('There is nothing to the %s.' % direction)


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)


@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura')
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    elif magic == 'fireball':
        say("A flaming Fireball shoots form your hands!")


say("""
Intro to tutorial

---------------------------------------

TOTURIAL: TO THE PRISON CELL!!!!

---------------------------------------

You are in a mansion and the last room is a
prison cell.  You are just able to use magic
but it will not help you.  You will also have
to escape the mansion to save your friends!  
""")
look()
start()
