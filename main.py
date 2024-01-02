def on_button_pressed_a():
    global var_primera
    basic.show_number(var_primera)
    var_primera = 1 + var_primera
input.on_button_pressed(Button.A, on_button_pressed_a)

var_primera = 0
basic.show_number(var_primera)