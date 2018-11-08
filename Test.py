x = 5
y = 2

width = 6
hight = 6

postion = x + (y * width)

print(postion)

coords_y = (postion - x) / width
coords_x = postion - (width * y)

print(f"Y axis: {coords_y}")
print(f"X axis: {coords_x}")
