import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Global variables
image_path = 'your_image_path.jpg'  # Replace with the actual path to your image
original_image = cv2.imread(image_path)
selected_roi = None
selection_start = None

# Callback function for mouse wheel events
def on_mouse_wheel(event):
    delta = -1 if event.delta < 0 else 1  # Determine scrolling direction
    canvas.yview_scroll(delta, "units")  # Scroll the canvas

# Callback function for mouse click and drag events
def on_mouse_press(event):
    global selected_roi, selection_start

    if selected_roi is None:
        selection_start = (event.x, event.y)
        selected_roi = canvas.create_rectangle(selection_start[0], selection_start[1], event.x, event.y, outline="red", width=2)

def on_mouse_drag(event):
    global selected_roi, selection_start

    if selected_roi is not None:
        canvas.coords(selected_roi, selection_start[0], selection_start[1], event.x, event.y)

def on_mouse_release(event):
    global selected_roi, selection_start

    if selected_roi is not None:
        # Convert canvas coordinates to image coordinates
        x1, y1 = canvas.canvasx(selection_start[0]), canvas.canvasy(selection_start[1])
        x2, y2 = canvas.canvasx(event.x), canvas.canvasy(event.y)

        # Display the rows and columns of the selected region
        print(f"Selected ROI: Rows [{int(y1)}:{int(y2)}], Columns [{int(x1)}:{int(x2)}]")

        # Reset selected_roi and selection_start
        canvas.delete(selected_roi)
        selected_roi = None
        selection_start = None

# Create a Tkinter window
root = tk.Tk()
root.title("Movable Image Window")

# Create a Canvas widget to display the image
canvas = tk.Canvas(root, width=original_image.shape[1], height=original_image.shape[0], scrollregion=(0, 0, original_image.shape[1], original_image.shape[0]))

# Bind the mouse wheel event to the canvas
canvas.bind("<MouseWheel>", on_mouse_wheel)

# Bind the mouse press, drag, and release events to draw the rectangle
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Create a PhotoImage object from the OpenCV image
image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
photo = ImageTk.PhotoImage(Image.fromarray(image_rgb))

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Pack the canvas into the window
canvas.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()