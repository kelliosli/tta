import random
import csv

import randomizer
import services


firstRow = ('id', 'playerid', 'spin','zone','hit', 'score')
print()
#test
file = []
scoreSet = {
    1:[],
    2:[]
}

file.append(firstRow)
id=1
serveCounter  = [random.randint(1,2),1]
playerIdCounter = serveCounter[0]
playerStartCounter = serveCounter[0]
score = [0,0,0,0]#[1playerSets,2playerSets, 1playerPoints,2playerPoints]

setNotEnded = 0
matchNotEnded = False

while matchNotEnded==False:
    if playerIdCounter % 2 == 0: 
        playerIdToWrite = 2 
    else:
        playerIdToWrite = 1
    
    hitted = randomizer.hitterRandomizer.generate()
    if hitted:
        if playerIdCounter==playerStartCounter:
            spinInMove = randomizer.serveSpinRandomizer.generate()
            zoneInMove = randomizer.serveZoneRandomizer.generate()
        else:
            spinInMove = randomizer.rallySpinRandomizer.generate()
            zoneInMove = randomizer.rallyZoneRandomizer.generate()
    else:
        if playerIdCounter==playerStartCounter:
            spinInMove = randomizer.serveSpinRandomizer.generate()
            zoneInMove = 0
        else:
            spinInMove = randomizer.rallySpinRandomizer.generate()
            zoneInMove = 0
            
    file.append([id, playerIdToWrite, spinInMove, zoneInMove,hitted])
    print([id, playerIdToWrite, spinInMove, zoneInMove,hitted], score)
    playerIdCounter += 1
    id += 1
    if hitted == False:
        serve = services.whoNextServe(serveCounter)
        serveCounter = serve[1]
        playerIdCounter=serve[0]#TO DO
        playerStartCounter = serve[0]
        if playerIdToWrite==1:
            score[3]+=1
        elif playerIdToWrite==2:
            score[2]+=1
                
    setNotEnded = services.checkSetIsEnded(score)
    if setNotEnded == 1:
        score[0] += 1
        scoreSet[1].append(score[2])
        scoreSet[2].append(score[3])
        
        score[3]=0
        score[2]=0
    elif setNotEnded == 2:
        score[1] += 1
        scoreSet[1].append(score[2])
        scoreSet[2].append(score[3])
        
        score[3]=0
        score[2]=0
        
    matchNotEnded=services.checkMatchIsEnded(score)
print('match created')


with open('match ' + services.scoreToTitle(scoreSet) +'.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(file)
    
print('succes')
print(str(scoreSet))