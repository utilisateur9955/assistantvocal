import socket

try:
    ip = socket.gethostbyname("www.google.com")
    print("IP de Google :", ip)
except Exception as e:
    print("Erreur :", e)
