import os
from PIL import Image
frame_files = [f"./frames/frame_{i:03d}.png" for i in range(1, 4383)]

output_file = "frames.txt"
img_width = 16
img_height = 12

with open(output_file, "w") as f:
    for frame_file in frame_files:
        image = Image.open(frame_file).convert("L")
        image = image.resize((img_width, img_height))

        binary_matrix = []
        for y in range(img_height):
            row = []
            for x in range(img_width):
                pixel = image.getpixel((x, y))
                row.append(1 if pixel < 128 else 0)
            binary_matrix.append("".join(map(str, row)))

        f.write("".join(binary_matrix) + "&")

print(f"Frames saved to {output_file}")