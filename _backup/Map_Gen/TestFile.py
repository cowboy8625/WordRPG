##-- Nothing In this File is needed --##

x = 5
y = 3
map_width = 6
map_hight = 6


position = x + (y * map_width)

coord_y = int((position / map_width)) # (position - x) / map_width

coord_x = position - (map_width * coord_y)  

print(f"Postion: {position}")
print('--------------------')
print(f"Total Volume of Map: {map_width * map_hight}")
print('--------------------')
print(f"X is: {coord_x} --- {coord_x == x} X Should: {x}")
print('--------------------')
print(f"Y is: {coord_y} --- {coord_y == y} Y Should: {y}")


