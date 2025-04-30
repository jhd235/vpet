from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple pet shape (a circle with ears)
# Body
draw.ellipse([50, 50, 150, 150], fill='lightblue', outline='black')
# Ears
draw.ellipse([40, 40, 80, 80], fill='lightblue', outline='black')
draw.ellipse([120, 40, 160, 80], fill='lightblue', outline='black')
# Eyes
draw.ellipse([80, 80, 90, 90], fill='black')
draw.ellipse([110, 80, 120, 90], fill='black')
# Smile
draw.arc([80, 100, 120, 120], 0, 180, fill='black', width=2)

# Save the image
image.save('pet.png')
print("Pet image created successfully!") 