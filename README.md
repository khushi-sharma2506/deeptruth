<div align="center">

# 🕵️‍♂️ DeepTruth

**Zero-Knowledge AI Content Verification for Journalists & Whistleblowers.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat&logo=streamlit)](https://deeptruth-axzrph5jzojzqmijatn5vs.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-43853D?logo=node.js&logoColor=white">
  <img alt="Midnight" src="https://img.shields.io/badge/Midnight_Blockchain-000000?logo=web3dotjs&logoColor=white">
  <img alt="Zero-Knowledge" src="https://img.shields.io/badge/ZK_Proofs-8A2BE2?logo=hive&logoColor=white">
</p>

</div>

---

## 🌍 The Problem

As Generative AI reaches hyper-realism, verifying whether video footage is real or AI-generated is becoming a massive crisis for journalists and human rights activists. 

However, whistleblowers who capture real footage of corruption cannot upload it to cloud-based AI verification tools without risking their identity and safety. Once footage is verified, how do news agencies trust it without exposing the source?

**DeepTruth breaks this dilemma using Zero-Knowledge cryptography.**

---

## 💡 The Solution

DeepTruth solves this using a **Local AI model** and **Midnight's Zero-Knowledge (ZK) Proofs**:
1. A whistleblower uploads a sensitive video to the DeepTruth app. **The video never leaves their device.**
2. A local AI model (`DeepTruth-Vision-v2`) scans the file's binary for cryptographic hardware C2PA signatures to ensure the video is not an AI deepfake.
3. Once verified, the app generates a **Zero-Knowledge Proof** and broadcasts it to the Midnight Blockchain.
4. The blockchain publicly records the video's hash as "Verified Human Content", but the identity of the uploader remains 100% mathematically redacted.

---

## 🏗️ Architecture

DeepTruth uses a hybrid Web2/Web3 architecture to maximize performance and absolute privacy.

```mermaid
graph TD
    %% Define styles
    classDef client fill:#1E293B,stroke:#94A3B8,stroke-width:2px,color:#F8FAFC
    classDef ai fill:#0F766E,stroke:#5EEAD4,stroke-width:2px,color:#F0FDFA
    classDef midnight fill:#6D28D9,stroke:#C4B5FD,stroke-width:2px,color:#F5F3FF
    classDef db fill:#0369A1,stroke:#7DD3FC,stroke-width:2px,color:#F0F9FF

    User([👤 Whistleblower])

    subgraph "1. Client Layer (Python & Streamlit)"
        UI[🖥️ Streamlit Dashboard]
        LocalAI[🤖 Local AI Binary Scanner]
    end

    subgraph "2. The Bridge Layer (Node.js)"
        Bridge[🌉 Midnight JS SDK Bridge]
    end

    subgraph "3. The Blockchain (Midnight Network)"
        Compact[📜 ZK Smart Contract]
        Ledger[(🗄️ Public ZK Ledger)]
    end

    %% Step-by-Step Flow
    User -- "1. Uploads sensitive video" --> UI
    
    UI -- "2. Scans for hardware metadata" --> LocalAI
    
    LocalAI -- "3a. If FAKE (AI generated)" --> Fail[❌ Abort Transaction]
    LocalAI -- "3b. If REAL (Hardware valid)" --> Bridge
    
    Bridge -- "4. Generates ZK Proof" --> Compact
    
    Compact -- "5. Discloses Hash, Redacts Identity" --> Ledger
    
    News([📰 News Agency]) -- "6. Verifies authenticity on public explorer" --> Ledger

    %% Apply Styles
    class UI,Fail client
    class LocalAI ai
    class Bridge,Compact,Ledger midnight
    class News db
```

---

## 🚀 How to Run Locally

### Prerequisites
* Python 3.8+
* Node.js v18+ (If integrating real Midnight Devnet)

### 1. Setup the Python Frontend
```bash
# Install dependencies
pip install -r requirements.txt

# Run the UI
streamlit run app.py
```

### 2. Verify Videos
* Upload any video file.
* Click **Run Analysis & Generate ZK Proof**. 
* Watch the animated terminal logs as the local AI analyzes the video and checks for hardware camera sensors.
* Check the **Public Ledger Explorer** tab to see your verified video hash permanently written to the database!

---

## 📜 Smart Contract Logic
Our smart contract is written in Midnight's **Compact** language (`contracts/deeptruth.compact`):

```typescript
pragma language_version 0.26;

export ledger lastVerifiedVideoHash: Opaque<"string">;

export circuit verifyVideo(videoHash: Opaque<"string">): [] {
    // We intentionally reveal ONLY the video hash to the public ledger.
    // The user's identity and raw video remain completely private.
    lastVerifiedVideoHash = disclose(videoHash);
}
```

---
<div align="center">
<i>Built with ❤️ for the Midnight Hackathon by <b>Khushi Sharma</b></i>
</div>
