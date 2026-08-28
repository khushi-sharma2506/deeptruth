import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ledgerPath = path.join(__dirname, 'ledger.json');

const videoHash = process.argv[2];

if (!videoHash) {
    console.error(JSON.stringify({ error: "No video hash provided." }));
    process.exit(1);
}

setTimeout(() => {
    // 1. Mocking the successful interaction with the Midnight Network
    const zkProofTxId = "0x" + Math.random().toString(16).slice(2, 10) + "..." + Math.random().toString(16).slice(2, 6);
    const timestamp = new Date().toISOString();
    
    const record = {
        hash: videoHash,
        transactionId: zkProofTxId,
        timestamp: timestamp,
        status: "Verified Human Creator",
        identity: "REDACTED_ZERO_KNOWLEDGE"
    };

    // 2. Read the current ledger
    let ledger = [];
    if (fs.existsSync(ledgerPath)) {
        const data = fs.readFileSync(ledgerPath, 'utf8');
        if (data) {
            ledger = JSON.parse(data);
        }
    }

    // 3. Prevent duplicates in our mock ledger
    const exists = ledger.find(item => item.hash === videoHash);
    if (!exists) {
        ledger.push(record);
        fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2));
    }

    // 4. Output the result back to Python
    console.log(JSON.stringify({ success: true, message: "Zero-Knowledge proof generated.", ...record }));
    
}, 1500); // 1.5s delay
