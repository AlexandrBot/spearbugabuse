import win32api, win32con 
import keyboard
import time

def leftclick():
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
     time.sleep(0.01)
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def bugabuse():
     spear_equipped = False
     while True:
          if keyboard.is_pressed('r') and spear_equipped == False:
               keyboard.press_and_release('2')
               time.sleep(0.276658)
               leftclick()
               keyboard.press_and_release('1')
          if keyboard.is_pressed('3') or keyboard.is_pressed('4') or keyboard.is_pressed('5') or keyboard.is_pressed('6') or keyboard.is_pressed('7') or keyboard.is_pressed('8') or keyboard.is_pressed('9'):
               spear_equipped = False
          if keyboard.is_pressed('1'):
               spear_equipped = True 
          if keyboard.is_pressed('/'):
               break
bugabuse()