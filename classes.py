import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.tooltip = None
    
    def show_tooltip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tooltip, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       font=("calibri", "8", "normal"))
        label.pack(ipadx=1)
        
    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = None
