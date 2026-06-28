import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")
st.title("Number Guessing Game")
st.write("Welcome to the Number Guessing Game! Try to guess the number between")
         
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False 
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.feedback = "Game reset! Try to guess the new number"

if not st.session_state.game_over:
    with st.form(key="guess_form", clear_on_submit=True):
       user_guess = st.number_input("Enter your guess:",
            min_value=1, max_value=100, step=1, help="Guess a number between 1 and 100")
       submit_button = st.form_submit_button("Submit Guess")

if submit_button:
    st.session_state.attempts += 1
    if user_guess < st.session_state.secret_number:
        st.session_state.feedback = f"📈 Too low! Try again. (Attempts: {st.session_state.attempts}"
    elif user_guess > st.session_state.secret_number:
        st.session_state.feedback = f"📉 Too high! Try again. (Attempts: {st.session_state.attempts})"
    else:
        st.session_state.feedback = f"Congratulations! You've guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts."
        st.session_state.game_over = True

if st.session_state.feedback:
    if st.session_state.game_over:
        st.success(st.session_state.feedback)
        st.balloons()
    else:
        st.info(st.session_state.feedback)

if st.session_state.game_over or st.button("Reset Game"):
    if st.button("Play Again" if st.session_state.game_over else "Confirm Reset", on_click=reset_game):
        st.rerun()