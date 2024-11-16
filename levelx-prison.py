from adventurelib import *

Room.items = Bag()

prison_cell = Room("""
You are in a dark prison cell, that smells of poo.you want a lamp to light up the room.
""")
# todo Have Lamp == you can see sword in prison cell

poo = Item('poo', 'poop')
prison_cell.items = Bag({poo})
current_room = prison_cell

prison_yard = Room("""
You are in a dirty prison yard with high walls.
""")
guard_chamber1_key = Item('large key', 'key')
prison_yard.items = Bag({guard_chamber1_key})

guard_chamber1 = Room("""
You are in a guard's chamber.
""")

hallway1 = Room("""
You are in a hallway with a lantern
""")
lantern = Item('lantern', 'lamp')
hallway1.items = Bag({lantern})

dark_chamber = Room("""
You are in a dark chamber with a high roof
""")

bright_chamber = Room("""
You are in a bright chamber with a friend
""")

kitchen_chamber = Room("""
You are in a wierd chamber with food and a friend
""")

dining_chamber = Room("""
there is a table with food
""")
mashed_potatoes = Item('mashed potatoes with jelly', 'potatoes')
muddy_water = Item('muddy water', 'water')
dining_chamber.items = Bag({mashed_potatoes, muddy_water})

play_chamber = Room("""
you are in a vast chamber with toys
""")

laundry_chamber = Room("""
you are in a vast chamber with a lot of clothes
""")

gym = Room("""
you are in a vast Room with a high Roof and a friend
""")

bed_chamber1 = Room("""
you are in a small Room with a big Roof and a bed and a pillow
""")
pillow = Item('pillow')
bed_chamber1.items = Bag({pillow})

hallway2 = Room("""
this Room STINKS! but you are not grossed out
""")
bundle_of_poo = Item('bundle of poo')
hallway2.items = Bag({bundle_of_poo})

bed_chamber2 = Room("""
you are in a small Room with a big Roof and a bed with a blanket on it
""")
blanket = Item("blanket")
bed_chamber2.items = Bag({blanket})

great_hall = Room("""
this Room has a big Roof and a long rectanguler table with a huge chair at the end of the table
""")
garden1 = Room("""
you are in a butiful garden with a lot of potatoes and flowers
""")
tower1 = Room("""
you can see all the land around
""")
tower2 = Room("""
you can see all the land around
""")
tower3 = Room("""
you can see all the land around
""")
tower4 = Room("""
you can see all the land around
""")
garden2 = Room("""
you are in a butiful garden with a lot of potatoes and flowers at the end of the garden
""")
small_key = Item('small key', 'key')
garden2.items = Bag ({small_key})

garden3 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and tamatos at the end of the garden
""")
medium_key = Item('medium key', 'key')
garden3.items = Bag ({medium_key})

garden4 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and cabbages at the end of the garden
""")
cabbage = Item('cabbage', 'plant')
garden4.items = Bag ({cabbage})
garden5 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and celary at the end of the garden
""")
cellery = Item('cellery', 'plant')
garden5.items = Bag ({cellery})
garden6 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and cucumbers at the end of the garden
""")
cucumber = Item('cucumber', 'plant')
garden6.items = Bag ({cucumber})

garden7 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and strawberrys at the end of the garden
""")
strawberry = Item('strawberry', 'plant')
garden7.items = Bag ({strawberry})

garden8 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and blackberrys at the end of the garden
""")
blackberry = Item('blackberry', 'plant')
garden8.items = Bag ({blackberry})

garden9 = Room("""
you are in a beautiful garden with a lot of potatoes and flowers and blueberrys at the end of the garden
""")
blueberry = Item('blueberry', 'plant')
garden9.items = Bag ({blueberry})

garden10 = Room("""
you are in a beautiful garden with a lot of potatoes and flowers and pineapples at the end of the garden
""")
pineapple = Item('pineapple', 'plant')
garden10.items = Bag ({pineapple})

garden11 = Room("""
you are in a beautiful garden with a lot of potatoes and flowers and oranges at the end of the garden
""")
oranges = Item('oranges', 'plant')
garden11.items = Bag ({oranges})

garden12 = Room("""
you are in a beautiful garden with a lot of potatoes and flowers and pears at the end of the garden
""")
potatoes = Item('potatoes','plant')
garden12.items = Bag({potatoes})

garden13 = Room("""
you are in a butiful garden with a lot of potatoes and flowers and whiteberrys at the end of the garden
""")
whiteberry = Item("Whiteberry")
garden13.items = Bag({whiteberry})

play_ground = Room("""
You are in a play ground with a lot of kids
""")
sand = Item('sand', 'sand_bag')
play_ground.items = Bag({sand})

weapon_chamber1 = Room("""
You are in a chamber with a lot of weapons
""")
sword = Item("long metal sword", "sword")
weapon_chamber1.items = Bag({sword})

