import streamlit as st
import sys
import contextlib
from io import StringIO
from src.main import main

# Page configuration
st.set_page_config(page_title="AutoRefactorOps", page_icon="🤖", layout="wide")

# Title and Description
st.title("🤖 AutoRefactorOps: Multi-Agent System")
st.markdown("""
This control panel allows Llama-powered AI agents to analyze your codebase, 
reduce **Technical Debt**, and perform safe, autonomous **Refactoring** with zero semantic drift.
""")

st.divider()

# Trigger Button
if st.button("🚀 Start Refactoring Pipeline", type="primary", use_container_width=True):
    with st.spinner("Initializing agents and scanning the codebase... Please wait (This may take 1-2 minutes)."):
        
        # Buffer to catch terminal outputs for the Streamlit UI
        output_buffer = StringIO()
        
        with contextlib.redirect_stdout(output_buffer):
            try:
                # Trigger the main Multi-Agent crew
                main()
            except Exception as e:
                print(f"\nAn error occurred during system execution: {str(e)}")
        
        # Success message
        st.success("Pipeline executed successfully! You can review the agents' final report below.")
        
        # Display logs in a text area
        st.text_area("Terminal Logs & Final Report", output_buffer.getvalue(), height=600)
        
st.markdown("---")
st.caption("AutoRefactorOps v1.0 | Developed for Academic Evaluation")