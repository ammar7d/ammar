def on_button_pressed_a():
    global fly
    fly = game.create_sprite(2, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global p
    p = randint(1, 9)
    basic.show_number(p)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_string("Hello!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

p = 0
fly: game.LedSprite = None
a = 10
b = 5
if a > b:
    basic.show_string("a is greater than b")