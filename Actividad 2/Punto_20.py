class recta(object):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def parametros(self):
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        b = self.y1 - m * self.x1
        if m%1 != 0:
            A,B,C=m*(m%1)**(-1),-(m%1)**(-1),(-m*self.x1+self.y1)*(m%1)**(-1);
            return (A,B,C)
        else:
            A,B,C=m,-1,-m*self.x1+self.y1;
            return (A,B,C)
    
    def __str__(self):
        return "La escuación de la recta es {}x + {}y + {} = 0".format(self.parametros()[0],self.parametros()[1],self.parametros()[2])

recta1 = recta(-2,5,1,2)
print(recta1.parametros())