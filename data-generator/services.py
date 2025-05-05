def checkSetIsEnded(score : list) -> int:
    if (score[2]-score[3]==2 and score[3]>=9) or (score[2]==11 and score[3]<=9):
        return 1
    elif (score[3]-score[2]==2 and score[2]>=9) or (score[3]==11 and score[2]<=9):
        return 2
    return 0

def checkMatchIsEnded(score : list) -> bool:
    if score[0]==3 or score[1]==3:
        return True
    return False
    
def whoNextServe(serves : list) -> list:
    if serves[0] == 1 and serves[1]==1:
        return [1,[1,2]]
    elif serves[0] == 1 and serves[1]==2:
        return  [2,[2,1]]
    elif serves[0] == 2 and serves[1]==1:
        return [2, [2,2]]
    elif serves[0] == 2 and serves[1]==2:
        return [1, [1,1]]

def scoreToTitle(scoreSet) -> str:
    s  = []
    s.append(scoreSet[1])
    s.append('-')
    s.append(scoreSet[2])
    res = ''
    for i in s:
        res = res +' ' + str(i) 
    return res

if __name__=='__main__':
    s = {1: [11, 5, 7, 6], 2: [7, 11, 11, 11]}
    print(scoreToTitle(s))
