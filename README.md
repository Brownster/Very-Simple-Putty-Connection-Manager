# SSH Connection Manager

SSH Connection Manager is a desktop application designed to manage your SSH connections in a convenient tree structure. It allows you to import connection settings from an XML file, organize them visually, and launch sessions using PuTTY or KiTTY. 

## Features

- Tree view display of SSH connections.
- Import connection settings from an XML file.
- Launch SSH sessions with PuTTY or KiTTY.
- Save the path to the SSH client executable (PuTTY or KiTTY) upon first startup.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually comes with Python installation on Windows)
- PuTTY or KiTTY installed on your system

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/brownster/Very-Simple-Putty-Connection-Manager.git
cd ssh-connection-manager

No additional installation is required as the application uses the Python standard library, except for the SSH client (PuTTY/KiTTY), which needs to be installed separately.
Usage

Run the application by executing the script:

sh

python3 app.py

On the first startup, the application will ask for the path to your SSH client executable. This path will be saved for future use.

To manage your SSH connections, import your XML file with connection settings by clicking on the "Import XML" button.

Double-click on a connection in the tree view to start an SSH session.
Configuration

The application creates a configuration file named ssh_manager_config.txt to store the path to the SSH client executable. If you need to change this path after the first setup, edit this file directly.
Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.
