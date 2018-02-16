import urllib.request
import json
from pynput import keyboard
import clipboard


class CatFact:
    v_pressed = False
    ctrl_pressed = False

    def GetFact():
        url = urllib.request.urlopen("https://catfact.ninja/fact")
        fact_json = json.load(url)

        return fact_json["fact"]

    def KeyPressListen(key):
        print(key)
        try:
            if key.char == "v":
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
            CatFact.CopyFact()

    def CopyFact():
        clipboard.copy(CatFact.GetFact())


if __name__ == "__main__":

    # Clear clipboard on start
    clipboard.copy("")

    with keyboard.Listener(on_press=CatFact.KeyPressListen,
                           on_release=CatFact.KeyReleaseListen) as listener:
        listener.join()
