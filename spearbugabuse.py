import win32api, win32con 
import keyboard
import time

def keybind():
    print('Assign a key, press Enter to save:')
    spear=input("Spear (default: 1): ").strip() or "1"
    hand = input("Hand (default: 2): ").strip() or "2"
    run_key = input('Start (default: r): ').strip() or "r"
    quit_key = input('Quit (default: ,): ').strip() or ","
    print(f'Current keybinds:Hand={hand}, Spear={spear}, Starter={run_key}, Quit_key={quit_key}')
    return spear,hand,run_key,quit_key


def leftclick():
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
     time.sleep(0.01)
     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def bugabuse():
     spear_slot, hand_slot, run_key, quit_key = keybind()
     
     spear_equipped = False
     while True:
          if keyboard.is_pressed(run_key) and spear_equipped == False:
               keyboard.press_and_release(hand_slot)
               time.sleep(0.276658)
               leftclick()
               keyboard.press_and_release(spear_slot)
          if keyboard.is_pressed('3') or keyboard.is_pressed('4') or keyboard.is_pressed('5') or keyboard.is_pressed('6') or keyboard.is_pressed('7') or keyboard.is_pressed('8') or keyboard.is_pressed('9'):
               spear_equipped = False
          if keyboard.is_pressed(spear_slot):
               spear_equipped = True 
          if keyboard.is_pressed(quit_key):
               break
bugabuse()
