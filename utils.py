import time


def on_item_press(canvas, item, drag_data, event):
    # Capture the starting position of the mouse
    drag_data['x'] = event.x
    drag_data['y'] = event.y

    # Update the currently selected item
    drag_data['item'] = item

    # Bind the motion event to handle dragging
    canvas.tag_bind(item, "<B1-Motion>",
                    lambda event, drag_data=drag_data, canvas=canvas, item=item: on_item_motion(canvas, item, drag_data,
                                                                                                event))


def on_item_motion(canvas, item, drag_data, event):
    # Calculate the distance moved by the mouse
    # event.x and y are the new coordinates
    # drag_data['x'] and drag_data['y'] are the starting coordinates
    dx = event.x - drag_data['x']
    dy = event.y - drag_data['y']

    # Move the item based on the distance moved by the mouse
    canvas.move(item, dx, dy)

    # Update the starting position for the next drag motion event
    drag_data['x'] = event.x
    drag_data['y'] = event.y


# -------------------------------------------------------------------------------------------------------------------- #

def on_canvas_click(canvas, drag_data, event):
    # Capture the starting position of the mouse
    drag_data['x'] = event.x
    drag_data['y'] = event.y

    # Bind the motion event to handle dragging
    canvas.bind('<B1-Motion>',
                lambda event, drag_data=drag_data, canvas=canvas: on_canvas_motion(canvas, drag_data, event))


def on_canvas_motion(canvas, drag_data, event):
    # Calculate the distance moved by the mouse
    dx = event.x - drag_data['x']
    dy = event.y - drag_data['y']

    # Get the current time
    current_time = time.time()

    # Update the position of the canvas item only if a certain amount of time has passed since the last update
    if current_time - drag_data['last_update_time'] > 0.015:  # Adjust this value as needed for smoother movement
        # Move the canvas item based on the distance moved by the mouse
        canvas.place_configure(x = canvas.winfo_x() + dx, y = canvas.winfo_y() + dy)

        # Update the last update time
        drag_data['last_update_time'] = current_time

    # Update the starting position for the next drag motion event
    drag_data['x'] = event.x
    drag_data['y'] = event.y
