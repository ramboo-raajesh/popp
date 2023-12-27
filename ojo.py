import cv2

# Global variables to store window position
window_position = (0, 0)

# Callback function for mouse events
def move_window(event, x, y, flags, param):
    global window_position

    if event == cv2.EVENT_MOUSEWHEEL:
        # Get the mouse wheel delta (positive for scrolling up, negative for scrolling down)
        delta = flags

        # Update the window position based on the mouse wheel delta
        window_position = (window_position[0], window_position[1] + delta)

        # Move the window to the updated position
        cv2.moveWindow('Image', window_position[0], window_position[1])

# Load your image
image = cv2.imread('your_image_path.jpg')  # Replace 'your_image_path.jpg' with the actual path to your image

# Set an initial window size and position
initial_width, initial_height = 800, 600
window_position = (0, 0)

# Create a non-resizable window
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', initial_width, initial_height)
cv2.moveWindow('Image', window_position[0], window_position[1])

# Set the mouse callback
cv2.setMouseCallback('Image', move_window)

# Display the image
cv2.imshow('Image', image)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()