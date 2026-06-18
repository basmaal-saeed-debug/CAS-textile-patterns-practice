print("pattern code working!")
from PIL import Image

pink = (255, 182, 193)
white = (255, 255, 255)

pattern_grid = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

img = Image.new("RGB", (4, 4))

for row in range(4):
    for col in range(4):
        grid_value = pattern_grid[row][col]
        if grid_value == 0:
            img.putpixel((col, row), pink)
        else:
            img.putpixel((col, row), white)

resized_img = img.resize((400, 400), Image.Resampling.NEAREST)
resized_img.save("firstpattern.png")
print("Visual pattern photo created successfully!")