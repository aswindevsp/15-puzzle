import time
import queue

def graph():
    map=[]
    for i in range(4):
        num = input().split()
        for j in range(4):
            map.append(int(num[j]))
    return tuple(map)
def manhatten(map):
        dx = 0
        dy = 0
        for i in range(16):
            if map[i] != 0:
                j = map[i]-1
                dy += abs(i-j)/4
                dx += abs((i % 4) - (j % 4))
        return dx,dy
    
goal = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0)
init_map = graph()
dx_i,dy_i = manhatten(init_map)
class board():
    def __init__(self,map_=(),path_='',cnt_= 0):
        self.map = map_
        self.path = path_
        self.cnt = cnt_
        self.dx,self.dy = manhatten(map_)
        global dy_i,dx_i
        self.score = (self.dx+self.dy)*1.0143+self.cnt+abs(self.dx*dy_i-self.dy*dx_i)*0.143
        
    def getNeighbour(self):
        for i in range(16):
            if self.map[i] == 0:
                break
        neighbour = []
        move = {
                'left': -1,
                'down': 4,
                'up': -4,
                'right': 1
                }
        for direc in move:
            if i + move[direc] < 16 and i + move[direc] >= 0:
                if i + move[direc] > i:
                    x,y = i,i+move[direc]
                else:
                    x,y = i+move[direc],i
                map_ = self.map[:x]+self.map[y:y+1]+self.map[x+1:y]+self.map[x:x+1]+self.map[y+1:]
                path_ = self.path
                path_ += str(map_[i]) + ' '
                if solvable(map_):
                    neighbour.append(board(map_,path_,self.cnt+1))
        return sorted(neighbour,key=lambda x:[x.score,-x.cnt])
    



    


def solvable(map):
    cnt = 0
    flag = 0
    for i in range(16):
            if map[i] == 0:
                flag = int(i/4)
                continue
            for j in range(i,16):
                if map[j] == 0:
                    continue
                if map[i] > map[j]:
                    cnt+=1
    return (cnt + flag) % 2 != 0   
 
                
def Astar(map):
    frontier = queue.PriorityQueue()
    closed  = dict()
    if solvable(map) is False:
        return "No Solution"
    else:
        frontier.put((0,0,0,board(map)))
        j = 0
        while not frontier.empty():
            top = frontier.get()
            node = top[3]
            nsco = top[0]
            print(j)
            if node.map in closed and nsco > closed[node.map]:
                continue
            closed.update({node.map: nsco})
            if node.map == goal:
                return node.path + "\nA optimal solution " + str(node.cnt) + " moves\n" +"Searched for " + str(j) + " times!"
            nei = node.getNeighbour()
            for n in nei:
                j+=1
                if n.map not in closed:
                    frontier.put((n.score,-n.cnt,j,n))    
        return "Error!"
    
                
    
    

def main():
    time_start=time.time()
    print(Astar(init_map))
    time_end=time.time()
    print('It cost ',time_end-time_start,'s',sep='') 
        
    
    
    

main()