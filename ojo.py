import cv2

# Load your image
image = cv2.imread('your_image_path.jpg')  # Replace 'your_image_path.jpg' with the actual path to your image

# Get screen width and height
screen_width, screen_height = 1366, 768  # Update with your screen resolution

# Calculate the aspect ratio of the image
image_aspect_ratio = image.shape[1] / image.shape[0]

# Calculate the new width and height based on the screen resolution and image aspect ratio
new_width = int(min(screen_width, screen_height * image_aspect_ratio))
new_height = int(min(screen_height, screen_width / image_aspect_ratio))

# Resize the image while maintaining its aspect ratio
image = cv2.resize(image, (new_width, new_height))

# Calculate the position to center the image on the screen
start_x = (screen_width - new_width) // 2
start_y = (screen_height - new_height) // 2

# Create a black background with the screen resolution
background = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

# Place the resized image on the black background
background[start_y:start_y + new_height, start_x:start_x + new_width] = image

# Display the image
cv2.imshow('Image', background)
cv2.waitKey(0)

# Use the cv2.selectROI function to interactively select a region
roi = cv2.selectROI('Select ROI', background, fromCenter=False, showCrosshair=True)

# Print the row and column values of the selected region
print(f"Selected ROI: Rows [{int(roi[1])}:{int(roi[1] + roi[3])}], Columns [{int(roi[0])}:{int(roi[0] + roi[2])}]")

# Draw a rectangle around the selected region
cv2.rectangle(background, (int(roi[0]), int(roi[1])), (int(roi[0] + roi[2]), int(roi[1] + roi[3])), (0, 255, 0), 2)

# Display the image with the rectangle
cv2.imshow('Selected Region', background)
cv2.waitKey(0)
cv2.destroyAllWindows()