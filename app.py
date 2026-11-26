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
    """<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    div[data-testid="stToolbar"] { display: none; }
    footer { display: none; }
    iframe { display: block; width: 100%; border: 0; }
    </style>""",
    unsafe_allow_html=True,
)

folder = Path(__file__).resolve().parent
html_file = folder / "Ebenezer_Portfolio_Responsive_Fixed.html"

if not html_file.is_file():
    st.error(
        "Portfolio HTML file not found. Keep "
        "'Ebenezer_Portfolio_Responsive_Fixed.html' in the same folder as app.py."
    )
    st.stop()

html = html_file.read_text(encoding="utf-8")

# A viewport-sized iframe keeps fixed dialogs centred while allowing the
# portfolio itself to scroll. In-page links are handled inside the HTML.
components.html(html, height=720, scrolling=True)
