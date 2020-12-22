with open('day_13.txt') as f:
    times = f.read().splitlines()

timestamp, buses = int(times[0]), times[1].split(',')
closest_timestamp = dict()

'''
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        closest_timestamp[bus] = timestamp - (timestamp % bus) + bus
'''

