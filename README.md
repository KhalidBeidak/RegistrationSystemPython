# Student Registration System in Python

A lightweight, terminal-based Student and Course Registration Management System written in Python. This project allows users to manage student profiles, assign courses, view detailed student information, and securely remove records using flat-file persistence.

---

## Features

* **Add Student:** Register new students with unique identifiers and names.
* **Add Course for a Student:** Assign and link specific courses to registered student profiles.
* **Show Student Information:** Retrieve and display comprehensive details about individual students along with their registered courses.
* **Delete Student:** Safely remove student records and their associated course assignments from the database.
* **Persistent Storage:** Automatically initializes and manages flat text files (`students.txt` and `courses.txt`) to ensure data is saved between application sessions.

---

## Project Structure

```text
RegistrationSystemPython/
│
├── main.py                 # Entry point containing the application menu loop and UI logic
├── functions.py            # Core implementation of student/course management logic and file I/O
├── students.txt            # Database file for student records (auto-generated)
└── courses.txt             # Database file for course records (auto-generated)
```

---

## Getting Started & Installation

### Option A: Windows Setup (MSYS2, VS Code & Python)

To run this project smoothly inside Visual Studio Code on Windows, you can utilize the MSYS2 environment terminal.

#### 1. Install MSYS2 via Command Prompt (CMD)
If you do not have MSYS2 installed yet, you can quickly install it using Windows Command Prompt:
* Open **Command Prompt** as Administrator.
* If you have `winget` installed (standard on modern Windows 10/11), run:
  ```cmd
  winget install msys2.msys2
  ```
* Alternatively, download and run the installer directly from the [Official MSYS2 Website](https://www.msys2.org/). Follow the default installation prompts (usually installing to `C:\msys64`).

Once installed, open your MSYS2 terminal and install Python:
```bash
pacman -Syu
pacman -S mingw-w64-ucrt64-python
```

#### 2. Install VS Code and Extensions
* Download and install **Visual Studio Code**.
* Open VS Code and install the following recommended extensions from the Extensions Marketplace (`Ctrl + Shift + X`):
  * **Python** (by Microsoft) - For linting, debugging, and syntax support.
  * **GitLens** or **Git Graph** (Optional) - For version control tracking.

#### 3. Install/Clone the Project File
* Clone this repository or download the ZIP file and extract it.
* Place the folder directly in the root of your `C:` drive and rename/ensure it reads:
  ```text
  C:\RegistrationSystemPython
  ```

#### 4. Open in VS Code & Configure Terminal
* Open VS Code and go to **File > Open Folder...**, then select `C:\RegistrationSystemPython`.
* Open the integrated VS Code terminal (`Ctrl + ~`).
* Switch your terminal session to the native MSYS2 environment by running:
  ```bash
  C:\msys64\usr\bin\bash.exe --login -i
  ```
  *(Tip: You can set this as your default VS Code terminal profile via `Terminal: Select Default Profile` in the Command Palette).*

#### 5. Run the Application
* Execute the Python program directly from your terminal:
  ```bash
  python main.py
  ```

---

### Option B: Linux / macOS Setup

If you are running the project on a UNIX-based system, the workflow utilizes your native terminal toolchain:

#### 1. Prerequisites
* Ensure you have **Python 3.x** installed on your system.
* Verify that you have **VS Code** installed along with the **Python** extension.

#### 2. Clone and Open the Project in VS Code
* Open your terminal and clone the repository to your local machine:
  ```bash
  git clone https://github.com/YOUR_USERNAME/RegistrationSystemPython.git
  cd RegistrationSystemPython
  ```
* Open the folder in VS Code:
  ```bash
  code .
  ```

#### 3. Run the Application
* Open the integrated terminal in VS Code and run the application:
  ```bash
  python3 main.py
  ```

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)