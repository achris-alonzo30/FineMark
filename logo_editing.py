from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import on_item_motion, on_item_press, on_canvas_click, on_canvas_motion
import time
import styles


class LogoEditing(Canvas):
    def __init__(self, parent, child, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.rotation_angle = 0
        self.img_path_file = None
        self.logo_item = None
        self.logo_img = None
        self.logo_canvas = None
        self.main_canvas = parent
        self.sub_canvas = child

        self.config(width = 400, height = 200, bg = styles.sub_color)

        self.adjustment_dimension()
        self.place_forget()

        # Add drag functionality
        self.drag_data = {'x': 0, 'y': 0, 'last_update_time': time.time(), 'item': None}
        self.bind('<B1-Motion>', lambda event: on_canvas_motion(self, self.drag_data, event))
        self.bind('<Button-1>', lambda event: on_canvas_click(self, self.drag_data, event))

    # ------------------------------------------------------------------------------------------------------------ #
    def open_img_file_path(self):
        self.img_path_file = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                                        filetypes = (("JPEG files", "*.jpg"),
                                                                     ("PNG files", "*.png"),
                                                                     ("All files", "*.*")))
        if self.img_path_file:
            print(f"File selected: {self.img_path_file}")
            self.open_img_file(self.img_path_file)

    def open_img_file(self, img_file_path):
        self.img_path_file = img_file_path
        logo_image = Image.open(img_file_path).convert("RGBA")
        sub_canvas_width = self.sub_canvas.winfo_width()
        sub_canvas_height = self.sub_canvas.winfo_height()

        # Resize the logo image if it's too large for the sub canvas
        if logo_image.width > sub_canvas_width or logo_image.height > sub_canvas_height:
            logo_image = logo_image.resize((sub_canvas_width, sub_canvas_height))

        self.logo_img = ImageTk.PhotoImage(logo_image)
        self.logo_item = self.sub_canvas.create_image(sub_canvas_width // 2,
                                                      sub_canvas_height // 2,
                                                      anchor = "center",
                                                      image = self.logo_img)

        # Add binding for draggable functionality
        self.sub_canvas.tag_bind(self.logo_item, "<Button-1>", self.on_logo_item_press)

    # ------------------------------------------------------------------------------------------------------------ #
    def adjustment_dimension(self):
        image_label = Label(self,
                            text = "Logo Editing",
                            bg = styles.sub_color,
                            font = (styles.font, 16),
                            pady = 10,
                            padx = 10)
        image_label.place(x = 130, y = 10)

        height_label = Label(self,
                             text = "Height Adjustment",
                             bg = styles.sub_color,
                             font = (styles.font, 16),
                             pady = 20,
                             padx = 20)
        height_label.place(x = 10, y = 50)

        new_height = Entry(self, width = 10, font = (styles.font, 16))
        new_height.place(x = 200, y = 65)

        # ------------------------------------------------------------------------------------------------------------ #
        width_label = Label(self,
                            text = "Width Adjustment",
                            bg = styles.sub_color,
                            font = (styles.font, 16),
                            pady = 20,
                            padx = 20)
        width_label.place(x = 10, y = 90)

        new_width = Entry(self, width = 10, font = (styles.font, 16))
        new_width.place(x = 200, y = 105)

        # ------------------------------------------------------------------------------------------------------------ #
        cancel_button = Button(self,
                               text = "Cancel",
                               width = 5,
                               font = (styles.font, 16),
                               command = "")
        cancel_button.place(x = 25, y = 160)

        # Apply button
        apply_button = Button(self,
                              text = "Apply",
                              width = 5,
                              font = (styles.font, 16),
                              command = "")
        apply_button.place(x = 300, y = 160)

    # ------------------------------------------------------------------------------------------------------------ #

    def cancel_item(self):
        # Delete the logo image
        self.main_canvas.delete(self.logo_item)

        # Reset the image path file
        self.img_path_file = None

        # Hide the logo_editing bar
        self.place_forget()

    # ---------------------------------------------------------------------------------------------------------------- #
    # Resizing Functions for the Logo
    def apply_changes(self, new_height, new_width):
        new_height = int(new_height)
        new_width = int(new_width)

        resized_image = self.resize_logo(self.img_path_file, new_height, new_width)
        self.update_logo_image(resized_image)

    @staticmethod
    def resize_logo(image_path, new_height, new_width):
        # Open the image using PIL
        image = Image.open(image_path)

        # Resize the image
        resized_photo = image.resize((new_width, new_height))

        return resized_photo

    def update_logo_image(self, image):
        self.logo_img = ImageTk.PhotoImage(image)
        self.sub_canvas.itemconfig(self.logo_item, image = self.logo_img)

    # ---------------------------------------------------------------------------------------------------------------- #
    # Draggable Functions for the Logo
    def on_logo_item_motion(self, event):
        on_item_motion(self.sub_canvas, self.logo_item, self.drag_data, event)

    def on_logo_item_press(self, event):
        on_item_press(self.sub_canvas, self.logo_item, self.drag_data, event)

    # ---------------------------------------------------------------------------------------------------------------- #
    # Draggable Functions for the EditingBar
    def on_bar_motion(self, event):
        on_canvas_motion(self.main_canvas, self.drag_data, event)

    def on_bar_press(self, event):
        on_canvas_click(self.main_canvas, self.drag_data, event)
