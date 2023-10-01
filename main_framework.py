import styles
from top_bar import TopBar
from dock_bar import DockBar
from image_editing import ImageEditing
from text_editing import TextEditing
from logo_editing import LogoEditing
from tkinter import *


class MainFramework:
    def __init__(self):
        self.root = Tk()
        self.root.title("Workspace")
        self.root.config(bg=styles.main_color)
        self.framework_canvas = Canvas(self.root, width=1560, height=1080, bg=styles.main_color)
        self.framework_canvas.pack(fill=BOTH, expand=True)
        self.photo_img = None

        self.image_canvas = Canvas(self.framework_canvas,
                                   width=500, height=600,
                                   bg=styles.sub_color,
                                   borderwidth=1)

        self.image_canvas_id = self.framework_canvas.create_window(500, 100, anchor=NW, window=self.image_canvas)

        DockBar(self.framework_canvas, self.image_canvas)
        ImageEditing(self.framework_canvas, self.image_canvas)
        TextEditing(self.framework_canvas, self.image_canvas)
        LogoEditing(self.framework_canvas, self.image_canvas)
        TopBar(self.framework_canvas, self.image_canvas)

        self.root.mainloop()


if __name__ == "__main__":
    main_framework = MainFramework()
