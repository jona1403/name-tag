let variable = 0
let variable2 = 0
input.onPinPressed(TouchPin.P0, function () {
    variable = 0
    variable2 = 0
    basic.clearScreen()
})
function on_pin_pressed_p3 () {
    basic.clearScreen()
    basic.showNumber(variable / variable2)
}
input.onButtonPressed(Button.A, function () {
    variable = variable + 1
    basic.showNumber(variable)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.clearScreen()
    basic.showNumber(variable * variable2)
})
input.onButtonPressed(Button.B, function () {
    variable2 = variable2 + 1
    basic.showNumber(variable2)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.clearScreen()
    basic.showNumber(variable + variable2)
})
basic.forever(function () {
	
})
