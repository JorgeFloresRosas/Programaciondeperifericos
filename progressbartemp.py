from tkinter import *
from tkinter import ttk

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barra de Progreso")

        self.progress_bar = ttk.Progressbar(root, mode="determinate", length=200)
        self.progress_bar.pack(pady=10)

        self.start_button = Button(root, text="Iniciar", command=self.start_progress)
        self.start_button.pack()

    def start_progress(self):
        self.progress_bar["value"] = 0  # Establecer el valor inicial en 0
        self.root.after(1000, self.update_progress)  # Llama a la función update_progress después de 1000ms (1 segundo)

    def update_progress(self):
        current_value = self.progress_bar["value"]
        if current_value < 100:
            step = 10  # Aumentar el valor en 10%
            self.progress_bar["value"] = current_value + step
            self.root.after(1000, self.update_progress)  # Llama a la función update_progress nuevamente después de 1000ms
        else:
            self.progress_bar["value"] = 100

if __name__ == "__main__":
    root = Tk()
    app = ProgressBarApp(root)
    root.mainloop()
