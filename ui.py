from tkinter import *
from tkinter import ttk


class Interface:
    def __init__(self, root):
        self.window = root
        self.window.title("Unit Converter")
        self.window.config(padx=20, pady=40)

        frame_width = 200
        frame_height = 200
        self.conversion_outcome = 1
        self.unit_options = ["Millimetre", "Centimetre", "Metre", "Kilometer",  "Mile", "Yard",
                             "Foot", "Inch"]
        self.measurements = {"Millimetre": 0, "Centimetre": 0, "Metre": 0, "Kilometer": 0,  "Mile": 0, "Yard": 0,
                             "Foot": 0, "Inch": 0}

        self.frame_top = Frame(self.window, width=800, height=300, relief=GROOVE)
        self.frame_top.pack()

        # unit input
        self.unit_input = Entry(self.frame_top, width=20)
        self.unit_input.insert(0, "1")
        self.unit_input.grid(row=1, column=0)

        # drop down to select unit type for the input
        self.in_unit_type_value = StringVar(self.frame_top)
        self.in_unit_type_value.set(self.unit_options[0])
        self.in_unit_type_options = self.unit_options
        self.in_Unit_type_dropdown = OptionMenu(self.frame_top, self.in_unit_type_value, *self.in_unit_type_options,
                                                command=self.update_unit_type_in)
        self.in_Unit_type_dropdown.grid(row=2, column=0)

        # unit output
        self.unit_out = Label(self.frame_top, width=20, text=self.conversion_outcome, bg="white")
        self.unit_out.grid(row=1, column=2)

        # drop down to select unit type for the output
        self.out_unit_type_value = StringVar(self.frame_top)
        self.out_unit_type_value.set(self.unit_options[1])
        self.out_unit_type_options = self.unit_options
        self.out_Unit_type_dropdown = OptionMenu(self.frame_top, self.out_unit_type_value, *self.out_unit_type_options,
                                                 command=self.update_unit_type_out)
        self.out_Unit_type_dropdown.grid(row=2, column=2)

        # add an = inbetween input and output
        self.equal_label = Label(self.frame_top, text="=")
        self.equal_label.grid(row=1, column=1)

        # calc button
        calc_button = Button(self.window, text="Calculate", width=41, command=self.math)
        calc_button.pack()

    def update_unit_type_in(self, unit_type):
        result = self.calc(self.in_unit_type_value.get(), self.out_unit_type_value.get(), float(self.unit_input.get()))
        self.unit_out.config(text=result)
    def update_unit_type_out(self, unit_type):
        result = self.calc(self.in_unit_type_value.get(), self.out_unit_type_value.get(), float(self.unit_input.get()))
        self.unit_out.config(text=result)
    def calc(self, unit_in, unit_out, value):
        if unit_in == "Millimetre":
            self.measurements["Centimetre"] = value / 10
            self.measurements["Metre"] = value / 1000
            self.measurements["Kilometer"] = value / 1000000
            self.measurements["Mile"] = value / 1609344
            self.measurements["Yard"] = value / 914
            self.measurements["Feet"] = value / 304.8
            self.measurements["Inch"] = value / 25.4

        elif unit_in == "Centimetre":
            self.measurements["Millimetre"] = value * 10
            self.measurements["Metre"] = value / 100
            self.measurements["Kilometer"] = value / 100000
            self.measurements["Mile"] = value / 160934.4
            self.measurements["Yard"] = value / 91.44
            self.measurements["Feet"] = value / 30.48
            self.measurements["Inch"] = value / 2.54

        elif unit_in == "Metre":
            self.measurements["Millimetre"] = value * 1000
            self.measurements["Centimetre"] = value * 100
            self.measurements["Kilometer"] = value / 1000
            self.measurements["Mile"] = value / 1609.344
            self.measurements["Yard"] = value * 1.0936
            self.measurements["Feet"] = value * 3.2808
            self.measurements["Inch"] = value * 39.3701

        elif unit_in == "Kilometer":
            self.measurements["Millimetre"] = value * 1000000
            self.measurements["Centimetre"] = value * 100000
            self.measurements["Metre"] = value * 1000
            self.measurements["Mile"] = value / 1.609344
            self.measurements["Yard"] = value * 1094
            self.measurements["Feet"] = value * 3280.84
            self.measurements["Inch"] = value * 39370.1

        elif unit_in == "Mile":
            self.measurements["Millimetre"] = value * 1609344
            self.measurements["Centimetre"] = value * 160934.4
            self.measurements["Metre"] = value * 1609.344
            self.measurements["Kilometer"] = value * 1.609344
            self.measurements["Yard"] = value * 1760
            self.measurements["Feet"] = value * 5280
            self.measurements["Inch"] = value * 63360

        elif unit_in == "Yard":
            self.measurements["Millimetre"] = value * 914
            self.measurements["Centimetre"] = value * 91.44
            self.measurements["Metre"] = value / 1.0936
            self.measurements["Kilometer"] = value / 1094
            self.measurements["Mile"] = value / 1760
            self.measurements["Feet"] = value * 3
            self.measurements["Inch"] = value * 36

        elif unit_in == "Feet":
            self.measurements["Millimetre"] = value * 304.8
            self.measurements["Centimetre"] = value * 30.48
            self.measurements["Metre"] = value / 3.2808
            self.measurements["Kilometer"] = value / 3280.84
            self.measurements["Mile"] = value / 5280
            self.measurements["Yard"] = value / 3
            self.measurements["Inch"] = value * 12

        elif unit_in == "Inch":
            self.measurements["Millimetre"] = value * 25.4
            self.measurements["Centimetre"] = value * 2.54
            self.measurements["Metre"] = value / 39.3701
            self.measurements["Kilometer"] = value / 39370.1
            self.measurements["Mile"] = value / 63360
            self.measurements["Yard"] = value / 36
            self.measurements["Feet"] = value / 12

        return self.measurements[unit_out]

    def math(self):
        result = self.calc(self.in_unit_type_value.get(), self.out_unit_type_value.get(), float(self.unit_input.get()))
        self.unit_out.config(text=result)
