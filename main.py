variable = 0
variable2 = 0

def on_button_pressed_a():
    global variable
    variable = variable + 1
    basic.show_number(variable)
def on_button_pressed_b():
    global variable2
    variable2 = variable2 + 1
    basic.show_number(variable2)
def on_pin_pressed_p0():
    global variable, variable2
    variable = 0
    variable2 = 0
    basic.clear_screen()
def on_pin_pressed_p1():
    basic.clear_screen()
    basic.show_number(variable + variable2)
def on_pin_pressed_p2():
    basic.clear_screen()
    basic.show_number(variable*variable2)
def on_pin_pressed_p3():
    basic.clear_screen()
    basic.show_number(variable/variable2)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
def on_forever():
    pass
basic.forever(on_forever)
