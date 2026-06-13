import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_dir="."):
        self.output_dir = output_dir

    def generate_html_report(self, summary: dict, filename="report.html"):
        html_content = f"""
        <html>
        <head>
            <title>CyberSecuritySuite Report</title>
            <style>
                body {{ font-family: Arial; background: #0f172a; color: #fff; padding: 20px; }}
                .box {{ padding: 15px; margin: 10px 0; background: #1e293b; border-radius: 10px; border-left: 5px solid #ef4444; }}
                h1 {{ color: #38bdf8; }}
                h2 {{ color: #fbbf24; }}
                .meta {{ color: #94a3b8; font-size: 0.9em; }}
            </style>
        </head>
        <body>
        <h1>CyberSecuritySuite - Security Report</h1>
        <p class="meta">Generated At: {datetime.now().isoformat()}</p>
        <div class="box">
            <h2>Summary</h2>
            <p><strong>Total Vulnerabilities:</strong> {summary.get('total_vulnerabilities')}</p>
            <p><strong>Risk Score:</strong> {summary.get('risk_score')}</p>
            <p><strong>Risk Level:</strong> <span style="color: #ef4444; font-weight: bold;">{summary.get('risk_level')}</span></p>
        </div>
        <h2>Vulnerability Details:</h2>
        """
        for vtype, items in summary.get("by_type", {}).items():
            for item in items:
                html_content += f"""
                <div class="box">
                    <h3>[{vtype}]</h3>
                    <p>{item.get('issue', 'No detail')}</p>
                </div>
                """
        html_content += "</body></html>"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename

    def generate_json_report(self, summary: dict, filename="report.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=4)
        return filename

    def generate_all(self, summary: dict):
        return {
            "html": self.generate_html_report(summary),
            "json": self.generate_json_report(summary)
        }

if __name__ == "__main__":
    sample_summary = {
        "total_vulnerabilities": 3,
        "risk_score": 50,
        "risk_level": "HIGH",
        "by_type": {
            "Security Header": [{"issue": "Missing CSP header"}],
            "Information Disclosure": [{"issue": "Possible sensitive info: sql syntax"}],
            "Cookie Security": [{"issue": "Missing HttpOnly flag"}]
        }
    }
    generator = ReportGenerator()
    reports = generator.generate_all(sample_summary)
    print("\n========== REPORT GENERATOR SYSTEM ==========")
    print("[+] Status: Success!")
    for k, v in reports.items():
        print(f"[+] Generated {k.upper()} Report: {v}")
    print("=============================================\n")
