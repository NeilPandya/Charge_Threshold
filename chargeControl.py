# A simple python script to setting the battery charge threshold easier.


def get_current_threshold():
    read_power_cfg = open('/sys/class/power_supply/BAT0/charge_control_end_threshold', 'r')
    print('Current battery charge threshold (%):', read_power_cfg.read())


def change_threshold():
    write_power_cfg = open('/sys/class/power_supply/BAT0/charge_control_end_threshold', 'w')
    ch_val = input('Enter new value (an integer from 0 to 100): ')
    if int(ch_val) < 0 or int(ch_val) > 100:
        print('Please enter a valid parameter (an integer from 0 to 100).')
        change_threshold()
    else:
        write_power_cfg.write(ch_val)
        print('New battery charging threshold set to', ch_val+'%.')


def ask_to_change():
    get_current_threshold()
    change_opt = input('Would you like to change it? (y/n): ')
    if change_opt == 'y' or change_opt == 'Y':
        change_threshold()
        print('Bye!')
    elif change_opt == 'n' or change_opt == 'N':
        print('Bye!')
    elif change_opt != 'y' or change_opt != 'n':
        print('Invalid response. Please enter yes or no (y/n).')
        ask_to_change()


ask_to_change()
exit()
