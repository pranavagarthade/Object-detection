from PIL import Image, ImageDraw
import json

# Load the image
image_path = 'R.jpeg'
image = Image.open(image_path)
gray_image = image.convert('L')  

detected_objects = [(50, 50, 100, 150), (200, 80, 120, 160)]  

# Determine the overall bounding rectangle
if detected_objects:
    x_min = min([x for (x, y, w, h) in detected_objects])
    y_min = min([y for (x, y, w, h) in detected_objects])
    x_max = max([x + w for (x, y, w, h) in detected_objects])
    y_max = max([y + h for (x, y, w, h) in detected_objects])

    bounding_box = (x_min, y_min, x_max - x_min, y_max - y_min)
else:
    bounding_box = (0, 0, gray_image.width, gray_image.height)

# Draw the bounding rectangle on the image
draw = ImageDraw.Draw(image)
draw.rectangle([bounding_box[0], bounding_box[1], bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]], outline="green", width=2)

# Save the processed image
output_image_path = 'output_image.jpg'
image.save(output_image_path)

# Example real-world coordinates (for demonstration purposes)
top_left_coords = (40.7128, -74.0060)  # Latitude, Longitude
length = 500  # in meters
width = 300  # in meters

metadata = {
    "Type": "BoundingRectangle",
    "TopLeftCorner": {
        "Latitude": top_left_coords[0],
        "Longitude": top_left_coords[1]
    },
    "Length": length,
    "LengthUnit": "meters",
    "Width": width,
    "WidthUnit": "meters",
    "BoundingBox": {
        "x": bounding_box[0],
        "y": bounding_box[1],
        "width": bounding_box[2],
        "height": bounding_box[3]
    }
}

# Save metadata to a JSON file
with open('metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)

print("Bounding boxes:", bounding_box)
print("Metadata:", json.dumps(metadata, indent=4))
