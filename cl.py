import pyautogui
import time

print("Clicker başlıyor! 5 saniye içinde çalışmaya başlayacak...")
time.sleep(5)  

try:
    while True:
        pyautogui.click() 
        time.sleep(10)  
except KeyboardInterrupt:
    print("Clicker durdu.")
