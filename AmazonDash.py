import streamlit as st
import pandas as pd
import plotly.express as px
import os

amazon = pd.read_csv(os.path.join('static','database','amazon.csv'))
amazon
