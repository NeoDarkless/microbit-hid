def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.show_string("BLE connected")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
    basic.pause(100)
    basic.show_string("BLE disconnected")
    basic.show_leds("""
        # . # # .
        . # . . #
        . . # # .
        . # # . #
        # . # # .
        """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    keyboard.send_string(keyboard.modifiers(keyboard._Modifier.CONTROL))
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_leds("""
    # . # # .
    . # . . #
    . . # # .
    . # # . #
    # . # # .
    """)
keyboard.start_keyboard_service()

def on_forever():
    pass
basic.forever(on_forever)
