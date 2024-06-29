import threading
import sys
import time
import tkinter as tk
import keyboard

class InterpDMM:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=sys.argv[2], height=sys.argv[3], background='#FFFFFF')
        self.canvas.pack()
        self.commands = {
            'PIZZA': self.draw_graphics,
            'BURGER': self.get_input,
            'SALAD': self.display_message,
            'SUSHI': self.ret,
            'PASTA': self.end_if,
            'PASTA': self.check_end_if,
            'TACO': self.set_variable,
            'STEAK': self.check_variable,
            'RAMEN': self.math_var,
            'SANDWICH': self.create_label,
            'CURRY': self.jump_to_label,
            'CHICKEN': self.clear_screen,
            'COOKIE': self.checkKey,
            'CHEESE': self.DMM_wait
        }
        self.variables = {}
        self.if_block = False
        self.labels = {}

    def interpret(self, code):
        self.current_line = 0
        self.return_line = 0;
        lines = code.split('\n')
        while self.current_line < len(lines):
            line = lines[self.current_line]
            if line:
                parts = line.split(' ')
                command = parts[0]
                args = parts[1:]

                # Check for variable references and replace them with values
                args_with_values = []
                for arg in args:
                    if arg.startswith('$'):
                        arg_name = arg[1:]
                        if arg_name in self.variables:
                            args_with_values.append(str(self.variables[arg_name]))
                        else:
                            print(f"Variable '{arg_name}' not found")
                    else:
                        args_with_values.append(arg)

                if command in self.commands:
                    self.commands[command](*args_with_values)
                else:
                    print(f"Invalid command: {command}")
            self.current_line += 1

    def interpret_ifs(self, code):
        lines = code.split(',')
        for line in lines:
            if line:
                parts = line.split(' ')
                command = parts[0]
                if command in self.commands:
                    self.commands[command](*parts[1:])
                else:
                    print(f"Invalid command: {command}")

    def run_interpreter(self, code):
        self.interpret(code)

    def run(self, code):
        interpreter_thread = threading.Thread(target=self.run_interpreter, args=(code,))
        interpreter_thread.start()
        self.root.mainloop()

    def clear_screen(self, color):
        self.canvas.delete('all')  # Delete all items on the canvas
        self.canvas.configure(background=color)

    def draw_graphics(self, x, y, width, height, outline, thickness, fill, mode):
        #print(f"Drawing rectangle at ({x}, {y}) with width {width} and height {height}")
        if mode == "SQUARE":
            self.canvas.create_rectangle(float(x), float(y), float(x) + float(width), float(y) + float(height), outline=outline, width = thickness)
        if mode == "CIRCLE":
            self.canvas.create_oval(float(x), float(y), float(x) + float(width), float(y) + float(height), outline=outline, width = thickness)
        if mode == "LINE":
            self.canvas.create_line(float(x), float(y), float(width), float(height), width = thickness, fill=fill)
        if mode == "FILLED-SQUARE":
            self.canvas.create_rectangle(float(x), float(y), float(x) + float(width), float(y) + float(height), outline=outline, width = thickness, fill=fill)
        if mode == "FILLED-CIRCLE":
            self.canvas.create_oval(float(x), float(y), float(x) + float(width), float(y) + float(height), outline=outline, width = thickness, fill=fill)

    #def draw_circle(self, x, y, radius):
    #    #print(f"Drawing circle at ({x}, {y}) with radius {radius}")
    #    pass

    #def draw_line(self, x1, y1, x2, y2):
    #    print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

    #def move_cursor(self, x, y):
    #    print(f"Moving cursor to ({x}, {y})")

    def get_input(self, var_name, input_type):
        #user_input = input("What to do next: ")
        user_input = input()

        try:
            if input_type == 'TEXT':
                self.variables[var_name] = user_input
            if input_type == 'NUM':
                self.variables[var_name] = float(user_input)
        except:
            print("Try again.")
            self.get_input(var_name, input_type)
        #print(f"User input: {user_input}")

    def display_message(self, *message):
        print(" ".join(message))

    def condition_check(self, condition, *code_block):
        if 'input' in self.variables and self.variables['input'] == condition:
            self.if_block = True
            sub_code = " ".join(code_block)
            self.interpret_ifs(sub_code)

    def check_end_if(self):
        if 'ENDIF' in self.variables and self.if_block:
            self.if_block = False
            del self.variables['ENDIF']

    def create_label(self, label_name):
        self.labels[label_name] = self.current_line

    def jump_to_label(self, label_name, mode):
        if mode == "LABEL":
            if label_name in self.labels:
                self.return_line = self.current_line+1
                self.current_line = self.labels[label_name]
        if mode == "LINE":
            self.return_line = self.current_line+1
            self.current_line = int(label_name)-2

    def end_if(self):
        self.variables['ENDIF'] = True

    def set_variable(self, var_name, value, input_type):
        if input_type == 'TEXT':
            self.variables[var_name] = value
        if input_type == 'NUM':
            self.variables[var_name] = float(value)

    def math_var(self, var_name, varToMath, mathType):
        if mathType == "ADD":
            self.variables[var_name] += float(varToMath)
        if mathType == "SUB":
            self.variables[var_name] -= float(varToMath)
        if mathType == "MUL":
            self.variables[var_name] *= float(varToMath)
        if mathType == "DIV":
            self.variables[var_name] /= float(varToMath)
        if mathType == "SET":
            self.variables[var_name] = float(varToMath)

    def ret(self):
        self.current_line = self.return_line

    def check_variable(self, var_name, var_type, condition, *code_block):
        if var_type == 'TEXT':
            if var_name in self.variables and self.variables[var_name] == condition:
                self.if_block = True
                sub_code = " ".join(code_block)
                self.interpret_ifs(sub_code)
        if var_type == 'NUM':
            if var_name in self.variables and self.variables[var_name] == float(condition):
                self.if_block = True
                sub_code = " ".join(code_block)
                self.interpret_ifs(sub_code)

    def checkKey(self, key, *code_block):
        if keyboard.is_pressed(key):
            self.if_block = True
            sub_code = " ".join(code_block)
            self.interpret_ifs(sub_code)

    def DMM_wait(self, amount):
        time.sleep(float(amount))

interpreter = InterpDMM()
# idk if self is a good idea
if ".dmm" in sys.argv[1]:
    with open(sys.argv[1], 'r') as file:
        code = file.read()
        interpreter.run(code)

else:
    print("File not found or has wrong extension. Try adding .dmm to the end of your file.\n Quiting in 3 seconds...")
    time.sleep(3)
