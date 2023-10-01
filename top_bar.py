from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageGrab
import styles
import sys


class TopBar(Canvas):
    def __init__(self, parent, image_canvas, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(width = 1920, height = 50, bg = styles.sub_color)
        self.place(x = 0, y = 0)
        self.framework_canvas = parent
        self.image_canvas = image_canvas
        self.create_buttons()

    def save_work(self):
        # Capture a screenshot of the self.image_canvas
        x = self.framework_canvas.winfo_rootx() + self.image_canvas.winfo_x()
        y = self.framework_canvas.winfo_rooty() + self.image_canvas.winfo_y()
        width = self.image_canvas.winfo_width()
        height = self.image_canvas.winfo_height()
        # Using ImageGrab.grab() provides a more straightforward way to obtain
        # the visual representation of the entire self.image_canvas,
        screenshot = ImageGrab.grab(bbox = (x, y, x + width, y + height))

        file_path = filedialog.asksaveasfilename(defaultextension = ".png",
                                                 filetypes = [("Portable Network Graphics", "*.png"),
                                                              ("JPEG", "*.jpg *.jpeg")])

        if file_path:
            screenshot.save(file_path)
            messagebox.showinfo("Work Saved", "The file has successfully been saved")

    def create_buttons(self):
        # Create and place icons within the sidebar canvas
        # Example:
        exit_button = Button(self,
                             text = "EXIT",
                             command = sys.exit,
                             width = 4,
                             height = 2,
                             bg = styles.sub_color,
                             )
        exit_button.place(x = 10, y = 7)

        app_label = Label(self, text = "FINEMARK", font = (styles.font, 25))
        app_label.place(x = 675, y = 10)

        save_button = Button(self,
                             text = "SAVE",
                             command = self.save_work,
                             width = 4,
                             height = 2,
                             bg = styles.sub_color,
                             )
        save_button.place(x = 1385, y = 7)
