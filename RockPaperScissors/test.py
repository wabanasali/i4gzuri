import random
counter, player, cpu= 0, '', ''
cpu_options = {'Rock':1,'Paper':2,'Scissors':3}
wins = [(1,3), (2,1), (3,2)]
def whoami(x):
    if x == 1:
        y = 'Rock'
    elif x == 2:
        y = 'Paper'
    else:
        y = 'Scissors'
    return y
ch = int(input('Enter 1 for Rock'+'\n'+'Enter 2 for Paper'+'\n'+'Enter 3 for Scissors'+'\n'))
while counter == 0:
    if ch in [1,2,3]:
        cpu_current_option = cpu_options[random.choice(list(cpu_options))]
        player, cpu = whoami(ch), whoami(cpu_current_option)
        if cpu_current_option == ch:
            counter = 0
            print("Player("+player+"): CPU("+cpu+")")
            print('There has been a tie')
            ch = int(input('Enter 1 for Rock'+'\n'+'Enter 2 for Paper'+'\n'+'Enter 3 for Scissors'+'\n'))
        else:
            counter = 1
            if (cpu_current_option, ch) in wins:
                print("Player("+player+"): CPU("+cpu+")")
                print('Sorry you lost')
            else:
                print("Player("+player+"): CPU("+cpu+")")
                print('Congrats you won')       
    else:
        print('Value out of desired range')
        ch = int(input('Enter 1 for Rock'+'\n'+'Enter 2 for Paper'+'\n'+'Enter 3 for Scissors'+'\n'))
