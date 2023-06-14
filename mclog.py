import time
pre = ''    #variable to store the previuos row
blacklist = ['test', 'apple']  #blacklisted words

while True:
    cache = open('C:/Users/user/AppData/Roaming/.Salwyrr/logs/latest.log', #Minecraft lates.log path
                 'r', encoding='utf-8')     #open a cache
    _ = list(cache)[-1]

    block = False

    for x in _.strip().split():  #checking for blacklisted words
        for word in blacklist:
            if x == word:
                block = True

    #checks if it isn't the previuos row, not blocked by the blacklist and it is written out to the chat
    if _ != pre and block == False and '[chat]' in _.lower():
        pre = _
        print(_, end='')
    time.sleep(0.05)

cache.close()   #close a cache

#Note! The code is about the idea, this code is far from perfect but it kinda works.
