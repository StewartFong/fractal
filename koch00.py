import turtle
Division = 3.0
DirectionAngle = [60,-120,60]
def call():
       return turtle.left
def koch(n,length):
    if n==0:
       turtle.forward(length)
    else:
       for DA in DirectionAngle:
           koch(n-1,length/Division)
           call()(DA)
       koch(n-1,length/Division)

