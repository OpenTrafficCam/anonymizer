# TODO: #24 Create a simple gui

# import tkinter as tk

# window = tk.Tk()
# button_input_pics_folder = tk.Button(text="Select folder for input pics")
# button_input_pics_folder.pack
# entry_input_pics_folder = tk.Entry()
# button_output_pics_folder = tk.Button(text="Select folder for output pics")
# button_output_pics_folder.pack
# button_output_weights_folder = tk.Button(text="Select folder for output weights")
# button_output_weights_folder.pack
# window.mainloop()

import tkinter as tk
from tkinter import filedialog


def fun1(text="test1"):
    print(text)


def drucken(wort="tesfa"):
    print(wort)


class Mainwindow(tk.Tk):
    def __init__(
        self,
        parent,
        button_count,
        button_text=[],
        geometry=None,
        tuple_func_arg=[],
    ):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.button_number = button_count
        self.button_text = button_text
        self.functions = tuple_func_arg
        self.geometry(geometry)
        self.input_folder = None
        self.output_folder = None

        self.grid_columnconfigure(0, weight=0)
        self.mainWidgets_buttons()

    def input_directory(self):

        # call back functions have to be global

        self.input_folder = filedialog.askdirectory()

    def output_directory(self):

        # call back functions have to be global

        self.output_folder = filedialog.askdirectory()

    def mainWidgets_buttons(self):

        self.button = tk.Button(
            self,
            text="Chose folder",
            command=lambda: self.input_directory(),
        ).grid(row=0, padx=2, pady=2, sticky="nsew")

        self.button = tk.Button(
            self,
            text="Output folder",
            command=lambda: self.output_directory(),
        ).grid(row=1, padx=2, pady=2, sticky="nsew")

        for number in range(self.button_number):

            text = (
                "No text assigned"
                if number >= len(self.button_text)
                else self.button_text[number]
            )

            try:
                func = self.functions[number][0]
                arg = self.functions[number][1]
                command = lambda x=arg: func(x)
            except:
                command = lambda: print("No function assigned")

            self.number = tk.Button(
                self,
                text=text,
                command=command,
            ).grid(row=number + 2, padx=2, pady=2, sticky="nsew")

            self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":

    app = Mainwindow(
        None,
        button_count=5,
        button_text=["button1", "button2"],
        tuple_func_arg=[(fun1, "str"), (drucken, "trasdjflka")],
    )
    app.mainloop()
