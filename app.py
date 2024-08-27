from flask import Flask, render_template, request, jsonify, session
import pandas as pd

# Load CSV files into DataFrames
questions_df = pd.read_csv('question.csv')
advice_df = pd.read_csv('advice.csv')

def get_next_question_id(current_question_id, response):
    """ Get the next question ID based on current question ID and response """
    question_row = questions_df[questions_df['id'] == current_question_id]
    if not question_row.empty:
        next_question_column = f'next_question_id_option{response}'
        if next_question_column in question_row.columns:
            next_question_id = question_row[next_question_column].values[0]
            if pd.notna(next_question_id):
                return int(next_question_id)
    return None

def get_advice(responses):
    """ Get advice based on user responses """
    response_key = ''.join([str(response) for response in responses])
    advice_df['response_key'] = advice_df['response_key'].astype(str).str.strip()
    advice_row = advice_df[advice_df['response_key'] == response_key]
    if not advice_row.empty:  # Remove parentheses here
        return advice_row['advice'].values[0]
    return "Consult a doctor. They will provide the best advice for your situation."
    

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

@app.route('/')
def index():
    session['responses'] = []
    session['question_count'] = 0
    session['current_question_id'] = 1  # Start with question ID 1
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    """ Get the current question and options """
    if session.get('question_count', 0) >= 5:
        # Return advice if 5 questions have been asked
        return jsonify({'advice': get_advice(session['responses']), 'next_question': None, 'is_last_question': True})
    
    current_question_id = session.get('current_question_id', 1)
    question_row = questions_df[questions_df['id'] == current_question_id]
    if question_row.empty:
        return jsonify({'error': 'Question not found'})
    
    question = question_row['question'].values[0]
    options = [question_row[f'option{i}'].values[0] for i in range(1, 4) if pd.notna(question_row[f'option{i}'].values[0])]
    
    return jsonify({'question': question, 'options': options})

@app.route('/submit_response', methods=['POST'])
def submit_response():
    data = request.json
    current_question_id = session.get('current_question_id', 1)
    response = data['response']
    
    # Update session with the response
    responses = session.get('responses', [])
    responses.append(response)
    session['responses'] = responses
    session['question_count'] = session.get('question_count', 0) + 1

    next_question_id = get_next_question_id(current_question_id, response)
    
    if session['question_count'] >= 5:
        # If 5 questions have been asked, provide advice and end
        return jsonify({'advice': get_advice(responses), 'next_question': None, 'is_last_question': True})
    
    if next_question_id:
        session['current_question_id'] = next_question_id
        return jsonify({'next_question_id': next_question_id, 'is_last_question': False})
    else:
        # Return advice directly if no next question ID is found
        return jsonify({'advice': get_advice(responses), 'next_question': None, 'is_last_question': True})

if __name__ == "__main__":
    app.run(debug=True)
