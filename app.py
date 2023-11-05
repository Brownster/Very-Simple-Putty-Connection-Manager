import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
import xml.etree.ElementTree as ET
import subprocess
import os

# Configuration file path
config_file = 'ssh_manager_config.txt'

def save_config(ssh_path):
    with open(config_file, 'w') as f:
        f.write(ssh_path)

def load_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return f.read().strip()
    else:
        return None

def ask_for_ssh_path():
    path = filedialog.askopenfilename(
        title="Locate PuTTY or KiTTY executable",
        filetypes=(("Executable files", "*.exe"), ("All files", "*.*"))
    )
    if path:
        save_config(path)
        return path
    else:
        messagebox.showerror("Error", "SSH executable path is required to continue.")
        return ask_for_ssh_path()  # Keep asking until a path is provided

# Load or ask for SSH path at startup
ssh_path = load_config()
if not ssh_path:
    ssh_path = ask_for_ssh_path()

def import_xml():
    # ... existing import_xml function

def start_ssh_session(event):
    # Get the selected item
    item = tree.selection()[0]
    # Fetch the details from the tree view
    connection_name = tree.item(item, 'text')
    host = tree.item(item, 'values')[0]
    port = tree.item(item, 'values')[1]
    username = tree.item(item, 'values')[2]

    # Define the command to open SSH session (using the path from the config file)
    ssh_command = f'"{ssh_path}" -ssh {username}@{host} -P {port}'

    # Execute the command (this will open PuTTY with the SSH session)
    subprocess.Popen(ssh_command, shell=True)

# Create the main window
root = tk.Tk()
root.title("SSH Connection Manager")

# Create a frame for the tree view
tree_frame = ttk.Frame(root)
tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the tree view
tree = ttk.Treeview(tree_frame, columns=('Host', 'Port', 'Username'))
tree.heading('#0', text='Connection Name')
tree.heading('Host', text='Host')
tree.heading('Port', text='Port')
tree.heading('Username', text='Username')
tree.column('#0', width=150)
tree.column('Host', width=100)
tree.column('Port', width=50)
tree.column('Username', width=100)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the tree view
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')
tree.configure(yscrollcommand=scrollbar.set)

# Create a frame for the buttons
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

# Add some buttons
add_button = ttk.Button(button_frame, text="Add Connection")
add_button.pack(side=tk.LEFT, padx=5, pady=5)

remove_button = ttk.Button(button_frame, text="Remove Connection")
remove_button.pack(side=tk.LEFT, padx=5, pady=5)

# Button for importing XML with the import function bound to it
import_button = ttk.Button(button_frame, text="Import XML", command=import_xml)
import_button.pack(side=tk.LEFT, padx=5, pady=5)

# Add double-click event binding to the tree view
tree.bind('<Double-1>', start_ssh_session)

# Run the main window loop
root.mainloop()

