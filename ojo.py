import cv2

# Load your image
image = cv2.imread('your_image_path.jpg')  # Replace 'your_image_path.jpg' with the actual path to your image

# Get screen width and height
screen_width, screen_height = 1366, 768  # Update with your screen resolution

# Resize the image to fit the screen
image = cv2.resize(image, (screen_width, screen_height))

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)

# Use the cv2.selectROI function to interactively select a region
roi = cv2.selectROI('Select ROI', image, fromCenter=False, showCrosshair=True)

# Print the row and column values of the selected region
print(f"Selected ROI: Rows [{int(roi[1])}:{int(roi[1] + roi[3])}], Columns [{int(roi[0])}:{int(roi[0] + roi[2])}]")

# Draw a rectangle around the selected region
cv2.rectangle(image, (int(roi[0]), int(roi[1])), (int(roi[0] + roi[2]), int(roi[1] + roi[3])), (0, 255, 0), 2)

# Display the image with the rectangle
cv2.imshow('Selected Region', image)
cv2.waitKey(0)
cv2.destroyAllWindows()