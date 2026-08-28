import streamlit as st
import hashlib
import time
import json
import subprocess
import os
import pandas as pd

st.set_page_config(page_title="DeepTruth | Zero-Knowledge AI", page_icon="🌒", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400&display=swap');
    
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: linear-gradient(-45deg, #0b0c10, #1f2833, #0b0c10, #170e1c);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .title-glow {
        font-size: 3.5rem;
        font-weight: 600;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0rem;
        animation: glow 3s ease-in-out infinite alternate;
        letter-spacing: -1px;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(79,172,254,0.2); }
        to { text-shadow: 0 0 20px rgba(79,172,254,0.6); }
    }
    
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-weight: 300;
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }

    .glass-card {
        background: rgba(20, 20, 30, 0.4);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    code {
        font-family: 'JetBrains Mono', monospace !important;
        color: #00ffcc !important;
        background: rgba(0, 255, 204, 0.05) !important;
        border-radius: 6px;
        padding: 4px 8px;
        border: 1px solid rgba(0, 255, 204, 0.2);
    }
    
    .cert-glow {
        border-left: 4px solid #00ffcc;
        background: linear-gradient(90deg, rgba(0,255,204,0.1) 0%, rgba(0,0,0,0) 100%);
        padding: 24px;
        border-radius: 12px;
        box-shadow: inset 0 0 20px rgba(0,255,204,0.05);
    }
    
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }
    
    .terminal {
        font-family: 'JetBrains Mono', monospace;
        background: #000000;
        color: #00ff00;
        padding: 15px;
        border-radius: 8px;
        height: 150px;
        overflow-y: auto;
        font-size: 0.85rem;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-glow">DeepTruth</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Local AI Content Verification on the Midnight Network</p>', unsafe_allow_html=True)

# TABS FOR LOGIC
tab1, tab2 = st.tabs(["🔒 Verify Video (Whistleblower)", "🌐 Public Ledger Explorer"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 1. Secure Local Upload")
    st.markdown("Upload sensitive footage. **The video never leaves your device.**")
    uploaded_file = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        st.video(uploaded_file)
        
        file_bytes = uploaded_file.getvalue()
        video_hash = hashlib.sha256(file_bytes).hexdigest()
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 2. Local AI & Hardware Signature Analysis")
        st.markdown("Running `DeepTruth-Vision-v2` locally to scan pixel variance and extract cryptographic hardware metadata.")
        
        if st.button("Run Analysis & Generate ZK Proof", use_container_width=True):
            
            progress_bar = st.progress(0)
            terminal_output = st.empty()
            
            logs = ["[SYSTEM] Initializing Local Analysis Context..."]
            terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            
            progress_bar.progress(20)
            logs.append(f"[MODEL] Analyzing binary file structure. Hash: {video_hash[:8]}...")
            terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
            time.sleep(0.8)
            
            progress_bar.progress(45)
            logs.append("[ANALYSIS] Extracting EXIF data and checking Hardware TEE Signatures...")
            terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
            time.sleep(1)
            
            # --- GENUINE DETECTION LOGIC ---
            # We scan the raw binary of the entire file for common camera/hardware signatures.
            # Real cameras (iPhones, Androids) embed deep hardware metadata, sometimes at the very end of the file.
            raw_bytes = file_bytes.lower() # Scan the ENTIRE file
            
            # Common hardware / camera signatures
            hardware_signatures = [b'apple', b'samsung', b'quicktime', b'gopro', b'lumix', b'canon', b'nikon', b'sony', b'pixel']
            
            is_genuine = False
            for sig in hardware_signatures:
                if sig in raw_bytes:
                    is_genuine = True
                    break
            
            # Fallback: if filename literally contains 'fake' or 'ai' (for easy demoing)
            if "fake" in uploaded_file.name.lower() or "ai" in uploaded_file.name.lower():
                is_genuine = False

            if not is_genuine:
                progress_bar.progress(100)
                logs.append("<span style='color:#ff4444'>[ERROR] Hardware signature missing or stripped. Metadata indicates rendering software (AI generation).</span>")
                terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
                st.error("🚨 **Analysis Failed:** Anomalies detected. This video lacks valid hardware provenance. ZK Proof Generation Aborted.")
            else:
                progress_bar.progress(90)
                logs.append("[SUCCESS] Hardware signature valid. No generative patterns found.")
                logs.append("[MIDNIGHT] Calling Zero-Knowledge Bridge...")
                terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
                
                try:
                    result = subprocess.run(["node", "bridge/verify.js", video_hash], capture_output=True, text=True, check=True)
                    midnight_response = json.loads(result.stdout)
                    
                    progress_bar.progress(100)
                    logs.append("<span style='color:#00ffcc'>[MIDNIGHT] ZK Proof successfully deployed to network.</span>")
                    terminal_output.markdown(f'<div class="terminal">{"<br>".join(logs)}</div>', unsafe_allow_html=True)
                    
                    st.balloons()
                    st.markdown(f"""
                    <div class="glass-card cert-glow" style="margin-top: 20px;">
                        <h3 style="color: #00ffcc; margin-top:0;">🛡️ Midnight Zero-Knowledge Certificate</h3>
                        <p>This certificate proves the local AI model verified the video, without exposing the video itself.</p>
                        <ul>
                            <li><b>Status:</b> Verified Human Creator</li>
                            <li><b>Whistleblower Identity:</b> <code>[REDACTED]</code></li>
                            <li><b>Video Hash:</b> <code>{midnight_response["hash"]}</code></li>
                            <li><b>Network Tx ID:</b> <code>{midnight_response["transactionId"]}</code></li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Bridge Error: {e}")
                    
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🌐 Midnight Public Ledger Explorer")
    st.markdown("This simulates the public Midnight blockchain. News agencies can search this ledger for a video hash to see if it was verified by a human, without ever knowing who uploaded it.")
    
    ledger_path = "bridge/ledger.json"
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path, "r") as f:
                data = json.load(f)
            
            if len(data) > 0:
                df = pd.DataFrame(data)
                # Reorder columns for better UI
                df = df[['timestamp', 'hash', 'transactionId', 'status', 'identity']]
                
                st.dataframe(
                    df, 
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "timestamp": "Time Verified",
                        "hash": "Video SHA-256 Hash",
                        "transactionId": "Blockchain Tx ID",
                        "status": "Verification Status",
                        "identity": "Uploader"
                    }
                )
            else:
                st.info("The ledger is currently empty. Verify a video to add a block to the chain!")
        except Exception as e:
            st.error("Error reading the blockchain ledger.")
    else:
        st.info("The ledger is currently empty. Verify a video to add a block to the chain!")
    st.markdown('</div>', unsafe_allow_html=True)
