from modules.network_server import NetworkServer


class Player():

    def __init__(self,x,y,direction,color,vitesse=5):
       self.x=x
       self.y=y
       self.direction=direction
       self.traine=[[self.x, self.y]]
    #    self.traine_x=[self.x]
    #    self.traine_y=[self.y]
       self.color=color

       self.score=0
       self.victoire=False
       self.vitesse=vitesse

    def update_pos(self):
        self.x = self.x + self.direction[0] * self.vitesse
        self.y = self.y + self.direction[1] * self.vitesse
        #ntw.sending_queue.put("pos,"+(self.nouveau_x ,self.nouveau_y))
        # self.x, self.y = pos
    def update_traine(self):
        self.traine.append([self.x,self.y])
        # self.traine.append([self.x,self.y])
        # self.traine.append([self.x,self.y])

    def __repr__(self) -> str:
        return f'x : {self.x} | y: {self.y} | dir : {self.direction}'
        
    def __str__(self) -> str:
        return f'x : {self.x} | y: {self.y} | dir : {self.direction}'
    
    def serialize(self):
        return {
            'x' : self.x,
            'y' : self.y,
            # 'direction' : self.direction,
            'traine' : self.traine,
            'color' : self.color
        }



# if __name__ == '__main__':
#     player = Player(0,1,(0,1),(0,0,0))
#     print(player)
#     player.update_pos(())