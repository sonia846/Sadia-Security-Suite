# █ Sadia Security Suite — Pro Hunter Framework v1.1.0
![Python](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-darkgreen?style=for-the-badge&logo=kalilinux)
![Framework](https://img.shields.io/badge/Framework-Pro--Hunter-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)
An advanced, automated security auditing and reconnaissance framework engineered in **Kali Linux**. This tool is optimized for modern penetration testers and bug bounty hunters to perform high-speed asset evaluation, discover sensitive information leaks, and compute vulnerability severity using standardized grading mechanics.
---
## 🚀 Key Framework Modules
### 1. Multi-Threaded Active Reconnaissance (`active_scanner.py`)
* **Parallel Execution Engine:** Utilizes Python's `threading` and concurrent `Queue` architecture to run synchronous directory validation scans.
* **Speed Optimization:** Drastically reduces directory brute-forcing time from minutes to seconds by handling up to 20 parallel worker threads.
* **Smart Status Assessment:** Inspects HTTP responses (`200`, `301`, `302`, `403`) to pinpoint exposed admin dashboards, configuration backups, and hidden directories.
### 2. Live Passive Header Auditor (`passive_scanner.py`)
* **Real Network Validation:** Drops mock baseline simulations to hit live target endpoints securely using realistic browser user-agents.
* **Security Control Mapping:** Audits critical defensive deployment infrastructure including **Content-Security-Policy (CSP)**, **X-Frame-Options (Clickjacking defense)**, and **HSTS**.
* **Information Disclosure Hunter:** Automatically extracts server banner footprints (e.g., detecting infrastructure hidden behind Cloudflare).
### 3. Industry-Standard Risk Analyzer (`main.py` & `report_generator.py`)
* **Dynamic CLI Execution:** Completely modular terminal workflow powered by `argparse` allowing customized run-time targets and thread scaling (`-u target.com --threads 10`).
* **CVSS Score Integration:** Computes risk severity using standard industrial scales (Critical, High, Medium, Low) assigning exact base vulnerability matrices.
* **Dynamic HTML Dashboard:** Compiles multi-module output telemetry into a clean, modern dark-themed HTML report complete with custom risk badges.
---
## 📊 Sample Assessment Metrics
The suite automatically calculates threats and builds structured vulnerability models:

| Vulnerability Type | Target Core Component | Default Severity | CVSS Base Score | Mitigation Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Missing HSTS** | Strict-Transport-Security | 🔴 HIGH | **7.5** | Prevents MitM HTTP Downgrades |
| **Missing CSP** | Content-Security-Policy | 🟡 MEDIUM | **5.5** | Hardens endpoint against XSS vectors |
| **Missing X-Frame** | X-Frame-Options | 🟡 MEDIUM | **4.3** | Completely mitigates Clickjacking |
| **Leakage Detected** | Server Banner Disclosure | 🔵 LOW | **2.5** | Reduces environmental fingerprinting |

---
## 🛠️ Installation & Pro Execution
### Prerequisites
Ensure your Kali Linux environment runs Python 3. The framework utilizes pre-packaged core system modules.
### Usage
Run the master control file directly from the command-line interface:
```bash
# Standard Quick Scan
python3 main.py -u example.com
# Elite High-Speed Multi-Threaded Hunting Mode
python3 main.py -u target.com --threads 15 --output security_audit.html
