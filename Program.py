import urllib.request
import json
from pynput import keyboard
import clipboard
import sys


class CatFact:
    v_pressed = False
    ctrl_pressed = False

    fact_json = None

    def GetFact():
        url = urllib.request.urlopen("https://catfact.ninja/fact")
        CatFact.fact_json = json.load(url)

    def CheckLength():
        try:
            max_length = int(sys.argv[1])
        except (IndexError, ValueError):
            max_length = None

        if max_length is not None and CatFact.fact_json["length"] > max_length:
            CatFact.GetFact()
        else:
            CatFact.CopyFact()
            print(CatFact.fact_json["length"])

    def KeyPressListen(key):
        try:
            if key.char == "v" or key.char == "V":
                CatFact.v_pressed = True
        except AttributeError:
            if key == keyboard.Key.ctrl:
                CatFact.ctrl_pressed = True

        CatFact.CheckKeys()

    def KeyReleaseListen(key):
        try:
            if key.char == "v":
                CatFact.v_pressed = False
        except AttributeError:
            if key == keyboard.Key.ctrl:
                CatFact.ctrl_pressed = False

    def CheckKeys():
        if CatFact.v_pressed and CatFact.ctrl_pressed:
            CatFact.GetFact()
            CatFact.CheckLength()

    def CopyFact():
        clipboard.copy(CatFact.fact_json["fact"])


if __name__ == "__main__":

    # Clear clipboard on start
    clipboard.copy("")

    with keyboard.Listener(on_press=CatFact.KeyPressListen,
                           on_release=CatFact.KeyReleaseListen) as listener:
        listener.join()
