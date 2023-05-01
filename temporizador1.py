import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Temporizador")
        self.master.config(bg="#B0BEC5") # Agregamos un color de fondo a la ventana


        # Inicializamos los valores
        self.total_time = 300  # 5 minutos
        self.sticker_count = 0
        self.reset_count = 0

        # Creamos los widgets
        self.timer_label = tk.Label(self.master, text="05:00", font=("Helvetica", 50), fg="#ffffff", bg="#607D8B", width=8, height=1)
        self.reset_button = tk.Button(self.master, text="MENSAJE", command=self.reset_timer_count, bg="#607D8B", fg="#ffffff", font=("Helvetica", 16), width=22, height=2)
        self.sticker_button = tk.Button(self.master, text="MENSAJE Y STICKER", command=self.reset_timer_sticker, bg="#607D8B", fg="#ffffff", font=("Helvetica", 16), width=22, height=2)
        self.reset_only_button = tk.Button(self.master, text="FOTO", command=self.reset_timer, bg="#607D8B", fg="#ffffff", font=("Helvetica", 16), width=22, height=2)
        # self.stop_button = tk.Button(self.master, text="Detener", command=self.stop_timer, bg="#ffffff", fg="#000000", font=("Helvetica", 16))
        self.reset_count_label = tk.Label(self.master, text="Mensajes: 0", bg="#B0BEC5", font=("Helvetica", 25))
        self.sticker_count_label = tk.Label(self.master, text="Stickers: 0", bg="#B0BEC5", font=("Helvetica", 25))
        # self.photo_count_label = tk.Label(self.master, text="Foto: 0", font=("Helvetica", 25))

        # Los colocamos en la ventana
        self.timer_label.pack(pady=20)
        self.reset_count_label.pack(pady=5)
        self.sticker_count_label.pack(pady=5)
        self.reset_button.pack(pady=10, padx=25)
        self.sticker_button.pack(pady=10, padx=30)
        self.reset_only_button.pack(pady=10, padx=30)
        # self.stop_button.pack(pady=10, padx=30)
        

        # Iniciamos el temporizador
        self.timer_id = None    
        self.timer()

    def timer(self):
        minutes = self.total_time // 60
        seconds = self.total_time % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        if self.total_time == 0:
            pass
        else:
            self.total_time -= 1
            self.timer_id = self.master.after(1000, self.timer)

    def reset_timer(self):
        self.total_time = 300
        self.master.after_cancel(self.timer_id)
        self.timer_id = None
        self.timer()

    def reset_timer_count(self):
        self.reset_count += 1
        self.reset_count_label.config(text=f"Mensajes: {self.reset_count}")
        self.reset_timer()

    def reset_timer_sticker(self):
        self.sticker_count += 1
        self.reset_count += 1
        self.sticker_count_label.config(text=f"Stickers: {self.sticker_count}")
        self.reset_count_label.config(text=f"Mensajes: {self.reset_count}")
        self.reset_timer()
          

    # def stop_timer(self):
    #     pass


root = tk.Tk()
timer = Timer(root)
root.mainloop()
