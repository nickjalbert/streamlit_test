import streamlit as st
import numpy as np
import pandas as pd


# Add a selectbox to the sidebar:
dataset = add_selectbox = st.sidebar.radio(
    'Available Datasets:',
    ('Cars', 'Snakes', 'Spiders')
)

# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)
#)


if dataset == 'Cars':
    df = pd.DataFrame({
    'Make': ['Toyota', 'Ford', 'Nissan', 'Mazda'],
    'Model': ['Supra', 'Ranger', 'Maxima', 'Miata'],
    'Year': [1994, 1999, 2002, 2001],
    })
    df
elif dataset == 'Snakes':
    df = pd.DataFrame({
    'Name': ['Black Mamba', 'Garden Snake', 'Python'],
    'Size': ['Medium', 'Small', 'Large'],
    'Venomous': [1, 0, 0],
    })
    df
elif dataset == 'Spiders':
    df = pd.DataFrame({
    'Name': ['Brown Recluse', 'Wolf', 'Sydney Funnel-Web'],
    'Number of Legs': [8, 8, 8],
    'Venomous': [1, 1, 0],
    })
    df
