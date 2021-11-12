# Installation using Python 3.6 along another Python version

## 1. Install Python

- Download and install [Win 64bit Version of Python 3.6.8](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe) (add to path, install pip, install for all users if needed)

## 2. Install virtualenv

- Open cmd window and run the following command:
  
    ```console
    pip install virtualenv
    ```

## 3. Clone repository

... to a selected folder on your PC (recommended: using VS Code)

## 4. Create virtualenv and install requirements

- Open the folder and type "cmd" in the address bar of your Windows File Explorer

- Create virtual environment by running the following command:

    ```console
    python -m virtualenv -p python3.6 py36env
    ```

- Activate virtual environment:
  
    ```console
    py36env\Scripts\activate
    ```

- Install requirements in virtual environment:
  
    ```console
    pip install -r requirements.txt
    ```

- Deactivate virtual environment:

    ```console
    deactivate
    ```

- If you use an IDE, you should also select the python interpreter from the virtual environment ("py36env")