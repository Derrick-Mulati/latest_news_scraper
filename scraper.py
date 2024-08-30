import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox

def get_latest_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h3')  # Adjusted based on BBC's structure
        
        return [headline.text.strip() for headline in headlines[:5]]
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve headlines:\n{e}")
        return []

def fetch_and_display():
    url = url_entry.get()
    headlines = get_latest_headlines(url)
    if headlines:
        headlines_listbox.delete(0, tk.END)
        for i, headline in enumerate(headlines, 1):
            headlines_listbox.insert(tk.END, f"{i}. {headline}")

# Setting up the Tkinter UI
root = tk.Tk()
root.title("Latest News Headlines")

# URL entry field
url_label = ttk.Label(root, text="News URL:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)
url_entry.insert(0, 'https://www.bbc.com/news')  # Default URL

# Fetch headlines button
fetch_button = ttk.Button(root, text="Fetch Headlines", command=fetch_and_display)
fetch_button.pack(pady=10)

# Listbox to display headlines
headlines_listbox = tk.Listbox(root, width=80, height=10)
headlines_listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
