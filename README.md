# Mental Health Advisor

This is a web-based application designed to provide users with advice based on their responses to a series of questions. The application guides the user through five questions and offers advice at the end based on their answers. The application is built using Flask and Pandas.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Features

- Provides a series of questions for users to answer.
- Offers advice based on the user's responses.
- Simple and easy-to-use interface.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/mental-health-advisor.git
    cd mental-health-advisor
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Open your web browser** and navigate to `http://127.0.0.1:5000` to start using the application.

## Usage

- The application will prompt you with a series of questions.
- Enter your response (a number between 1 and 3) in the provided input box and press "Next".
- After answering five questions, you will receive advice based on your responses.

## File Structure

```plaintext
mental-health-advisor/
│
├── app.py                  # The main Flask application
├── templates/
│   └── index.html          # The main HTML file for the UI
├── static/
│   ├── css/
│   │   └── styles.css      # CSS file for styling the UI
├── question.csv            # CSV file containing the questions and options
├── advice.csv              # CSV file containing the response keys and corresponding advice
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation (this file)
