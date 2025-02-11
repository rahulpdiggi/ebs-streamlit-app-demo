import streamlit as st
import pandas as pd

# Initialize session state to store user answers and score if not already set
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered_questions' not in st.session_state:
    st.session_state.answered_questions = set()

# Sample quiz questions
quiz_data = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Berlin', 'Paris', 'Madrid'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['African Elephant', 'Blue Whale', 'Giraffe', 'Polar Bear'],
        'correct_answer': 'Blue Whale'
    }
]

def calculate_score():
    """Calculate the total score based on correct answers"""
    return len([q for q in st.session_state.answered_questions if 
                st.session_state.user_answers.get(q) == quiz_data[q]['correct_answer']])

# App title and description
st.title('Multiple Choice Quiz')
st.write('Select your answers to see instant feedback!')

# Current score display at the top
total_questions = len(quiz_data)
current_score = calculate_score()
st.metric("Current Score", f"{current_score} / {total_questions}")

# Display all questions
for i, question_data in enumerate(quiz_data):
    st.subheader(f"Question {i + 1}")
    st.write(question_data['question'])
    
    # Create a unique key for each radio button group
    answer_key = f"question_{i}"
    
    # Display radio buttons for options
    selected_answer = st.radio(
        "Select your answer:",
        question_data['options'],
        key=answer_key,
        index=None  # No default selection
    )
    
    # Show instant feedback when an answer is selected
    if selected_answer:
        st.session_state.user_answers[i] = selected_answer
        st.session_state.answered_questions.add(i)
        
        if selected_answer == question_data['correct_answer']:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is: {question_data['correct_answer']}")
    
    st.markdown("---")  # Add a separator between questions

# Reset button
if st.button('Reset Quiz'):
    st.session_state.user_answers = {}
    st.session_state.score = 0
    st.session_state.answered_questions = set()
    st.experimental_rerun()
    