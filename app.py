"""Streamlit launcher for Ebenezer's existing HTML portfolio."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ebenezer J | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """<style>
    .block-container {padding: 0 !important; max-width: 100% !important;}
    header[data-testid="stHeader"] {display: none;}
    div[data-testid="stToolbar"] {display: none;}
    footer {display: none;}
    iframe {display: block;}
    </style>""",
    unsafe_allow_html=True,
)

html_file = Path(__file__).resolve().parent / "Ebenezer Portfolio.html"

if not html_file.is_file():
    st.error("Could not find 'Ebenezer Portfolio.html'. Put it in the same folder as app.py.")
    st.stop()

html = html_file.read_text(encoding="utf-8")
components.html(html, height=2500, scrolling=True)