weapon_chamber2 = Room("""
you are in a chamber with a lot of shields
""")
shield = Item(" large wooden shield", "shield")
weapon_chamber2.items = Bag({shield})
guards_chamber2 = Room("""
you are in a guards chamber with a guard that is asleep and your best friend
""")
hammer = Item(" large hammer", "hammer")
guards_chamber2.items = Bag({hammer})
garden14 = Room("""
this garden is so butiful
""")
apple = Item("apple", "apple")
garden14.items = Bag({apple})

front_gate = Room("""
you are in a room with a lot of armed guards
""")

hallway1.south = prison_yard
prison_cell.south = hallway1
hallway1.east = dark_chamber
hallway1.west = bright_chamber
guard_chamber1.south = kitchen_chamber
bright_chamber.south = guard_chamber1
kitchen_chamber.east = prison_yard
bright_chamber.north = dining_chamber
dark_chamber.north = play_chamber
dark_chamber.east = laundry_chamber
dark_chamber.south = gym
gym.west = prison_yard
gym.south = bed_chamber1
bed_chamber1.west = hallway2
hallway2.west = guard_chamber1
play_chamber.north = bed_chamber2
bed_chamber2.west = great_hall
great_hall.south = dining_chamber
great_hall.north = garden1
great_hall.west = tower4
hallway2.south = tower3
gym.east = tower2
bed_chamber2.north = tower1
garden1.east = garden2
garden2.east = garden3
garden3.east = garden4
garden4.south = garden5
garden5.west = play_chamber
garden5.south = laundry_chamber
garden5.east = garden6
garden6.east = garden7
garden7.south = garden8
garden8.south = garden9
garden9.south = garden10
garden10.south = tower2
tower2.south = garden11
garden11.west = garden12
garden12.west = garden13
garden13.west = bed_chamber1
garden13.south = play_ground
play_ground.west = weapon_chamber1
weapon_chamber1.west = weapon_chamber2
garden1.north = garden14
tower3.south= front_gate

inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    new_room = current_room.exit(direction)
    if new_room:
        if new_room == guard_chamber1:
            if inventory.find('large key'):
                say('You put the key in the lock. The door opens')
            else:
                say('There is a large door, and you need a key to enter it')
                return

        if new_room == tower2:
            if inventory.find('small key'):
                say('you put the key in the lock. as you do the door opens')
            else:
                say('you need to look in garden2 for a small key')
                return

        if new_room == front_gate:
            key_hash = ''
            if inventory.find('small key'):
                key_hash += '1'
            else:
                key_hash += '0'
            if inventory.find('medium key'):
                key_hash += '1'
            else:
                key_hash += '0'
            if inventory.find('large key'):
                key_hash += '1'
            else:
                key_hash += '0'

            match key_hash:
                case '111':
                    say('You put the keys in the lock. as you do the door opens')
                case '000':
                    say('There are 3 locks on this door, and you do not have any keys to fit in any of them')
                    return
                case '001':
                    say('you fill the large key hole,but the smaller locks you need keys for')
                    return
                case '010':
                    say('the middle lock is filled,but the other ones need a key')
                    return
                case '011':
                    say('you fill the two biggest key holes,but there is a small one that needs a key')
                    return
                case '100':
                    say('you fill the smallest key hole,but not the larger ones')
                    return
                case '101':
                    say('the smallest and largest key holes are filled,but the middle one needs a key')
                    return
                case '110':
                    say('While two of your keys fit in the two smallest locks, there is a larger lock that you still need to find the key for')
                    return

            if inventory.find('sword'):
                say('you hit a guard with a sword and kill the guard')
            else:
                say('you are not armed so you are thrown in jail')
                weapon_chamber2.items.add(inventory.take('shield'))
                current_room = prison_cell

                return

            if inventory.find('shield'):
                say('another guard tries to hit you, but you block it with your shield and bosh him with your sword!')

            else:
                say('even though you might have a sword a guard hits you from behind - if you had a shield, maybe you could have protected yourself! He throws you back in your cell')
                weapon_chamber1.items.add(inventory.take('sword'))
                current_room = prison_cell
                return

        current_room = new_room

        if current_room == front_gate:
            say("""
            You run out the prison to freedom!
            
            Looking behind, you see your friends run out after you.

            -------------------------------------

            LEVEL 1: ESCAPE THE PRISON! - COMPLETE!

            -------------------------------------

            """)



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
You are pirate nobody, a pirate who has no name and likes poo.
 
You have been imprisoned by the King because he asked you to build a ship, but you built it from poo.
 
It didn't work, so the King thew you in prison.
 
Your goal now is to escape prison, and show the world that a ship made from poo can sail!

-------------------------------------

LEVEL 1: ESCAPE THE PRISON!

-------------------------------------

""")
look()
start()
