# import tkinter as tk
# from tkinter import messagebox
# import pyshorteners

# class URLShortener:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("URL Shortener")
#         self.root.geometry("400x200")

#         # Create header label
#         self.header_label = tk.Label(root, text="URL Shortener", font=("Arial", 18, "bold"))
#         self.header_label.pack(pady=20)

#         # Create URL entry field
#         self.url_label = tk.Label(root, text="Enter URL:")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(root, width=40)
#         self.url_entry.pack()

#         # Create shortener button
#         self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
#         self.shorten_button.pack(pady=10)

#         # Create result label
#         self.result_label = tk.Label(root, text="Shortened URL:")
#         self.result_label.pack()
#         self.result_entry = tk.Entry(root, width=40)
#         self.result_entry.pack()

#     def shorten_url(self):
#         url = self.url_entry.get()
#         if url:
#             try:
#                 shortener = pyshorteners.Shortener()
#                 shortened_url = shortener.tinyurl.short(url)
#                 self.result_entry.delete(0, tk.END)
#                 self.result_entry.insert(0, shortened_url)
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))
#         else:
#             messagebox.showerror("Error", "Please enter a URL")

# root = tk.Tk()
# url_shortener = URLShortener(root)
# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import pyshorteners

class URLShortener:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Create main frame
        self.main_frame = tk.Frame(root, bg="#f7f7f7")
        self.main_frame.pack(fill="both", expand=True)

        # Create header label
        self.header_label = tk.Label(self.main_frame, text="URL Shortener", font=("Arial", 24, "bold"), fg="#3498db", bg="#f7f7f7")
        self.header_label.pack(pady=20)

        # Create URL entry field
        self.url_label = tk.Label(self.main_frame, text="Enter URL:", font=("Arial", 14), fg="#666", bg="#f7f7f7")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 14), fg="#333", bg="#fff", highlightthickness=1, highlightcolor="#ccc", borderwidth=2, relief="groove")
        self.url_entry.pack(pady=10)

        # Create shortener button
        self.shorten_button = tk.Button(self.main_frame, text="Shorten URL", command=self.shorten_url, font=("Arial", 14, "bold"), fg="#fff", bg="#3498db", activebackground="#4CAF50", activeforeground="#fff")
        self.shorten_button.pack(pady=10)

        # Create result label
        self.result_label = tk.Label(self.main_frame, text="Shortened URL:", font=("Arial", 14), fg="#666", bg="#f7f7f7")
        self.result_label.pack()
        self.result_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 14), fg="#333", bg="#fff", highlightthickness=1, highlightcolor="#ccc", borderwidth=2, relief="groove")
        self.result_entry.pack(pady=10)

    def shorten_url(self):
        url = self.url_entry.get()
        if url:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(url)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, shortened_url)
        else:
            messagebox.showerror("Error", "Please enter a URL")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortener(root)
    root.mainloop()