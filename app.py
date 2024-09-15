import numpy as np
import time
import os
import cv2
from itertools import combinations
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
    # Simulate a sound by pausing (you can integrate sound later if needed)
    time.sleep(3)
    return after

# Function to display the current pin status
def show(status):
    path = os.path.join('path_to_images', status + '.png')
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, width=200)

# Streamlit app setup
st.title("Bowling Pin Simulation")

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
