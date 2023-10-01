from tkinter import *
from image_editing import ImageEditing
from text_editing import TextEditing
from logo_editing import LogoEditing
import styles


class DockBar(Canvas):
    def __init__(self, parent, child, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.child = child

        # Dimensions of the sidebar
        self.config(width = 375, height = 40, bg = styles.sub_color)
        self.place(x = 550, y = 730)

        # Importing Canvas for Editing Text and Logo Classes
        self.text_editing_canvas = TextEditing(self.parent, self.child)
        self.logo_editing_canvas = LogoEditing(self.parent, self.child)
        self.image_editing_canvas = ImageEditing(self.parent, self.child)

        # Call a method to create icons within the sidebar canvas
        self.create_icons()

    # ---------------------------------------------------------------------------------------------------------------- #
    # Show/Hide Canvas Functions
    def show_text_editing(self):
        self.text_editing_canvas.place(x = 1020, y = 100)

    def show_logo_editing(self):
        self.logo_editing_canvas.open_img_file_path()
        self.logo_editing_canvas.place(x = 1020, y = 400)

    def show_image_editing(self):
        self.image_editing_canvas.open_img_file_path()
        self.image_editing_canvas.place(x = 50, y = 100)

    # ---------------------------------------------------------------------------------------------------------------- #
    # Sidebar Canvas Functions
    def create_icons(self):
        x = 15
        y = 10
        offset = 130  # Vertical spacing between labels

        # Create and place icons within the sidebar canvas
        add_image = Button(self,
                           text = "Add Image",
                           borderwidth = 0,
                           highlightthickness = 0)
        add_image.config(padx = 5, pady = 5)
        add_image.place(x = x, y = y)
        add_image.bind("<Button-1>", lambda event: self.show_image_editing())

        add_logo = Button(self,
                          text = "Add Logo",
                          borderwidth = 0,
                          highlightthickness = 0)
        add_logo.config(padx = 5, pady = 5)
        add_logo.place(x = x + offset, y = y)
        add_logo.bind("<Button-1>", lambda event: self.show_logo_editing())

        add_text = Button(self,
                          text = "Add Text",
                          borderwidth = 0,
                          highlightthickness = 0)
        add_text.config(padx = 5, pady = 5)
        add_text.place(x = x + offset * 2, y = y)
        add_text.bind("<Button-1>", lambda event: self.show_text_editing())
