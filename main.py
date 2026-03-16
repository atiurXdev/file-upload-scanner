import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from scanner import run_scan

def start_scan():
    btn_scan.config(state='disabled')
    output_box.delete(1.0, tk.END)
    
    base_url = entry_url.get().strip()
    email = entry_email.get().strip()
    password = entry_pass.get().strip()

    def log(msg):
        output_box.insert(tk.END, msg + "\n")
        output_box.see(tk.END)
        root.update()

    def scan_thread():
        run_scan(base_url, email, password, log)
        btn_scan.config(state='normal')

    threading.Thread(target=scan_thread).start()

# GUI Setup
root = tk.Tk()
root.title("File Upload Vulnerability Scanner")
root.geometry("700x500")
root.configure(bg="#1e1e2e")

# Title
tk.Label(root, text="🔍 File Upload Vulnerability Scanner",
         font=("Helvetica", 16, "bold"),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=5)

tk.Label(frame, text="Target URL:", bg="#1e1e2e",
         fg="#cdd6f4").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_url = tk.Entry(frame, width=40, bg="#313244", fg="white",
                     insertbackground="white")
entry_url.insert(0, "http://localhost:3000")
entry_url.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:", bg="#1e1e2e",
         fg="#cdd6f4").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(frame, width=40, bg="#313244", fg="white",
                       insertbackground="white")
entry_email.insert(0, "test@test.com")
entry_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Password:", bg="#1e1e2e",
         fg="#cdd6f4").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_pass = tk.Entry(frame, width=40, bg="#313244", fg="white",
                      show="*", insertbackground="white")
entry_pass.insert(0, "Test1234!")
entry_pass.grid(row=2, column=1, padx=5, pady=5)

# Scan Button
btn_scan = tk.Button(root, text="▶  Start Scan",
                     font=("Helvetica", 12, "bold"),
                     bg="#89b4fa", fg="#1e1e2e",
                     padx=20, pady=8, command=start_scan)
btn_scan.pack(pady=10)

# Output Box
output_box = scrolledtext.ScrolledText(root, width=80, height=15,
                                        bg="#181825", fg="#a6e3a1",
                                        font=("Courier", 11))
output_box.pack(padx=10, pady=5)

root.mainloop()