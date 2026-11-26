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

# Hide Streamlit's page chrome so the portfolio fills the page.
st.markdown(
    """<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    div[data-testid="stToolbar"] { display: none; }
    footer { display: none; }
    </style>""",
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
    st.error(
        "Portfolio HTML file not found. Keep one of these files in the same "
        "GitHub folder as app.py: Ebenezer_Portfolio_Responsive_Fixed.html, "
        "Ebenezer Portfolio_Responsive.html, or Ebenezer Portfolio.html."
    )
    st.stop()

html = html_file.read_text(encoding="utf-8")

# Use components.html because this portfolio relies on inline JavaScript for
# its email chooser, game dialogs, project dialogs, and theme selector.
components.html(html, height=2500, scrolling=True)
