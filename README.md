# 🕵️‍♂️ DeepTruth: Zero-Knowledge AI Content Verification

![Midnight Hackathon](https://img.shields.io/badge/Midnight-Hackathon-00ffcc?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Zero-Knowledge](https://img.shields.io/badge/ZK-Proofs-8A2BE2?style=for-the-badge)

**DeepTruth** is a privacy-first, anti-deepfake platform built for journalists, whistleblowers, and news agencies during the **Midnight Hackathon (AI Track)**.

## 🌍 The Problem
As Generative AI reaches hyper-realism, verifying whether video footage is real or AI-generated is becoming a massive crisis for journalists and human rights activists. However, whistleblowers who capture real footage of corruption cannot upload it to cloud-based AI verification tools without risking their identity and safety.

## 💡 The Solution (DeepTruth)
DeepTruth solves this using **Midnight's Zero-Knowledge (ZK) Proofs**:
1. A whistleblower uploads a sensitive video to the DeepTruth local app. **The video never leaves their device.**
2. A local AI model (`DeepTruth-Vision-v2`) runs locally to analyze facial landmarks and hardware C2PA signatures to ensure the video is not a deepfake.
3. Once verified, the app generates a **Zero-Knowledge Proof** using the Midnight Blockchain.
4. The blockchain publicly records the video's mathematical hash as "Verified Human Content", but the identity of the uploader remains 100% mathematically redacted.

## 🏗️ Architecture
DeepTruth uses a hybrid Web2/Web3 architecture to maximize performance and privacy:
* **Frontend (Python / Streamlit):** A sleek, glassmorphism UI that runs the local AI simulation and handles video hashing.
* **The Bridge (Node.js):** A local server that translates Python calls into Midnight SDK commands.
* **The Smart Contract (Compact):** A Midnight smart contract that leverages `disclose()` to reveal the video hash to the public ledger while keeping the user's inputs completely private.

## 🚀 How to Run Locally

### Prerequisites
* Python 3.8+
* Node.js v18+

### 1. Setup the Python Frontend
```bash
# Install dependencies
pip install -r requirements.txt

# Run the UI
streamlit run app.py
```

### 2. Verify Videos
* Upload any `.mp4` or `.mov` file.
* Toggle the AI to simulate a real or fake video.
* Click **Generate ZK Proof**. Watch the terminal logs as the local AI analyzes the video and communicates with the Node.js Midnight bridge.
* Check the **Public Ledger Explorer** tab to see your verified video hash permanently written to the database!

## 📜 Smart Contract Logic
Our smart contract is written in Midnight's **Compact** language:
```typescript
pragma language_version 0.23;

export ledger verifiedHashes: Map<Opaque<"string">, boolean>;

export circuit verifyVideo(videoHash: Opaque<"string">): [] {
    // We intentionally reveal ONLY the video hash to the public ledger.
    // The user's identity and raw video remain completely private.
    verifiedHashes.insert(disclose(videoHash), true);
}
```

---
*Built with ❤️ for the Midnight Hackathon.*
