from tkinter import *
import time


class StopWatch(Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()
        self.on = True

    def makeWidgets(self):
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr, bg='skyblue',
                  font=("Arial", 25, "bold"))
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        """ Update the label with elapsed time. """
        if self.on:
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._timer = self.after(10, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def restart(self):
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.on = True
        self.Start()


    def stop_timer(self):
        self.on = False

    def reset(self):
        self.timestr.set('00:00:00')


def main():
    root = Tk()
    root.title('Stopwatch')
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("200x200+{}+{}".format(positionRight, positionDown))
    #root.geometry('300x300')
    root.attributes("-topmost", True)
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)  # which implicitly packs top_frame on the top
    sw = StopWatch(root)
    sw.pack(side=TOP)
    # Button(root, text='Start', command=sw.Start).pack(side=LEFT)
    sw.Start()

    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    Button(root, text='Stop', command=lambda: sw.stop_timer()).pack(side=BOTTOM)
    Button(root, text='Restart', command=lambda: sw.restart()).pack(side=BOTTOM)
    Button(root, text='Reset', command=lambda: sw.reset()).pack(side=BOTTOM)

    root.mainloop()


if __name__ == '__main__':
    main()