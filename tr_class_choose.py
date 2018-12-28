# import the library
from appJar import gui


def setup_gui():
    global app
    app = gui("Torrent Class Chooser")

def set_window():
    app.addLabel("title", "Welcome to appJar")
    app.setLabelBg("title", "green")

setup_gui()
set_window()
# start the GUI
app.go()
