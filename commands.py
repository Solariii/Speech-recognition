import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is python commander. How are you?")
        else:
            f = Fetcher("https://www.google.com/search?sxsrf=ACYBGNTeZ6qqc_TMKB89RIRNgfBEQE9g4Q%3A1568993598414&source=hp&ei=PvGEXd2OF4Xkgwf0rYuYBA&q=" + text)
            answer = f.lookup()
            self.respond(answer)

        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("Opening " + app)
            os.system("open -a " + app + ".app")

    def respond(self, response):
        print(response)
        subprocess.call("say '" + response + "'", shell=True)