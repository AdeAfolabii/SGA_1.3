# Purpose : print a dictionary containing keys ranging from 5 to 15 with the valuses being the square

Squares = {}

for x in range (5,15):

    Squares[x] = x*x

print(Squares)

# using dictionary comprehension
 
Squares = {x: x*x for x in range (5,15)}
print(Squares)