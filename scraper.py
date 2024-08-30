import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox

def get_all_headings(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all heading tags
        headings = []
        for heading_tag in ['h3', 'h4', 'h5', 'h6']:
            headings.extend(soup.find_all(heading_tag))
        
        return [heading.text.strip() for heading in headings]
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve headings:\n{e}")
        return []

def fetch_and_display():
    url = url_entry.get()
    headings = get_all_headings(url)
    if headings:
        headings_listbox.delete(0, tk.END)
        for i, heading in enumerate(headings, 1):
            headings_listbox.insert(tk.END, f"{i}. {heading}")

# Setting up the Tkinter UI
root = tk.Tk()
root.title("Web Page Headings Scraper")

# URL entry field
url_label = ttk.Label(root, text="Website URL:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)
url_entry.insert(0, 'https://www.bbc.com/news')  # Default URL

# Fetch headings button
fetch_button = ttk.Button(root, text="Fetch Headings", command=fetch_and_display)
fetch_button.pack(pady=10)

# Listbox to display headings
headings_listbox = tk.Listbox(root, width=80, height=15)
headings_listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
