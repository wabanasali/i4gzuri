import random
counter, player, cpu= 0, '', ''
optns= ['R', 'P', 'S']
wins = [('R','S'), ('P','R'), ('S', 'P')]
def whoami(x):
    if x == 'R':
        y = 'Rock'
    elif x == 'P':
        y = 'Paper'
    else:
        y = 'Scissors'
    return y
ch = input('Enter R for Rock'+'\n'+'Enter P for Paper'+'\n'+'Enter S for Scissors'+'\n')
while counter == 0:
    if ch in optns:
        cpu_current_option = random.choice(list(optns))
        player, cpu = whoami(ch), whoami(cpu_current_option)
        if cpu_current_option == ch:
            counter = 0
            print("Player("+player+"): CPU("+cpu+")")
            print('There has been a tie')
            ch = input('Enter R for Rock'+'\n'+'Enter P for Paper'+'\n'+'Enter S for Scissors'+'\n')
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
        ch = input('Enter R for Rock'+'\n'+'Enter P for Paper'+'\n'+'Enter S for Scissors'+'\n')
