import argparse
import sys
from passive_scanner import PassiveScanner
from active_scanner import ActiveScanner
from report_generator import ReportGenerator

def main():
    # Setup CLI Argument Parser (Hacker Layout)
    parser = argparse.ArgumentParser(description="Sadia Security Automation Framework - Pro Hunter Mode")
    parser.add_argument("-u", "--url", required=True, help="Target URL to audit (e.g., example.com)")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of concurrent threads for active scanning (default: 5)")
    parser.add_argument("-o", "--output", default="sadia_report.html", help="Custom HTML report output filename")
    
    args = parser.parse_args()
    target = args.url
    threads = args.threads
    output_file = args.output

    # Program Banner Display
    print(f"""
===========================================================
  ███████╗ █████╗ ██████╗ ██╗ █████╗     ██████╗██████╗ 
  ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗   ██╔════╝██╔══██╗
  ███████╗███████║██║  ██║██║███████║   ██║     ██████╔╝
  ╚════██║██╔══██║██║  ██║██║██╔══██║   ██║     ╚════██╗
  ███████║██║  ██║██████╔╝██║██║  ██║   ╚██████╗██████╔╝
  ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═════╝╚═════╝ 
             SADIA AUTOMATION SECURITY SUITE
  [+] Framework Mode : Pro Hunter  [+] Threads: {threads}
  [+] Platform       : Kali Linux  [+] Author : Sadia
===========================================================""")

    # Initializing Modules
    p_scanner = PassiveScanner()
    a_scanner = ActiveScanner()
    reporter = ReportGenerator()

    # Executing Phase 1
    passive_findings = p_scanner.scan_live_site(target)
    p_scanner.report()

    # Executing Phase 2
    active_findings = a_scanner.scan_target(target, thread_count=threads)
    a_scanner.report()

    # Consolidating Results
    all_findings = passive_findings + active_findings
    total_vulns = len(all_findings)
    
    # Extract Max CVSS Score safely
    scores = [f['score'] for f in all_findings]
    max_score = max(scores) if scores else 0.0
    
    # Industry Grade Threat Level Calculation
    if max_score >= 7.0:
        risk_level = "HIGH"
    elif max_score >= 4.0:
        risk_level = "MEDIUM"
    elif max_score > 0.0:
        risk_level = "LOW"
    else:
        risk_level = "LOW"

    master_summary = {
        "total_vulnerabilities": total_vulns,
        "max_score": max_score,
        "risk_level": risk_level,
        "findings": all_findings
    }

    # Generate Professional HTML Assessment Report
    print("\n[*] Compiling findings into standard CVSS dashboard structure...")
    reporter.generate_html_report(master_summary, filename=output_file)
    print(f"\n[+] MISSION ACCOMPLISHED: Audit report is armed and ready!")
    print("===========================================================\n")

if __name__ == "__main__":
    main()
