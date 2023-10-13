class Player():

    def __init__(self):
    #    self.x=x
    #    self.y=y
    #    self.direction=direction
    #    self.traine=[(self.x, self.y)]
    #    self.color=color

       self.score=0
       self.victoire=False
    #    self.vitesse=vitesse

    def update_pos(self):
        self.x = self.x + self.direction[0] * self.vitesse
        self.y = self.x + self.direction[1] * self.vitesse
        #ntw.sending_queue.put("pos,"+(self.nouveau_x ,self.nouveau_y))
        # self.x, self.y = pos
    def update_traine(self):
        self.traine=self.traine.append((self.x,self.y))

    def __repr__(self) -> str:
        return f'x : {self.x} | y: {self.y} | dir : {self.direction}'
        
    def __str__(self) -> str:
        return f'x : {self.x} | y: {self.y} | dir : {self.direction}'

    def deserialize(self, data : dict):
        self.x = data['x']
        self.y = data['y']
        self.traine = data['traine']