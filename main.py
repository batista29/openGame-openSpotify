import pyautogui
import time

pyautogui.press('win')
pyautogui.write('chrome')
time.sleep(0.5)
pyautogui.press('enter')

time.sleep(0.7)
pyautogui.write('https://open.spotify.com/')
pyautogui.press('enter')

time.sleep(3)
pyautogui.moveTo(x=293, y=255)
time.sleep(2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(x=167, y=608)
pyautogui.click()
time.sleep(1)

pyautogui.press('win')
pyautogui.write('tlauncher')
pyautogui.press('enter')