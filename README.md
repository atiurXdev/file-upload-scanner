cat > README.md << EOF
# File Upload Vulnerability Scanner 🔍

A GUI-based tool to detect file upload vulnerabilities using OWASP Juice Shop.

## Features
- Automatic login to target application
- Tests 5 different file upload attack types
- Generates detailed vulnerability report
- Clean dark-themed GUI

## Vulnerabilities Tested
- PHP Web Shell upload
- GIF with PHP payload
- Double extension bypass
- Oversized file upload
- Normal file upload

## Requirements
- Python 3.x
- Docker (for OWASP Juice Shop)

## Installation
\`\`\`bash
git clone https://github.com/atiurXdev/file-upload-scanner
cd file-upload-scanner
python3 -m venv venv
source venv/bin/activate
pip install requests
\`\`\`

## Setup OWASP Juice Shop
\`\`\`bash
docker run -d -p 3000:3000 bkimminich/juice-shop
\`\`\`

## Usage
\`\`\`bash
python3 main.py
\`\`\`

## Results
| Result | Meaning |
|--------|---------|
| ❌ VULNERABLE | Server accepted dangerous file |
| ✅ SAFE | Server blocked the file |
| ⚠️ WARNING | Server error |

## Tech Stack
- Python
- Tkinter (GUI)
- Requests
- Docker
- OWASP Juice Shop

## Disclaimer
This tool is for educational purposes only.
Use only on systems you own or have permission to test.
EOF