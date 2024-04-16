import tkinter as tk

root = tk.Tk()

# Tạo một nút để lấy kích thước cửa sổ
button = tk.Button(root, text="Get Window Size", command=lambda: print("Geometry:", root.winfo_geometry()))
button.pack()

root.mainloop()
