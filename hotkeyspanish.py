#-*-coding: utf-8-*-
from keyboard import add_hotkey, wait, write
import ctypes

def CAPSLOCK_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)

def spanishy(letter, dot=False):
	result = ""
	if letter == "a":
		result = "á"
	elif letter == "e":
		result = "é"
	elif letter == "i":
		result = "í"
	elif letter == "o":
		result = "ó"
	elif letter == "u":
		if dot:
			result = "ü"
		else:
			result = "ú"
	elif letter == "n":
		result = "ñ"


	if CAPSLOCK_STATE():
		result = result.upper()
	print(result)
	write(result)




def main():
	add_hotkey("shift+a", spanishy, args=("a"))
	add_hotkey("shift+e", spanishy, args=("e"))
	add_hotkey("shift+i", spanishy, args=("i"))
	add_hotkey("shift+o", spanishy, args=("o"))
	add_hotkey("shift+u", spanishy, args=("u"))
	add_hotkey("shift+:+u", spanishy, args=("u", True))
	add_hotkey("shift+n", spanishy, args=("n"))
	wait()


if __name__ == '__main__':
	main()