import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Global variable to store image path
image_path = 'your_image_path.jpg'  # Replace with the actual path to your image

# Callback function for mouse wheel events
def on_mouse_wheel(event):
    delta = -1 if event.delta < 0 else 1  # Determine scrolling direction
    canvas.yview_scroll(delta, "units")  # Scroll the canvas

# Load your image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Unable to load image from '{image_path}'")
    exit()

# Create a Tkinter window
root = tk.Tk()
root.title("Movable Image Window")

# Create a Canvas widget to display the image
canvas = tk.Canvas(root, width=image.shape[1], height=image.shape[0], scrollregion=(0, 0, image.shape[1], image.shape[0]))

# Bind the mouse wheel event to the canvas
canvas.bind("<MouseWheel>", on_mouse_wheel)

# Create a PhotoImage object from the OpenCV image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
photo = ImageTk.PhotoImage(Image.fromarray(image_rgb))

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Pack the canvas into the window
canvas.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()