from utils import on_item_motion, on_item_press, on_canvas_click, on_canvas_motion
from tkinter import font
from tkinter import *
import tkinter.colorchooser as colorchooser
import time
import styles


class TextEditing(Canvas):
    def __init__(self, parent, child, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.rotation_angle = 0
        self.color_button = None
        self.text_item = None
        self.color_var = None
        self.main_canvas = parent
        self.sub_canvas = child

        self.config(width = 400, height = 275, bg = styles.sub_color)

        self.text_layout()
        self.place_forget()

        # Add drag functionality
        self.drag_data = {'x': 0, 'y': 0, 'last_update_time': time.time(), 'item': None}
        self.bind('<B1-Motion>', lambda event: on_canvas_motion(self, self.drag_data, event))
        self.bind('<Button-1>', lambda event: on_canvas_click(self, self.drag_data, event))

    # ------------------------------------------------------------------------------------------------------------ #
    def text_layout(self):
        text_label = Label(self,
                           text = "Text",
                           bg = styles.sub_color,
                           font = (styles.font, 16),
                           pady = 20,
                           padx = 20)
        text_label.place(x = 10, y = 10)

        text_input_entry = Entry(self, width = 25, font = (styles.font, 16))
        text_input_entry.place(x = 80, y = 25)

        # ------------------------------------------------------------------------------------------------------------ #
        font_label = Label(self,
                           text = "Font",
                           bg = styles.sub_color,
                           font = (styles.font, 16),
                           pady = 20,
                           padx = 20)
        font_label.place(x = 10, y = 60)

        # Font selection
        font_names = font.families()
        font_var = StringVar(value = font_names[0])

        font_menu = OptionMenu(self, font_var, *font_names)
        font_menu.place(x = 80, y = 80)

        # ------------------------------------------------------------------------------------------------------------ #
        size_label = Label(self,
                           text = "Font Size",
                           bg = styles.sub_color,
                           font = (styles.font, 16),
                           pady = 20,
                           padx = 20)
        size_label.place(x = 10, y = 110)

        # Font size selection
        min_size = 8
        max_size = 150
        step = 2
        size_values = list(range(min_size, max_size + 1, step))
        size_var = StringVar(value = str(size_values[0]))  # Convert size to string

        # '*' used for unpacking the values returned by the map() function. So it can be displayed.
        size_menu = OptionMenu(self, size_var, *map(str, size_values))
        size_menu.place(x = 120, y = 130)

        # ------------------------------------------------------------------------------------------------------------ #
        color_label = Label(self,
                            text = "Color",
                            bg = styles.sub_color,
                            font = (styles.font, 16),
                            pady = 20,
                            padx = 20)
        color_label.place(x = 10, y = 160)

        # Text color selection
        self.color_button = Button(self,
                                   text = "Select Color",
                                   command = self.open_color_picker)
        self.color_button.place(x = 80, y = 175)
        self.color_var = StringVar(value = "black")

        # ------------------------------------------------------------------------------------------------------------ #
        cancel_button = Button(self,
                               text = "Cancel",
                               width = 5,
                               font = (styles.font, 16),
                               command = self.cancel_item)
        cancel_button.place(x = 25, y = 230)

        apply_button = Button(self,
                              text = "Apply",
                              width = 5,
                              font = (styles.font, 16),
                              command = lambda: self.apply_changes(text_input_entry.get(),
                                                                   font_var.get(),
                                                                   int(size_var.get()),
                                                                   self.color_var.get()))
        apply_button.place(x = 300, y = 230)

    # ------------------------------------------------------------------------------------------------------------ #
    def cancel_item(self):
        if self.text_item:
            self.main_canvas.delete(self.text_item)
            self.text_item = None
        self.place_forget()

    def apply_changes(self, text, font_name, font_size, text_color):
        selected_font = font.Font(family = font_name, size = font_size)
        if self.text_item:
            self.sub_canvas.delete(self.text_item)  # Delete from sub canvas
        x, y = 500, 200  # Set initial position of the text item
        self.text_item = self.sub_canvas.create_text(x, y, text = text, font = selected_font, fill = text_color)
        self.sub_canvas.tag_bind(self.text_item, '<Button-1>', self.on_text_item_press)

    def open_color_picker(self):
        color = colorchooser.askcolor(title = "Select Color")
        if color[1]:
            selected_color = color[1]
            self.color_var.set(selected_color)
            self.color_button.config(text = selected_color)

    # ---------------------------------------------------------------------------------------------------------------- #
    # Draggable Functions for the Text and Text Editing Bar
    def on_text_item_motion(self, event):
        on_item_motion(self.sub_canvas, self.text_item, self.drag_data, event)

    def on_text_item_press(self, event):
        on_item_press(self.sub_canvas, self.text_item, self.drag_data, event)

    # ---------------------------------------------------------------------------------------------------------------- #
    # Draggable Functions for the EditingBar
    def on_bar_motion(self, event):
        on_canvas_motion(self.main_canvas, self.drag_data, event)

    def on_bar_press(self, event):
        on_canvas_click(self.main_canvas, self.drag_data, event)
