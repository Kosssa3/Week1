screen = (1920, 1080)

width = screen[0]
height = screen[1]

print("Width: %d" % width)
print("Height: %d" % height)

pixels = width * height
print("Pixels: %d" % pixels)

aspect_ratio = width / height
print("Aspect ratio: %.2f" % aspect_ratio)

portrait = (height, width)
print("Portrait:", portrait)
