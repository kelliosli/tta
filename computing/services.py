def to_points(arr):
    """convert ds moves array to array[point[[mpve],[move]]]"""
    pointed = []
    tmp = []
    for i in arr:
        if i[4]==False:
            tmp.append(i)
            pointed.append(tmp)
            tmp = []
        else:
            tmp.append(i)
    return pointed

def whoWinner(point):
    """return who win point"""
    if point[-1][1]==1:
        return 2
    return 1

def movesToSpins(moves) -> str:
    s = ''
    for move in moves:
        if s=='':
            s+=move[2]
        else:
            s+='-' + move[2]
    return s

def movesToSpinsZones(moves) -> str:
    s = ''
    for move in moves:
        if s=='':
            s+=move[2]+"-"+str(move[3])
        else:
            s+='-' + move[2]+"-"+str(move[3])
    return s

def average_len(points):
    len_moves = int(points[-1][-1][0])
    len_points = len(points)
    return len_moves/len_points

def stats(points, maxCheck=0) -> dict:
    """

    Args:
        points (_type_): array with sorted
        maxCheck (int): max point length

    Returns:
        dict: statistics {
            1:{'SPINS':[points winned, all points]},
            2:{'SPINS':[points winned, all points]}
        }
    """
    tmp = []
    stats = {
        1:{},
        2:{},
    }
    for point in points:
        for move in point:
            if maxCheck != 0 and len(tmp)>maxCheck:
                break
            winner = whoWinner(point)
            player = point[0][1]
            tmp.append(move)
            spin = movesToSpins(tmp)
            if spin not in stats[player]:
                stats[player][spin] = [0,0]
            if winner==player:
                stats[player][spin][0]+=1
                stats[player][spin][1]+=1
            # else:
            #     stats[player][1][spin] = [1,1]
            else:
                stats[player][spin][1]+=1
        tmp=[]
    return stats


def statsU(points, maxCheck=0) -> dict:
    """

    Args:
        points (_type_): array with sorted
        maxCheck (int): max point length

    Returns:
        dict: statistics {
            1:{'SPINS':[points winned, all points]},
            2:{'SPINS':[points winned, all points]}
        }
    """
    tmp = []
    stats = {
        1:{},
        2:{},
    }
    for point in points:
        for move in point:
            if maxCheck != 0 and len(tmp)>maxCheck:
                break
            winner = whoWinner(point)
            player = point[0][1]
            tmp.append(move)
            spin = movesToSpinsZones(tmp)
            if spin not in stats[player]:
                stats[player][spin] = [0,0]
            if winner==player:
                stats[player][spin][0]+=1
                stats[player][spin][1]+=1
            # else:
            #     stats[player][1][spin] = [1,1]
            else:
                stats[player][spin][1]+=1
        tmp=[]
    return stats
    
    
