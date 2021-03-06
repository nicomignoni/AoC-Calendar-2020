DOOR_PUBLIC_KEY = 12578151
CARD_PUBLIC_KEY = 5051300

NUMERATOR = 20201227

DOOR_LOOPSIZE = 0
CARD_LOOPSIZE = 0

SUBJECT_NUMBER = 7

DOOR_VALUE = 1
while DOOR_VALUE != DOOR_PUBLIC_KEY:
    DOOR_VALUE = (DOOR_VALUE * SUBJECT_NUMBER) % NUMERATOR
    DOOR_LOOPSIZE += 1
    
CARD_VALUE = 1
while CARD_VALUE != CARD_PUBLIC_KEY:
    CARD_VALUE = (CARD_VALUE * SUBJECT_NUMBER) % NUMERATOR
    CARD_LOOPSIZE += 1

print('Doop loopsize: {}\nCard loopsize: {}'.format(DOOR_LOOPSIZE, CARD_LOOPSIZE))

# Encryption key (from card)
ENCRYPTION_KEY = 1
ENCRYPTION_SUBJECT_NUMBER = DOOR_VALUE # (= DOOR_PUBLIC_KEY)
for i in range(CARD_LOOPSIZE):
    ENCRYPTION_KEY = (ENCRYPTION_KEY * ENCRYPTION_SUBJECT_NUMBER) % NUMERATOR

# Encryption key (from door, same final result)
ENCRYPTION_KEY = 1
ENCRYPTION_SUBJECT_NUMBER = CARD_VALUE # (= DOOR_PUBLIC_KEY)
for i in range(DOOR_LOOPSIZE):
    ENCRYPTION_KEY = (ENCRYPTION_KEY * ENCRYPTION_SUBJECT_NUMBER) % NUMERATOR
