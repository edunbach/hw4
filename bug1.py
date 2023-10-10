#Q4 bug1.py circle class

class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        returnf'''This is a circle
    ({self.x}, {self.y})
    {self.size}'''

    def draw(self):
        return f'''

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

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

if __name__ == "__main__":
    main()
