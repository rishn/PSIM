# RJK'S Password Sensitive Information Manager
<p align="center">
  <img src="https://github.com/rishn/PSIM/blob/main/PSIM/Banner.png?raw=true" alt="Gameplay" />
</p>

<p align="center">
  <img src="https://github.com/rishn/PSIM/blob/main/PSIM/Palm Print.png?raw=true" alt="Gameplay" />
</p>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)

## Overview

This application is a secure password manager built using Python's Tkinter library. It allows users to generate and manage passwords securely. The application features a clear and user-friendly interface to perform actions such as generating passwords, adding or updating accounts, and managing sub-groups. All sensitive information is stored in a local directory with encryption for added security.

## Features

- **Password Generation**: Generate secure passwords with customizable length and complexity.
- **Account Management**: Add, update, and delete accounts within sub-groups.
- **Sub-Group Management**: Create and manage sub-groups for organizing accounts.
- **Clipboard Functionality**: Copy generated passwords or account details to the clipboard.

## Demo

https://github.com/user-attachments/assets/ee0192eb-89da-4d71-84c8-f9e7005ac5df

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Additional Python packages: `string`, `random`
  
## Installation

1. **Clone or Download**: Clone the repository or download the code to your local machine.
     ```bash
      git clone https://github.com/rishn/PSIM
    ```

2. **Install Dependencies**: Ensure Python 3.8 and Tkinter are installed. Tkinter usually comes with Python, so no additional installation is typically required.

3. **Setup Directory Structure**: Ensure the `Sensitive` directory exists in the same location as your script. If not, the application will create it automatically.
    ```bash
    mkdir Sensitive
    ```

5. **Run the Application**: Execute the script to launch the application.
   <br/>For Windows:
    ```bash
    python psim.py
    ```

    For Linux/MacOS:
    ```bash
    python3 psim.py
    ```

## Usage

### Initial Setup

- **Clearance Key Setup**: On the first run, you will be prompted to enter and confirm a new clearance key. This key is used to secure access to the application.

### Main Features

- **Generate Secure Password**:
  - Navigate to "Secure Password Generator" to create strong passwords.
  - Specify the desired length and generate a password.
  - Option to copy the generated password to the clipboard.

- **Manage Personal Information**:
  - **View**: View details of existing accounts and sub-groups.
  - **Add**: Add new sub-groups or accounts to your data.
  - **Delete**: Remove existing sub-groups or accounts.
  - **Update**: Modify details of existing accounts or sub-groups.

### Navigating the GUI

- **Main Window**: After entering a valid clearance key, the main window will provide options to view, add, delete, or update personal information.
- **Sub-Groups and Accounts**: Use the listbox to interact with sub-groups and accounts. Buttons are provided for each action to manage your information effectively.

## File Structure

- **`psim.py`**: The main script file containing the application logic.
- **`Sensitive/1.dat`**: Stores the clearance key.
- **`Sensitive/2.dat`**: Stores personal information in a pseudo-encrypted format.
- **`Banner.png`**: Image file used in the GUI for branding purposes.
- **`Palm Print.png`**: Image file displayed on the main window.

## Troubleshooting

- **Invalid Key**: If an invalid clearance key is entered, you will have up to 3 attempts to enter the correct key before the application exits.
- **File Errors**: Ensure that the `Sensitive` folder and the required files are present in the correct directory.
