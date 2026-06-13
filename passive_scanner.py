import requests

class PassiveScanner:
    def __init__(self):
        self.findings = []
        # Professional Security Headers jinhe check karna zaroori hai
        self.target_headers = {
            "Content-Security-Policy": {"severity": "Medium", "score": 5.5, "desc": "Missing Content-Security-Policy (CSP) header. Protection against XSS is reduced."},
            "X-Frame-Options": {"severity": "Medium", "score": 4.3, "desc": "Missing X-Frame-Options. Site might be vulnerable to Clickjacking."},
            "X-Content-Type-Options": {"severity": "Low", "score": 3.1, "desc": "Missing X-Content-Type-Options. Vulnerable to MIME-sniffing attacks."},
            "Strict-Transport-Security": {"severity": "High", "score": 7.5, "desc": "Missing Strict-Transport-Security (HSTS). MitM attacks via HTTP downgrade are possible."}
        }

    def scan_live_site(self, target_url):
        print(f"\n[*] Launching Passive Header Audit on: {target_url}")
        self.findings = []
        
        # URL formatting check
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url

        try:
            # Real Network Request using Mozilla User-Agent to avoid getting blocked
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CyberHunter/1.0'}
            response = requests.get(target_url, headers=headers, timeout=5, verify=True)
            
            # Scanning Response Headers
            server_headers = response.headers
            
            for header, info in self.target_headers.items():
                if header not in server_headers:
                    self.findings.append({
                        "type": "Missing Security Header",
                        "item": header,
                        "severity": info["severity"],
                        "score": info["score"],
                        "issue": info["desc"]
                    })
                    
            # Server Banner Information Disclosure check
            if "Server" in server_headers:
                self.findings.append({
                    "type": "Information Disclosure",
                    "item": "Server Banner",
                    "severity": "Low",
                    "score": 2.5,
                    "issue": f"Server banner leaks software info: {server_headers['Server']}"
                })
                
        except requests.exceptions.RequestException as e:
            print(f"[-] Network Connection Error on {target_url}: {e}")
            
        return self.findings

    def report(self):
        print("\n============= PASSIVE SCAN AUDIT =============")
        if not self.findings:
            print("[+] Excellent! All standard security headers are present.")
        else:
            for i, finding in enumerate(self.findings, 1):
                print(f"[{i}] [{finding['severity']} - Score: {finding['score']}] {finding['item']} -> {finding['issue']}")
        print("==============================================")

if __name__ == "__main__":
    # Test script locally to verify framework
    scanner = PassiveScanner()
    scanner.scan_live_site("example.com")
    scanner.report()
