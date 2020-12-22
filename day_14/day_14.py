with open('day_14.txt') as f:
    prog= f.read().splitlines()

# Part 1
def masked_value(mask, val):
    bin_value = format(int(val), '036b')
    mskd_value= ''
    for i, bit in enumerate(mask):
        if bit == 'X':
            mskd_value += bin_value[i]
        else:
            mskd_value += bit
    return int(mskd_value, 2)

mask = None
memory = dict()

for line in prog:
    cmd, _, val = line.split()
    if cmd == 'mask':
        mask = val
    elif cmd[:3] == 'mem':
        address = int(cmd[4:-1])
        msk_value = masked_value(mask, val)
        memory[address] = msk_value

# Part 2
def addresses_from_mask(mask, address):
    bin_address = format(address, '036b')
    mskd_address = ''
    for i, bit in enumerate(mask):
        if bit == 'X':
            mskd_address += 'X'
        elif bit == '0':
            mskd_address += bin_address[i]
        elif bit == '1':
            mskd_address += '1'

    new_addresses = list()
    num_x = mskd_address.count('X')
    for i in range(2 ** num_x):
        mskd_address_sub = mskd_address
        for sub_bit in format(i, '0{}b'.format(num_x)):
            mskd_address_sub = mskd_address_sub.replace('X', sub_bit, 1)
        new_addresses.append(int(mskd_address_sub, 2))
    return new_addresses

mask = None
memory = dict()

for line in prog:
    cmd, _, val = line.split()
    if cmd == 'mask':
        mask = val
    elif cmd[:3] == 'mem':
        address = int(cmd[4:-1])
        for new_address in addresses_from_mask(mask, address):
            memory[new_address] = int(val)
    
