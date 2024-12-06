####################################################################################
# Yaroslav Trach, Kevin Wehrle, Aidan Sheehy
# AMERICAN SPY BOMB DEFUSAL SYSTEM: Casino
# Professor K
# Last Modified: 12/06/2024
####################################################################################


# MARK: - Import all the required libraries
import random
import time
from tkinter import *
from tkinter import Toplevel, Entry, messagebox
import tkinter
from threading import Thread
from time import sleep
from random import randint
import board
from adafruit_ht16k33.segments import Seg7x4
from digitalio import DigitalInOut, Direction, Pull
from adafruit_matrixkeypad import Matrix_Keypad


# MARK: - CONSTANTS
# the bomb's initial countdown timer value (seconds)
COUNTDOWN = 300
# the maximum passphrase length
MAX_PASS_LEN = 14
# does the asterisk (*) clear the passphrase?
STAR_CLEARS_PASS = True

TOGGLES_GUI_UPDATED = False
# generates random code
BINARY_CODE = format(random.randrange(1,15), "04b")


# MARK: - MAIN GLOBAL FUNCTION FOR CONSTANT UI UPDATES
def check_class():
    togglesUpdated = False
   
    # Check if Toggles Defused
    if not toggles._running:
        gui.update_toggles_color("green")
        if not wires._running:
            gui.update_wire_circles(wires._value)
        

    # Check if Toggles and Wires Defused
    if not toggles._running and not wires._running:
        
        # Check if all Toggles green
        if wires._value == "11111":
            
            if not hasattr(gui, 'code_entry_shown'):
                
                # Mark Button as activated (green)
                button._defused = True
                
                if button._code_window and button._code_display:
                    button.update_code_display()

    # Show failure screen if time is up
    if (timer._value == 0):
        print("Tmer 0")
        gui.show_failure_screen()
    
    
    # check again after 100ms
    gui.after(100, check_class)






# MARK: - MAIN CLASSES

