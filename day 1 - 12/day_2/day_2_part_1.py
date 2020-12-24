with open('day_2.txt') as f:
    p = f.readlines()
    count = 0
    for l in p:
        splitted_l = l.split()
        policy = splitted_l[0].split('-')
        letter = splitted_l[1][:-1]
        passwd = splitted_l[2]

        if (passwd.count(letter) >= int(policy[0]) and passwd.count(letter) <= int(policy[1])):
            count += 1

print(count)
        
           
        
