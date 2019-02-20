from classes.game import person, bcolors
from classes.magic import spell

# create black magic
fire = spell('fire', 8, 100, 'black')
thunder = spell('thunder', 12, 124, 'black')
blizzard = spell('blizzard', 10, 110, 'black')
meteor = spell('meteor', 20, 200, 'black')
quake = spell('quake', 14, 142, 'black')

# create white magic
cure = spell('cure', 12, 120, 'white')
cura = spell('cura', 18, 200, 'white')

# instantiate people
player = person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS' + bcolors.ENDC)

while running:
    print('====================')
    player.choose_action()
    choice = input('Choose an action: ')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose magic: ')) - 1

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        if spell.type == 'white':
            player.reduce_mp(spell.cost)
            player.heal(magic_damage)
            print(bcolors.OKBLUE + '\n' + spell.name + " heals for", str(magic_damage), "HP." + bcolors.ENDC)
        elif spell.type == 'black':
            player.reduce_mp(spell.cost)
            enemy.take_damage(magic_damage)
            print(bcolors.OKBLUE + '\n' + spell.name + ' deals', str(magic_damage), 'points of damage' + bcolors.ENDC)
            print()

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)

    print("Enemy attacks for", enemy_damage)

    print("--------------------------------")
    print('Enemy HP: ', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')
    print('Your HP: ', bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.ENDC)
    print('Your MP: ', bcolors.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC + '\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You Win!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'Your enemy has defeated you!' + bcolors.ENDC)
        running = False
