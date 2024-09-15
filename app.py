import numpy as np
import time
import os
from itertools import combinations
from PIL import Image
import streamlit as st

# Function to get candidate states
def get_candidates(before):
    candidates = []
    indices = [i for i, pin in enumerate(before) if pin == '0'] 

    for r in range(1, len(indices) + 1):  
        for combo in combinations(indices, r):
            after = list(before)
            for idx in combo:
                after[idx] = '1' 
            candidates.append(''.join(after))
    
    return candidates

# Function to simulate throwing the ball
def throw_ball(before):
    if before == '1111111111':
        return '0000000000'
    candidates = get_candidates(before)
    after = np.random.choice(candidates)
    time.sleep(1)
    return after

# Function to display the current pin status side-by-side
def show(before, after):
    col1, col2 = st.columns(2)  # Define two columns with equal width

    with col1:
        path_before = os.path.join('data', before + '.png')
        img_before = Image.open(path_before)
        st.image(img_before, caption="Before Throw", width=300)  # Adjust width as needed

    with col2:
        path_after = os.path.join('data', after + '.png')
        img_after = Image.open(path_after)
        st.image(img_after, caption="After Throw", width=300)  # Adjust width as needed

# Streamlit app setup
st.title("Bowling Pin Simulation")

# Initialize session state to store the current pin status
if 'status' not in st.session_state:
    st.session_state.status = '0000000000'
    st.session_state.after_status = '0000000000'  # Added to track the 'after' status

# Display the current pin arrangement
show(st.session_state.status, st.session_state.after_status)

# Add buttons for interaction
if st.button('Throw'):
    st.session_state.after_status = throw_ball(st.session_state.status)
    st.session_state.status = st.session_state.after_status  # Update 'status' to new state
    show(st.session_state.status, st.session_state.after_status)

if st.button('Reset'):
    st.session_state.status = '0000000000'
    st.session_state.after_status = '0000000000'
    show(st.session_state.status, st.session_state.after_status)

