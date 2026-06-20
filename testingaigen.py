print("testing...")
from PIL import Image


pink = (255, 182, 193)
white = (255, 255, 255)
red = (255, 89, 100) 


pattern_grid = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 2, 2, 0, 1, 0, 1, 0], 
    [0, 1, 0, 1, 2, 2, 2, 2, 0, 1, 0, 1], 
    [1, 0, 1, 2, 2, 2, 2, 2, 2, 0, 1, 0], 
    [0, 1, 0, 1, 2, 1, 0, 2, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
]

img = Image.new("RGB", (12, 12))

for row in range(12):
    for col in range(12):
        grid_value = pattern_grid[row][col]
        if grid_value == 0:
            img.putpixel((col, row), pink)
        elif grid_value == 1:
            img.putpixel((col, row), white)
        else:
            img.putpixel((col, row), red) 

resized_img = img.resize((600, 600), Image.Resampling.NEAREST)

from PIL import ImageDraw

draw = ImageDraw.Draw(resized_img)
cell_size = 50
outline_color = (0, 0, 0)
for row in range(12):
    for col in range(12):
        x0 = col * cell_size
        y0 = row * cell_size
        x1 = x0 + cell_size - 1
        y1 = y0 + cell_size - 1
        draw.rectangle([x0, y0, x1, y1], outline=outline_color)

resized_img.save("cute_sweater_pattern.png")
print("done and dusted")