# the LCD display "GUI"
class Lcd(Frame):
    
    # MARK: INITIALIZATION
    def __init__(self, window):
        super().__init__(window, bg="black")
        self.window = window
        self._ltimer = None
        self._lkeypad = None
        self._lwires = None
        self._lbutton = None
        self._ltoggles = None
        self._lpause = None
        self._lquit = None
        self.pack(fill=BOTH, expand=True)
       
        self.show_welcome()

    # MARK: MAIN FUNCTIONS
    def show_welcome(self):
        self.window.after(500, self.window.attributes, '-fullscreen', 'True')
        for widget in self.winfo_children():
            widget.destroy()
        welcome_label = Label(self, text="Welcome to the Bomb Defusal System",
                              font=("Courier New", 24), bg="black", fg="white")
        welcome_label.pack(pady=20)
        get_started_button = Button(self, text="Click to Get Started",
                                    font=("Courier New", 18),
                                    command=self.show_difficulty_selection,
                                    bg="red", fg="white")
        get_started_button.pack(pady=20)
   
    def show_difficulty_selection(self):
        for widget in self.winfo_children():
            widget.destroy()
       
        # Difficulty selection elements
        difficulty_label = Label(self, text="Select Difficulty Level",
                                 font=("Courier New", 24), bg="black", fg="white")
        difficulty_label.pack(pady=20)

        # Buttons for each difficulty level
        easy_button = Button(self, text="Easy", font=("Courier New", 18),
                             command=lambda: self.show_danger_screen("Easy"),
                             bg="green", fg="white")
        easy_button.pack(pady=10)

        medium_button = Button(self, text="Medium", font=("Courier New", 18),
                               command=lambda: self.show_danger_screen("Medium"),
                               bg="orange", fg="white")
        medium_button.pack(pady=10)

        hard_button = Button(self, text="Hard", font=("Courier New", 18),
                             command=lambda: self.show_danger_screen("Hard"),
                             bg="red", fg="white")
        hard_button.pack(pady=10)
   
    def show_danger_screen(self, difficulty, togglesColor="gray"):
        
        # Set time based on difficulty
        global COUNTDOWN, timer
        if difficulty == "Easy":
            COUNTDOWN = 10  # 6 minutes
        elif difficulty == "Medium": 
            COUNTDOWN = 240  # 4 minutes
        elif difficulty == "Hard":
            COUNTDOWN = 120  # 2 minutes
        
        timer = Timer(COUNTDOWN, display)
        self.setTimer(timer)
        timer.start()
        
        
        # Transition to the Danger screen
        for widget in self.winfo_children():
            widget.destroy()

        # Set the background color to black
        self.config(bg="black")
       
        self.difficulty = difficulty

        # Add the "Danger" title
        danger_label = Label(self, text="DANGER", font=("Courier New", 48),
                             bg="black", fg="red")
        danger_label.pack(pady=20)

        # Create the three sections with white separators
        top_section = Frame(self, bg="black")
        top_section.pack(fill=X, padx=20)

        middle_section = Frame(self, bg="black")
        middle_section.pack(fill=X, padx=20)

        bottom_section = Frame(self, bg="black")
        bottom_section.pack(fill=X, padx=20)


        Label(middle_section, text="", font=("Courier New", 18), bg="black", fg="white").pack(pady=5)
        Label(bottom_section, text="", font=("Courier New", 18), bg="black", fg="white").pack(pady=5)
       
       
        # Top leading section with four circles representing switch states
        circle_frame = Frame(top_section, bg="black")
        circle_frame.pack(side=LEFT, padx=10)
       
        # Circle states: gray (off), green (on)
        self.circle_labels = []
        for _ in range(4):
            circle_label = Label(circle_frame, width=4, height=2, bg=togglesColor, relief="solid")
            circle_label.pack(side=LEFT, padx=5)
            self.circle_labels.append(circle_label)
            
            
        
        self.update_toggles_color(togglesColor)
       
           
        # Add the horizontal separator (a white line)
        separator = Frame(self, bg="white", height=2, width=500)
        separator.pack(pady=20)

        # Add five circles for the wire states
        wire_frame = Frame(self, bg="black")
        wire_frame.pack(pady=20)

        self.wire_circle_labels = []
        for _ in range(5):
            wire_circle_label = Label(wire_frame, width=4, height=2, bg="gray", relief="solid")
            wire_circle_label.pack(side=LEFT, padx=5)
            self.wire_circle_labels.append(wire_circle_label)
            
        serial_frame = Frame(self, bg="black")
        serial_frame.pack(side=BOTTOM, pady=20)
    
        serial_label = Label(serial_frame, 
                            text=f"Serial Number: {self.serial_number()}", 
                            font=("Courier New", 14),
                            bg="black", 
                            fg="white")
        serial_label.pack()
            
    def show_failure_screen(self):
        
        # Clear existing widgets
        for widget in self.winfo_children():
            widget.destroy()
            
        # Make window fullscreen
        self.window.attributes('-fullscreen', True)
            
        # Set red background
        self.config(bg="red")
        
        # Create main container
        main_frame = Frame(self, bg="red")
        main_frame.pack(fill=BOTH, expand=True)
        
        # Add "YOU FAILED!" text
        fail_label = Label(main_frame, text="YOU FAILED!", 
                          font=("Courier New", 72, "bold"),
                          bg="red", fg="white")
        fail_label.pack(pady=50)
        
        # Create canvas for circles
        canvas = Canvas(main_frame, bg="red", highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        
        # Add decorative yellow explosion circles
        for _ in range(20):
            x = random.randint(0, self.window.winfo_screenwidth())
            y = random.randint(0, self.window.winfo_screenheight())
            size = random.randint(30, 100)
            canvas.create_oval(x, y, x+size, y+size, fill="yellow", outline="yellow")
    
    def update_toggles_color(self, togglesColor):
        # Update each circle's background color with the specified color
        for circle in self.circle_labels:
            circle.config(bg=togglesColor)
        
    def update_wire_circles(self, wire_state):
        # Update each wire circle based on the wire state
        for idx, state in enumerate(wire_state):
            color = "green" if state == "1" else "gray"
            self.wire_circle_labels[idx].config(bg=color)
    
    def show_success_screen(self):
        # Clear existing widgets
        for widget in self.winfo_children():
            widget.destroy()
            
        # Make window fullscreen
        self.window.attributes('-fullscreen', True)
            
        # Set green background
        self.config(bg="green")
        
        # Create main container
        main_frame = Frame(self, bg="green")
        main_frame.pack(fill=BOTH, expand=True)
        
        # Add "BOMB DEFUSED!" text
        success_label = Label(main_frame, text="BOMB DEFUSED!", 
                          font=("Courier New", 72, "bold"),
                          bg="green", fg="white")
        success_label.pack(pady=50)
        
        # Add message to P.K.
        message_label = Label(main_frame, text="Have a good day P.K.!", 
                           font=("Courier New", 36),
                           bg="green", fg="white")
        message_label.pack(pady=30)    
    
    def serial_number(self):
        print(BINARY_CODE)
        serial_format = "x00xx1xx0"  # format for randomly generated serial number
        serial_number = ""
        code = int(BINARY_CODE, 2)  # Gets the random binary code
        print(code)
        for i in serial_format:
            if i == "x":
                serial_number += chr(random.randint(97, 122)).upper()
            elif i == "0":
                serial_number += str(random.randint(1, 9))
            elif i == "1":
                serial_number += str(code)

        return serial_number
    
    
    # MARK: ---- LEGACY CODE: sets up the LCD "GUI" ----
    def start_main_interface(self, difficulty):
        global COUNTDOWN
        if difficulty == "Easy":
            COUNTDOWN = 300
        elif difficulty == "Medium":
            COUNTDOWN = 180
        elif difficulty == "Hard":
            COUNTDOWN = 120

        self.show_main_interface()

    def show_main_interface(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.window.after(500, self.window.attributes, '-fullscreen', 'True')
        self.setup()

    def setup(self):
        # set column weights
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.pack(fill=BOTH, expand=True)
        # the timer
        self._ltimer = Label(self, bg="black", fg="white", font=("Courier New", 24), text="Time left: ")
        self._ltimer.grid(row=0, column=0, columnspan=2, sticky=W)
        # the keypad passphrase
        self._lkeypad = Label(self, bg="black", fg="white", font=("Courier New", 24), text="Combination: ")
        self._lkeypad.grid(row=1, column=0, columnspan=2, sticky=W)
        # the jumper wires status
        self._lwires = Label(self, bg="black", fg="white", font=("Courier New", 24), text="Wires: ")
        self._lwires.grid(row=2, column=0, columnspan=2, sticky=W)
        # the pushbutton status
        self._lbutton = Label(self, bg="black", fg="white", font=("Courier New", 24), text="Button: ")
        self._lbutton.grid(row=3, column=0, columnspan=2, sticky=W)
        # the toggle switches status
        self._ltoggles = Label(self, bg="black", fg="white", font=("Courier New", 24), text="Toggles: ")
        self._ltoggles.grid(row=4, column=0, columnspan=2, sticky=W)
        # the pause button (pauses the timer)
        self._lpause = tkinter.Button(self, bg="red", fg="white", font=("Courier New", 24), text="Pause", command=self.pause)
        self._lpause.grid(row=5, column=0, sticky=W, padx=25, pady=40)
        # the quit button
        self._lquit = tkinter.Button(self, bg="red", fg="white", font=("Courier New", 24), text="Quit", command=self.quit)
        self._lquit.grid(row=6, column=1, sticky=W, padx=25, pady=40)
    # ------------------------------------------------------------------------------------------------------------------------


    # binds the 7-segment display component to the GUI
    def setTimer(self, timer):
        self._timer = timer

    # binds the pushbutton component to the GUI
    def setButton(self, button):
        self._button = button

    # pauses the timer
    def pause(self):
        self._timer.pause()

    # quits the GUI, resetting some components
    def quit(self):
        # turn off the 7-segment display
        self._timer._display.blink_rate = 0
        self._timer._display.fill(0)
        # turn off the pushbutton's LED
        for pin in self._button._rgb:
            pin.value = True
        # close the GUI
        exit(0)


# MARK: Template (superclass) for various bomb components/phases
class PhaseThread(Thread):
    
    # MARK: INITIALIZATION
    def __init__(self, name):
        super().__init__(name=name, daemon=True)
        # initially, the phase thread isn't running
        self._running = False
        # phases can have values (e.g., a pushbutton can be True or False, a keypad passphrase can be some string, etc)
        self._value = None


    # MARK: MAIN FUNCTIONS
    # resets the phase's value
    def reset(self):
        self._value = None


# MARK: - MAIN TIMER CLASS
# the timer phase
class Timer(PhaseThread):
    def __init__(self, value, display, name="Timer"):
        super().__init__(name)
        self._value = value
        # the LCD display object
        self._display = display
        # initially, the timer isn't paused
        self._paused = False

    # updates the timer
    def update(self):
        self._min = f"{self._value // 60}".zfill(2)
        self._sec = f"{self._value % 60}".zfill(2)

    # runs the thread
    def run(self):
        self._running = True
        while self._running:
            if (not self._paused):
                # update the timer and display its value on the 7-segment display
                self.update()
                self._display.print(str(self))
                # wait 1s and continue
                sleep(1)
                # stop if the timer has expired
                if (self._value == 0):
                    break
                # otherwise, 1s has elapsed
                self._value -= 1
            else:
                sleep(0.1)
                print("sleep")
        self._running = False

    # pauses and unpauses the timer
    def pause(self):
        self._paused = not self._paused
        # blink the 7-segment display when paused
        self._display.blink_rate = (2 if self._paused else 0)
        

    def __str__(self):
        return f"{self._min}:{self._sec}"



#: MARK: - COMPONENT CLASSES

# the keypad phase
class Keypad(PhaseThread):
    
    # MARK: INITIALIZATION
    def __init__(self, keypad, timer, name="Keypad"):
        super().__init__(name)
        self._value = ""
        self._key = ""
        self._timer = timer
        self.pressed_keys = []
        self._keypad = keypad
        self._encrypted = []
        self._decrypted = [
            "Data",
            "Decryption",
            "Binary",
            "Compiler",
            "System",
            "Cryptography",
            "Computing",
            "Encryption",
            "Network",
            "Recursion",
            "Database",
            "Virtualization",
            "Algorithm",
            "Hashing",
            "Blockchain",
            "Cybersecurity"
        ]

        self._dictionary = {
            "2" : "a", "22" : "b", "222" : "c",
            "3": "d", "33": "e", "333": "f",
            "4": "g", "44": "h", "444": "i",
            "5": "j", "55": "k", "555": "l",
            "6": "m", "66": "n", "666": "o",
            "7": "p", "77": "r", "777": "s",
            "8": "t", "88": "u", "888": "v",
            "9": "w", "99": "x", "999": "y",
        }


    # MARK: MAIN FUNCTIONS
    # runs the thread
    def run(self):
        self._running = True
        print(BINARY_CODE)
        while (True):
            
            # process keys when keypad key(s) are pressed
            if (self._keypad.pressed_keys):
                # debounce
                while (self._keypad.pressed_keys):
                    try:
                        key = self._keypad.pressed_keys[0]
                    except:
                        key = "2"
                    sleep(0.1)
                    
                if (key == "*" and STAR_CLEARS_PASS):
                    self._value = ""
                    self._key = ""
                    
                # we haven't yet reached the max pass length (otherwise, we just ignore the keypress)
                elif (len(self._value) < MAX_PASS_LEN):
                    if key == "#":
                        if str(self._key) in self._dictionary.keys():
                            self._value += self._dictionary[str(self._key)]
                        self._key = ""
                        key = ""
                        pass
                    
                    # log the key
                    self._key += str(key)
                    
                    
                    # == DEBUG PRINT ==
                    print(self._value)
                    # =================
                
                # == DEBUG PRINT ==
                print()
                print("Key:")
                print(key)
                # =================
                
            sleep(0.1)
            
            # checks if the input 
            if self._value == self._decrypted[0].lower():
                self._running = False
               
                # == DEBUG PRINT ==
                print("Keyboard Defused")
                # =================
                
                gui.show_success_screen()
                
                # Stop the main timer
                timer._running = False
                timer._value = "00:00"
                timer.pause()
                
                display.brightness = 0
                
                break

    def __str__(self):
        return self._value

# the jumper wires phase
class Wires(PhaseThread):
    
    # MARK: INITIALIZATION
    def __init__(self, pins, name="Wires"):
        super().__init__(name)
        self._value = ""
        # the jumper wire pins
        self._pins = pins
    
    # MARK: MAIN FUNCTIONS
    # runs the thread
    def run(self):
        self._running = True
        while (True):
            # get the jumper wire states (0->False, 1->True)
            self._value = "".join([str(int(pin.value)) for pin in self._pins])
            sleep(0.1)
            # checks if the correct wires are unplugged
            if self._value[0] == "0" and self._value[2] == "0":
                self._running = False
                print("Wires Defused")

    def __str__(self):
        return f"{self._value}/{int(self._value, 2)}"


# the pushbutton phase
class ActionButton(PhaseThread):
    
    # MARK: INITIALIZATION
    def __init__(self, state, rgb, keypad, name="Button"):
        super().__init__(name)
        self._value = False
        self._state = state
        self._rgb = rgb
        self._defused = False
        self.code_entry_shown = False
        self._keypad = keypad  # Store keypad reference
        self._current_code = ""
        self._code_window = None


    # MARK: MAIN FUNCTIONS
    def run(self):
        self._running = True
        while (True):
            if self._defused:
                self._rgb[0].value = True  
                self._rgb[1].value = False
                self._rgb[2].value = True  
                
                if self._state.value and not self.code_entry_shown:
                    self.show_code_entry()
                    self.code_entry_shown = True
                    
                # Handle keypad input when code entry is active
                if self.code_entry_shown and self._code_window:
                    self.handle_keypad_input()
                    
            else:
                self._rgb[0].value = False
                self._rgb[1].value = True
                self._rgb[2].value = True
                
            self._value = self._state.value
            sleep(0.1)
        self._running = False

    def handle_keypad_input(self):
        if keypad.pressed_keys:
            while keypad.pressed_keys:
                try:
                    key = keypad.pressed_keys[0]
                    self.update_code_display()
                except:
                    pass
                sleep(0.1)
    
    # Functions below are for presenting a new window for entering the code from the keypad
    def show_code_entry(self):
        self._code_window = Toplevel()
        self._code_window.title("Code Entry")
        self._code_window.geometry("500x300")
        
        Label(self._code_window, 
              text="Enter DS (Decryption-Secret) Key:", 
              font=("Courier New", 14)).pack(pady=20)
        
        self._code_display = Label(self._code_window, 
                                 text="", 
                                 font=("Courier New", 14))
        self._code_display.pack(pady=20)
        
        instruction_label = Label(self._code_window,
                                text="Use keypad to enter code\n* to clear, # to finish letter",
                                font=("Courier New", 12))
        instruction_label.pack(pady=10)

    def update_code_display(self):
        if self._code_display:
            display_text = self._keypad._value
            self._code_display.config(text=display_text)

    def set_defused(self, defused):
        self._defused = defused


# the toggle switches phase
class Toggles(PhaseThread):
    
    # MARK: INITIALIZATION
    def __init__(self, pins, name="Toggles"):
        super().__init__(name)
        self._value = ""
        # the toggle switch pins
        self._pins = pins


    # MARK: MAIN FUNCTIONS
    # runs the thread
    def run(self):
        self._running = True
        while (True):
            # get the toggle switch values (0->False, 1->True)
            self._value = "".join([str(int(pin.value)) for pin in self._pins])
            sleep(0.1)
            # Checks if the toggles are correctly flipped
            self._running = not (self._value == BINARY_CODE)
               
        
    def __str__(self):
        return f"{self._value}/{int(self._value, 2)}"

######
# MARK: - MAIN PROGRAM

# configure and initialize the LCD GUI
WIDTH = 800
HEIGHT = 600
window = Tk()
gui = Lcd(window)

# configure and initialize the phases/components

# 7 segment display
# 4 pins: 5V(+), GND(-), SDA, SCL
#         ----------7SEG---------
i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.5
timer = Timer(COUNTDOWN, display)
# bind the 7-segment display to the LCD GUI
gui.setTimer(timer)

# keypad
# 8 pins: 10, 9, 11, 5, 6, 13, 19, NA
#         -----------KEYPAD----------
keypad_cols = [DigitalInOut(i) for i in (board.D10, board.D9, board.D11)]
keypad_rows = [DigitalInOut(i) for i in (board.D5, board.D6, board.D13, board.D19)]
keypad_keys = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("*", "0", "#"))
matrix_keypad = Matrix_Keypad(keypad_rows, keypad_cols, keypad_keys)
keypad = Keypad(matrix_keypad, timer)
keypad.start()

# jumper wires
# 10 pins: 14, 15, 18, 23, 24, 3V3, 3V3, 3V3, 3V3, 3V3
#          -------JUMP1------  ---------JUMP2---------
wire_pins = [DigitalInOut(i) for i in (board.D14, board.D15, board.D18, board.D23, board.D24)]
for pin in wire_pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.DOWN
wires = Wires(wire_pins)

# pushbutton
# 6 pins: 4, 17, 27, 22, 3V3, 3V3
#         -BUT1- -BUT2-  --BUT3--
button_input = DigitalInOut(board.D4)
button_RGB = [DigitalInOut(i) for i in (board.D17, board.D27, board.D22)]
button_input.direction = Direction.INPUT
button_input.pull = Pull.DOWN
for pin in button_RGB:
    pin.direction = Direction.OUTPUT
    pin.value = True
button = ActionButton(button_input, button_RGB, keypad)
# bind the pushbutton to the LCD GUI
gui.setButton(button)

# toggle switches
# 3x3 pins: 12, 16, 20, 21, 3V3, 3V3, 3V3, 3V3, GND, GND, GND, GND
#           -TOG1-  -TOG2-  --TOG3--  --TOG4--  --TOG5--  --TOG6--
toggle_pins = [DigitalInOut(i) for i in (board.D12, board.D16, board.D20, board.D21)]
for pin in toggle_pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.DOWN
toggles = Toggles(toggle_pins)

# start the phase threads
wires.start()
button.start()
toggles.start()


# MARK: ---- LEGACY CODE ----
# check the phase threads
def check():
    # check the countdown
    if (timer._running):
        # update the GUI
        gui._ltimer.config(text=f"Time left: {timer}")
    else:
        # if the countdown has expired, quit
        quit()
    # check the keypad
    if (keypad._running):
        # update the GUI
        gui._lkeypad.config(text=f"Combination: {keypad}")
    # check the wires
    if (wires._running):
        # update the GUI
        gui._lwires.config(text=f"Wires: {wires}")
    # check the button
    if (button._running):
        # update the GUI
        gui._lbutton.config(text=f"Button: {button}")
       
    # check the toggles
    if (toggles._running):
        print("")
       
    # check again after 100ms
    gui.after(100, check)
# ---------------------------


# quits the bomb
def quit():
    # turn off the 7-segment display
    display.blink_rate = 0
    display.fill(0)
    # turn off the pushbutton's LED
    for pin in button._rgb:
        pin.value = True
    # destroy the GUI and exit the program
    window.destroy()
    exit(0)


# MARK: ---- LEGACY CODE ----
# start checking the threads
check_class()
# ---------------------------


# display the LCD GUI
window.mainloop()

print("The bomb has been turned off.")