import tkinter
import config

def main():



    top = tkinter.Tk()
    window = tkinter.PanedWindow(top, orient=tkinter.VERTICAL)
    canvas = tkinter.Canvas(top, width=config.width, height=config.height)
    bg = tkinter.PhotoImage(file='map1024x512.gif')

    canvas.create_image((config.width / 2), (config.height / 2), image=bg)
    text = tkinter.Text(top)
    text.configure(state="disabled")
    config.textBox = text

    window.add(canvas)
    window.add(text)

    top.mainloop()