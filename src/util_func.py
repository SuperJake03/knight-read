"""
Handles mouse logic on Table of Contents canvas for Window/Mac/Linux
"""

from tkinter import Text


def on_mouse_scroll_win_mac(canvas, event):
    if isinstance(event.widget, Text):
        return
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def on_mouse_scroll_linux(canvas, event):
    if isinstance(event.widget, Text):
        return
    if event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")
