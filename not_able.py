from random import choice
class randomwalk:
    def __init__(self,n=50000):
        self.n=n

        self.x_value=[0]
        self.y_value=[0]
    def walk(self):
        while len(self.x_value)<self.n:
            #Start walking

            x_directon=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_walk=x_directon*x_distance


            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_walk=y_direction*x_distance


            if x_distance==0 and y_distance==0:
                continue

            x=self.x_value[-1]+x_walk
            y=self.y_value[-1]+y_walk

            self.x_value.append(x)
            self.y_value.append(y)


            
        