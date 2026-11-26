"""Streamlit launcher for Ebenezer's HTML portfolio.

Place this file in the same GitHub repository/folder as
Ebenezer_Portfolio_Responsive_Fixed.html.
"""
from pathlib import Path
import re

import streamlit as st

st.set_page_config(
    page_title="Ebenezer J | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's own page chrome out of the portfolio layout.
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

# Prefer the corrected file. The other names are fallbacks for repositories
# that still contain the earlier HTML filename.
possible_html_files = [
    folder / "Ebenezer_Portfolio_Responsive_Fixed.html",
    folder / "Ebenezer Portfolio_Responsive.html",
    folder / "Ebenezer Portfolio.html",
]
html_file = next((path for path in possible_html_files if path.is_file()), None)

if html_file is None:
    st.error(
        "Portfolio HTML file not found. Put "
        "'Ebenezer_Portfolio_Responsive_Fixed.html' in the same folder as app.py."
    )
    st.stop()

html_document = html_file.read_text(encoding="utf-8")

# st.html() inserts content into the Streamlit page (unlike components.html,
# which creates an iframe). Extract the document's CSS and body contents so
# the portfolio is embedded as a page fragment rather than a nested document.
head_match = re.search(r"<head\b[^>]*>(.*?)</head\s*>", html_document, re.I | re.S)
body_match = re.search(r"<body\b[^>]*>(.*?)</body\s*>", html_document, re.I | re.S)

if not body_match:
    st.error("The portfolio HTML file does not contain a readable body section.")
    st.stop()

head_content = head_match.group(1) if head_match else ""
styles = "\n".join(re.findall(r"<style\b[^>]*>.*?</style\s*>", head_content, re.I | re.S))
body_content = body_match.group(1)
portfolio_fragment = f"{styles}\n{body_content}"

# JavaScript is needed for the theme switcher, copy-email dialog, and interactive
# portfolio features. The direct insertion also lets fixed dialogs use the
# browser viewport instead of an iframe viewport.
st.html(portfolio_fragment, width="stretch", unsafe_allow_javascript=True)
