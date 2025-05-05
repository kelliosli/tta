class ttAnalyzer():
    """
    Analyze table tennis game to 
    """
    
    def __init__(self, game) -> None:
        self.game = game
        self.pointed_array = self._to_pointed_array()
        
    # def statistics(self) -> dict:
    #     """return statistics dict"""
    #     stat = {
    #         1:{},
    #         2:{},
    #     }
        
    #     for point in self.pointed_array:
    #         whoWinned = self.whoWinner(point)
            
    #         for move in point:
    
    
    def combinations(self, max_comb = 3) -> dict:
        stat = {
            1:{
                "spin": {},
                "zone":{},
                "zoneSpin":{}
                },
            2:{
                "spin": {},
                "zone":{},
                "zoneSpin":{}
                },
        }

        for point in self.pointed_array:
            winned = self.whoWinner(point)
            n = len(point)
            for i in range(n-1):
                tmp = []
                tmp_zone = []
                tmp_zs = []
                player = point[i][1]
                for l in range(i, n-1,2):
                    tmp.append(point[l][2])
                    tmp_zone.append(str(point[l][3]))
                    tmp_zs.append(f"{point[l][2]}:{point[l][3]}")
                    # print(tmp, '-'.join(tmp))
                    if len(tmp)>1 and len(tmp)<=max_comb:
                        spins = '-'.join(tmp)
                        zones = '-'.join(tmp_zone)
                        zs = '-'.join(tmp_zs)
                        if spins not in stat[player]['spin']:
                            stat[player]['spin'][spins] = [0,0]
                        if zones not in stat[player]['zone']:
                            stat[player]['zone'][zones] = [0,0]
                        if zs not in stat[player]['zoneSpin']:
                            stat[player]['zoneSpin'][zs] = [0,0]
                        stat[player]['spin'][spins][1] += 1
                        stat[player]['zone'][zones][1] += 1
                        stat[player]['zoneSpin'][zs][1] += 1
                        if player == winned:
                            stat[player]['spin'][spins][0] += 1
                            stat[player]['zone'][zones][0] += 1
                            stat[player]['zoneSpin'][zs][0] += 1
        return stat
                
                
                
                
        
    
    def average_len(self):
        len_moves = int(self.pointed_array[-1][-1][0])
        len_points = len(self.pointed_array)
        return len_moves/len_points
    
    def get_game(self):
        return self.game
    
    def get_pointed_game(self):
        return self.pointed_array
    
    def whoWinner(self, point):
        if point[-1][1]==1:
            return 2
        return 1
    
    def frequency(self):
        stat  = {
            1:{
                "zone":{},
                "spin":{},
                "spinServe":{},
                "zoneServe":{},
                },
            2:{
                "zone":{},
                "spin":{},
                "spinServe":{},
                "zoneServe":{},
                },
        }
        for l in range(len(self.game)-1):
            i = self.game[l]
            if l != 1:
                if self.game[l-1][4]==False:
                    if i[2] not in stat[i[1]]['spinServe']:
                        stat[i[1]]['spinServe'][i[2]] = 0
                    if str(i[3]) not in stat[i[1]]['zoneServe']:
                        stat[i[1]]['zoneServe'][str(i[3])] = 0
                    stat[i[1]]['spinServe'][i[2]] += 1
                    stat[i[1]]['zoneServe'][str(i[3])] += 1               
                else:
                    if i[2] not in stat[i[1]]['spin']:
                        stat[i[1]]['spin'][i[2]] = 0
                    if str(i[3]) not in stat[i[1]]['zone']:
                        stat[i[1]]['zone'][str(i[3])] = 0
                    stat[i[1]]['spin'][i[2]] += 1
                    stat[i[1]]['zone'][str(i[3])] += 1
            else:
                if i[2] not in stat[i[1]]['spinServe']:
                    stat[i[1]]['spinServe'][i[2]] = 0
                if str(i[3]) not in stat[i[1]]['zoneServe']:
                    stat[i[1]]['zoneServe'][str(i[3])] = 0
                stat[i[1]]['spinServe'][i[2]] += 1
                stat[i[1]]['zoneServe'][str(i[3])] += 1
        return stat
        
    # def frequency_winned(self):
    #     pass
    
    def _to_pointed_array(self):
        """convert ds moves array to array[point[[mpve],[move]]]"""
        pointed = []
        tmp = []
        for i in self.game:
            if i[4]==False:
                tmp.append(i)
                pointed.append(tmp)
                tmp = []
            else:
                tmp.append(i)
        return pointed
    
    def _movesToSpins(self, moves) -> str:
        s = ''
        for move in moves:
            if s=='':
                s+=move[2]
            else:
                s+='-' + move[2]
        return s
    