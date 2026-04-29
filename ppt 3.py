import tkinter as tk
from tkinter import messagebox
import math

def hitung():
    try:
        fungsi = entry_fungsi.get()
        x0 = float(entry_x0.get())
        x1 = float(entry_x1.get())
        tol = 0.0001
        maks = 50

        hasil.delete("1.0", tk.END)

        for i in range(maks):
            f0 = eval(fungsi, {"x": x0, "math": math})
            f1 = eval(fungsi, {"x": x1, "math": math})

            x2 = x1 - (f1 * (x1 - x0)) / (f1 - f0)

            hasil.insert(tk.END, f"Iterasi {i+1}: x = {x2:.6f}\n")

            if abs(x2 - x1) < tol:
                hasil.insert(tk.END, f"\nAkar = {x2:.6f}")
                return

            x0 = x1
            x1 = x2

    except:
        messagebox.showerror("Error", "Input salah!")

root = tk.Tk()
root.title("Metode Secant")
root.geometry("420x500")
root.configure(bg="#c2dc80")   

tk.Label(root, text="METODE SECANT", 
         bg="#7e914e", fg="#f3eef1",
         font=("Arial", 16, "bold")).pack(pady=10)


tk.Label(root, text="Fungsi f(x):", bg="#d56989", fg="white", font=("Arial", 10, "bold")).pack()
entry_fungsi = tk.Entry(root, width=30, bg="white", fg="black", font=("Arial", 11), justify="center")
entry_fungsi.pack(pady=5)
entry_fungsi.insert(0, "")

tk.Label(root, text="x0:", bg="#d56989", fg="white", font=("Arial", 10, "bold")).pack()
entry_x0 = tk.Entry(root, bg="white", fg="black", justify ="center")
entry_x0.pack(pady=5)
entry_x0.insert(0, "")


tk.Label(root, text="x1:", bg="#d56989", fg="white", font=("Arial", 10, "bold")).pack()
entry_x1 = tk.Entry(root, bg="white", fg="black", justify="center")
entry_x1.pack(pady=5)
entry_x1.insert(0, "")

tk.Button(root, text="HITUNG",
          command=hitung,
          bg="#7e914e",
          fg="white",
          activebackground="#7e914e",
          font=("Arial", 11, "bold"),
          width=15).pack(pady=10)

hasil = tk.Text(root, height=15, width=42,
                bg="#f3eef1",
                fg="#5c6740",
                font=("Consolas", 10))
hasil.pack(pady=10)

root.mainloop()