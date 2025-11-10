import webbrowser

class Annoy:
    def __init__(self):
        self._annoy : bool = False
        self._annoy_index: int = 0
        print("Warning: This module can glitch and force your computer to restart")
        print("Warning: Not recommended to set annoy_level > 3")

    def init(self):
        self._annoy = True

    def uninit(self):
        self._annoy = False
        self._annoy_index = 0

    def set_annoy_level(self, new_index: int):
        if self._annoy:
            self._annoy_index = new_index
            if self._annoy_index == 0:
                self._annoy_index = 5

    def rickroll(self):
        if self._annoy:
            if self._annoy_index <= 3:
                for i in range(4 ^ self._annoy_index):
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9uXgQ")
            if self._annoy_index == 4:
                for i in range(200):
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9uXgQ")
            else:
                while True:
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9uXgQ")
    
