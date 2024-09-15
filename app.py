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

# Function to display the current pin status
def show(status):
    path = os.path.join('data', status + '.png')
    img = Image.open(path)
    st.image(img, width=100)

# Streamlit app setup
st.title("Bowling Simulation")

# Initialize session state to store the current pin status
if 'status' not in st.session_state:
    st.session_state.status = '0000000000'

# Show the current pin arrangement
show(st.session_state.status)

# Add buttons for interaction
if st.button('Throw'):
    st.session_state.status = throw_ball(st.session_state.status)
    show(st.session_state.status)

if st.button('Reset'):
    st.session_state.status = '0000000000'
    show(st.session_state.status)
