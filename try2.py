from PIL import Image
white = (255, 255, 255)
black = (0, 0, 0)
pattern_grid = [
    [ 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
]
img = Image.new("RGB", (12, 4))
for row in range(12):
    for col in range(4):
        if pattern_grid[col][row]==1:
            img.putpixel((row,col), white)
        else:
            img.putpixel((row,col), black)

resized_img = img.resize((400,400), Image.Resampling.NEAREST)
resized_img.save("pattern2.png")
print("chefs done cooking mate!")
