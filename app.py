"""Streamlit launcher for Ebenezer's interactive HTML portfolio."""
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
    """
    <style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"],
    div[data-testid="stToolbar"],
    footer { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

folder = Path(__file__).resolve().parent
possible_html_files = [
    folder / "Ebenezer_Portfolio_Responsive_Fixed.html",
    folder / "Ebenezer Portfolio_Responsive.html",
    folder / "Ebenezer Portfolio.html",
]
html_file = next((path for path in possible_html_files if path.is_file()), None)

if html_file is None:
    st.error("Portfolio HTML file not found. Keep the HTML file in the same GitHub folder as app.py.")
    st.stop()

html = html_file.read_text(encoding="utf-8")

# A 720px iframe viewport keeps fixed-position dialogs centred in the
# visible portfolio area. The long portfolio scrolls inside the iframe.
components.html(html, height=720, scrolling=True)
