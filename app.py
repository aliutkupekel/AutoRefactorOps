import streamlit as st
import sys
import contextlib
import re
import os
from io import StringIO
from src.main import main

# Page configuration
st.set_page_config(page_title="AutoRefactorOps", page_icon="⚙️", layout="wide")

def clean_ansi(text):
    """Cleans terminal color codes from the output."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

st.title("⚙️ AutoRefactorOps: Multi-Agent System")
st.markdown("#### Autonomous Technical Debt Reduction & Verification Dashboard")
st.markdown("Developed by Ali, Alperen, Yiğit & Niyazi")
st.divider()

# Dosya Yolları
target_file_path = "evaluation/synthetic_repo/target_smelly.py"
test_file_path = "evaluation/synthetic_repo/test_target.py"

# Arayüzü 2 Sekmeye (Tab) Bölüyoruz
tab1, tab2 = st.tabs(["💻 Code Editor (Input)", "🚀 Pipeline Execution (Dashboard)"])

# ==========================================
# TAB 1: KULLANICI GİRDİSİ (CODE EDITOR)
# ==========================================
with tab1:
    st.markdown("### 📥 Upload or Paste Your Code")
    st.info("📝 **Important:** The Verification Agent relies on Unit Tests. If you change the Target Code, make sure the Pytest Suite matches your new code to ensure zero semantic drift.")
    
    # Mevcut dosyaları oku
    try:
        with open(target_file_path, "r", encoding="utf-8") as f:
            default_code = f.read()
        with open(test_file_path, "r", encoding="utf-8") as f:
            default_test = f.read()
    except Exception:
        default_code = "# Target code goes here..."
        default_test = "# Pytest code goes here..."

    # Yan yana iki kod editörü
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### 1️⃣ Target Python Code (To be Refactored)")
        user_code = st.text_area("Target Code", value=default_code, height=400, label_visibility="collapsed")
    with col_b:
        st.markdown("#### 2️⃣ Pytest Suite (For Verification)")
        user_test = st.text_area("Test Code", value=default_test, height=400, label_visibility="collapsed")

    # Kaydetme Butonu
    if st.button("💾 Save Code & Tests to Workspace", type="secondary"):
        try:
            with open(target_file_path, "w", encoding="utf-8") as f:
                f.write(user_code)
            with open(test_file_path, "w", encoding="utf-8") as f:
                f.write(user_test)
            st.success("✅ Files saved successfully! The agents will now analyze your custom code. Proceed to the next tab.")
        except Exception as e:
            st.error(f"Failed to save files: {str(e)}")

# ==========================================
# TAB 2: OPERASYON VE DASHBOARD
# ==========================================
with tab2:
    # Dashboard Information Cards (4 Agents)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info("🕵️ **Discovery Agent**\n\nScans codebase for high Cyclomatic Complexity.")
    with col2:
        st.warning("👷‍♂️ **Refactoring Agent**\n\nReduces Technical Debt (Delta D) autonomously.")
    with col3:
        st.success("🧐 **Verification Agent**\n\nEnsures Zero Semantic Drift via AST & Tests.")
    with col4:
        st.error("🛡️ **Rollback Agent**\n\nGuarantees safety via Git state saving and rollbacks.")

    st.markdown("---")

    # Trigger Button
    if st.button("🚀 INITIATE AUTONOMOUS PIPELINE", type="primary", use_container_width=True):
        
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        status_text.info("System Initialized. Agents are scanning the workspace... (This may take 1-2 minutes)")
        progress_bar.progress(30)
        
        output_buffer = StringIO()
        
        with contextlib.redirect_stdout(output_buffer):
            try:
                main()
            except Exception as e:
                print(f"\nCRITICAL ERROR: {str(e)}")
                
        progress_bar.progress(100)
        status_text.success("Pipeline Execution Successfully Completed!")
        
        raw_output = output_buffer.getvalue()
        cleaned_output = clean_ansi(raw_output)
        
        st.markdown("### 📊 Final Operation Report")
        
        if "FINAL OPERATION REPORT" in cleaned_output:
            final_report_section = cleaned_output.split("FINAL OPERATION REPORT")[-1]
            final_report_clean = final_report_section.replace("=", "").strip()
            
            # Başarılı ise yeşil, rollback (hata) ise kırmızı kutu göster
            if "SUCCESSFUL MERGE" in final_report_clean:
                st.success(final_report_clean)
            else:
                st.error(final_report_clean)
        else:
            st.warning("System finished, but the final report format was unexpected. See details below.")
        
        with st.expander("🔍 View Detailed Agent Execution Logs (Terminal Output)"):
            st.text(cleaned_output)
            
    st.markdown("---")
    st.caption("AutoRefactorOps v2.0 | Interactive Platform Build")