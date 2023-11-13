# Function Caller App

This Flask web application allows users to call functions from different modules based on specified rules.

## Setup

1. Clone the repository:

   ```bash
   git clone <https://github.com/nadavc25/class_test.git>

2. Create a virtual environment:
   ```bash
   python -m venv venv

3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate

4. Install dependencies:
   ```bash
    pip install -r requirements.txt

5. run flask:
   ```bash
    python app.py


The app will be available at http://127.0.0.1:5000/ in your web browser.

Open the application and use the form to select a function and provide inputs.

Click the "Call Function" button to execute the selected function.

Note: Follow the rule that you must call at least one function in the simp module before calling functions in the comp module.

## Rules
The application follows the rule that users cannot call functions in the comp module before calling at least one function in the simp module. An exception will be generated if this rule is violated.
## Project Structure
app.py: Main Flask application file.
tools/: Folder containing modules for number manipulation and collection functions.
numbers/: Folder containing number manipulation modules.
simp.py: Module with simple functions for addition and subtraction.
comp.py: Module with more complex functions for sum of digits and palindrome check.
col.py: Module with collection function.
## Dependencies
Flask: Web framework for Python.
Axios: JavaScript library for making HTTP requests.