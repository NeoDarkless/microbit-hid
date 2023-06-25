bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    basic.showString("BLE connected")
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showIcon(IconNames.No)
    basic.pause(100)
    basic.showString("BLE disconnected")
    basic.showLeds(`
        # . # # .
        . # . . #
        . . # # .
        . # # . #
        # . # # .
        `)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    keyboard.sendString(keyboard.modifiers(keyboard._Modifier.control))
})
basic.showLeds(`
    # . # # .
    . # . . #
    . . # # .
    . # # . #
    # . # # .
    `)
keyboard.startKeyboardService()
basic.forever(function on_forever() {
    
})
