import json

class ReportGenerator:
    def __init__(self):
        pass

    def generate_html_report(self, summary_data, filename="sadia_report.html"):
        # JSON backend save
        with open("report.json", "w") as f:
            json.dump(summary_data, f, indent=4)
            
        # HTML Professional Dashboard Structure
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Sadia Cyber Suite Report</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 40px; }}
        .container {{ max-width: 900px; margin: auto; background: #161b22; padding: 30px; border-radius: 10px; border: 1px solid #30363d; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }}
        h1 {{ color: #58a6ff; border-bottom: 2px solid #21262d; padding-bottom: 10px; margin-top: 0; }}
        .meta {{ font-size: 14px; color: #8b949e; margin-bottom: 20px; }}
        .badge {{ padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }}
        .bg-HIGH {{ background-color: #da3633; color: white; }}
        .bg-MEDIUM {{ background-color: #d29922; color: black; }}
        .bg-LOW {{ background-color: #30363d; color: #8b949e; }}
        .summary-box {{ background: #21262d; padding: 20px; border-radius: 6px; margin-bottom: 25px; border-left: 5px solid #58a6ff; }}
        .vuln-card {{ background: #1f242c; padding: 15px; border-radius: 6px; margin-bottom: 15px; border: 1px solid #30363d; }}
        .vuln-title {{ font-weight: bold; font-size: 18px; color: #ff7b72; margin-bottom: 5px; }}
        .score {{ float: right; font-weight: bold; color: #f25858; }}
        .desc {{ font-size: 14px; color: #8b949e; margin-top: 5px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Sadia Security Suite - Scan Assessment Report</h1>
        <div class="meta"><strong>Engine Framework:</strong> Pro-Hunter Mode v1.1.0 | <strong>Author:</strong> Sadia</div>
        
        <div class="summary-box">
            <h3>Executive Summary</h3>
            <p><strong>Total Vulnerabilities Uncovered:</strong> {summary_data['total_vulnerabilities']}</p>
            <p><strong>Calculated Threat Level:</strong> <span class="badge bg-{summary_data['risk_level']}">{summary_data['risk_level']}</span> (Max CVSS Score: {summary_data['max_score']})</p>
        </div>

        <h3>Vulnerability & Exposure Details</h3>
        <div id="vulnerabilities">
        """
        
        # Injecting Findings dynamically into HTML
        if not summary_data['findings']:
            html_content += "<p style='color:#7ee787;'>[+] Perfect! No security gaps found on the target endpoint.</p>"
        else:
            for vuln in summary_data['findings']:
                html_content += f"""
                <div class="vuln-card">
                    <span class="score">CVSS Base: {vuln['score']}</span>
                    <div class="vuln-title">[{vuln['type']}] - {vuln['item']}</div>
                    <div>Severity: <span class="badge bg-{vuln['severity'].upper()}">{vuln['severity']}</span></div>
                    <div class="desc">{vuln['issue']}</div>
                </div>
                """
                
        html_content += """
        </div>
    </div>
</body>
</html>
"""
        with open(filename, "w") as f:
            f.write(html_content)
        print(f"[+] Advanced Dashboard successfully saved to: {filename}")
