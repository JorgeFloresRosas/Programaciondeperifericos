from tkinter import *
from tkinter import ttk

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barra de Progreso")

        self.progress_bar = ttk.Progressbar(root, mode="indeterminate", length = 200, orient = VERTICAL)
        self.progress_bar.pack(pady=10)

        self.start_button = Button(root, text="Iniciar", command=self.start_progress)
        self.start_button.pack()

        self.stop_button = Button(root, text="Detener", command=self.stop_progress)
        self.stop_button.pack()

    def start_progress(self):
        self.progress_bar.start()

    def stop_progress(self):
        self.progress_bar.stop()

if __name__ == "__main__":
    root = Tk()
    app = ProgressBarApp(root)
    root.mainloop()
