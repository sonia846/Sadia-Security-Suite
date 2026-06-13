import requests
import threading
from queue import Queue

class ActiveScanner:
    def __init__(self):
        self.findings = []
        # Common hidden directories to hunt for
        self.wordlist = [
            "admin", "login", "config.php", "wp-admin", "backup", 
            "db", "api", "v1", "secret", "dev", "git"
        ]
        self.print_lock = threading.Lock()

    def check_directory(self, target_url, directory, queue):
        while True:
            dir_to_check = queue.get()
            if dir_to_check is None:
                break
                
            # Construct real test URL
            base_url = target_url.rstrip('/')
            test_url = f"{base_url}/{dir_to_check}"
            
            try:
                headers = {'User-Agent': 'Mozilla/5.0 CyberHunter/1.0'}
                response = requests.get(test_url, headers=headers, timeout=3, allow_redirects=False)
                
                # Agar Status Code 200 (OK) ya 301/302 (Redirect) mile to directory maujood hai
                if response.status_code in [200, 301, 302, 403]:
                    severity = "High" if response.status_code == 200 else "Medium"
                    score = 7.5 if response.status_code == 200 else 5.0
                    
                    finding = {
                        "type": "Directory Discovery",
                        "item": f"/{dir_to_check}",
                        "severity": severity,
                        "score": score,
                        "issue": f"Exposed directory found: {test_url} (Status: {response.status_code})"
                    }
                    
                    with self.print_lock:
                        self.findings.append(finding)
                        print(f"[+] [FOUND] Status {response.status_code} -> /{dir_to_check}")
                        
            except requests.exceptions.RequestException:
                pass
                
            queue.task_done()

    def scan_target(self, target_url, thread_count=5):
        print(f"\n[*] Launching Multi-Threaded Active Directory Brute-Force ({thread_count} threads)...")
        self.findings = []
        
        # Threading Queue setup
        path_queue = Queue()
        for path in self.wordlist:
            path_queue.put(path)
            
        threads = []
        # Start multiple parallel threads for pro-speed
        for i in range(thread_count):
            t = threading.Thread(target=self.check_directory, args=(target_url, path_queue, path_queue))
            t.start()
            threads.append(t)
            
        path_queue.join()
        
        # Stop threads
        for i in range(thread_count):
            path_queue.put(None)
        for t in threads:
            t.join()
            
        return self.findings

    def report(self):
        print("\n============= ACTIVE SCAN AUDIT =============")
        if not self.findings:
            print("[-] No significant open directories discovered from wordlist.")
        else:
            for i, finding in enumerate(self.findings, 1):
                print(f"[{i}] [{finding['severity']} - Score: {finding['score']}] {finding['item']} -> {finding['issue']}")
        print("==============================================")

if __name__ == "__main__":
    # Local module test
    scanner = ActiveScanner()
    scanner.scan_target("http://example.com", thread_count=5)
    scanner.report()
