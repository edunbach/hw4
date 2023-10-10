#Q4 bug1.py circle class

class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f'''This is a circle
({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '

'''

