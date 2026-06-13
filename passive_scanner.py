class PassiveScanner:
    def __init__(self):
        self.findings = []

    def scan(self, response_data: dict):
        self.findings = []
        self.check_security_headers(response_data)
        self.check_information_disclosure(response_data)
        self.check_cookies(response_data)
        return self.findings

    def check_security_headers(self, response_data):
        headers = response_data.get("headers", {})
        security_headers = {
            "Content-Security-Policy": "Missing CSP header",
            "X-Frame-Options": "Missing X-Frame-Options (Clickjacking risk)",
            "X-XSS-Protection": "Missing XSS Protection header",
            "Strict-Transport-Security": "Missing HSTS header"
        }
        for header, issue in security_headers.items():
            if header not in headers:
                self.findings.append({"type": "Security Header", "severity": "Medium", "issue": issue})

    def check_information_disclosure(self, response_data):
        body = response_data.get("body", "").lower()
        if "sql syntax" in body:
            self.findings.append({"type": "Information Disclosure", "severity": "Low", "issue": "Possible sensitive info: sql syntax"})

    def check_cookies(self, response_data):
        headers = response_data.get("headers", {})
        cookies = headers.get("Set-Cookie", "")
        if cookies and "HttpOnly" not in cookies:
            self.findings.append({"type": "Cookie Security", "severity": "Medium", "issue": "Missing HttpOnly flag"})

    def report(self):
        print("\n========== PASSIVE SCAN REPORT ==========")
        for i, finding in enumerate(self.findings, 1):
            print(f"[{i}] Type: {finding['type']} | Severity: {finding['severity']} | Issue: {finding['issue']}")

if __name__ == "__main__":
    sample_response = {"headers": {"Content-Type": "text/html"}, "body": "<html><h1>SQL syntax error</h1></html>"}
    scanner = PassiveScanner()
    scanner.scan(sample_response)
    scanner.report()
