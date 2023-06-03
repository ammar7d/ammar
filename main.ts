input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    fly = game.createSprite(2, 4)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    p = randint(1, 9)
    basic.showNumber(p)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("Hello!")
})
let p = 0
let fly : game.LedSprite = null
let a = 10
let b = 5
if (a > b) {
    basic.showString("a is greater than b")
}

