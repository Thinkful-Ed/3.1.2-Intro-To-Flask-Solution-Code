# Solution Code: Introduction to Flask

This repository contains a simple Flask application and demonstrates the basic structure and behavior of Python modules.

## File Descriptions
- `app.py`: A basic Flask application that has two routes:
  1. `'/'` which returns "Hello, World!"
  2. `'/error'` which deliberately triggers an error by raising a ValueError
- `main_program.py`: A script that imports and uses `my_module.py`.
- `my_module.py`: A module containing a single function.
  - Which contains a function that uses the following logic:
    - If run directly =>  it indicates it's being run as the main program.
    - If imported => it indicates it's been imported as a module

## Installation
1. Clone this repository.
2. `cd` into the newly created directory.
3. Set up a virtual environment:
   ```shell
   python3 -m venv first_flask_app_env
   ```
4. Activate the virtual environment. Depending on your operating system, use one of the following:
   * On macOS and Linux:
     ```shell
     source first_flask_app_env/bin/activate
     ```
   * On Windows:
     ```shell
     .\first_flask_app_env\Scripts\activate
     ```
5. Install the required packages (Flask should be in the `requirements.txt`):
   ```shell
   pip install -r requirements.txt
   ```
6. Run the Flask project:
   ```shell
   python app.py
   ```

When you navigate to `localhost:5001`, you should see the message "Hello, World!". Navigating to `localhost:5001/error` will trigger the deliberate error.

## Additional Notes
To understand the behavior of the module, you can:
1. Run `main_program.py` to see the import behavior of `my_module.py`.
2. Directly run `my_module.py` to see its behavior when executed as the main program.

If you encounter any issues or need further clarification on any part of this project, please reach out for assistance.