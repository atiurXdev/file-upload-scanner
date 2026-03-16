import requests

def get_auth_token(base_url, email, password):
    url = f"{base_url}/rest/user/login"
    data = {"email": email, "password": password}
    try:
        r = requests.post(url, json=data, timeout=5)
        if r.status_code == 200:
            return r.json()['authentication']['token']
    except:
        pass
    return None

def test_file_upload(base_url, token, filepath, filename):
    url = f"{base_url}/api/Complaints"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        with open(filepath, 'rb') as f:
            files = {'file': (filename, f, 'application/octet-stream')}
            data = {'UserId': 1, 'message': 'test complaint'}
            r = requests.post(url, headers=headers, files=files, data=data, timeout=5)
            return r.status_code
    except Exception as e:
        return str(e)

def run_scan(base_url, email, password, log_callback):
    log_callback("🔐 Logging in to Juice Shop...")
    token = get_auth_token(base_url, email, password)
    
    if not token:
        log_callback("❌ Login failed! Check credentials.")
        return

    log_callback("✅ Login successful!\n")
    log_callback("🔍 Starting File Upload Vulnerability Scan...\n")

    tests = [
        ("payloads/test.jpg",      "test.jpg",        "Normal JPG image"),
        ("payloads/shell.php",     "shell.php",        "PHP Web Shell"),
        ("payloads/shell.gif",     "shell.gif",        "GIF with PHP payload"),
        ("payloads/shell.php.jpg", "shell.php.jpg",    "Double Extension bypass"),
        ("payloads/largefile.jpg", "largefile.jpg",    "Oversized file (6MB)"),
    ]

    results = []
    for filepath, filename, desc in tests:
        status = test_file_upload(base_url, token, filepath, filename)
        if status in [200, 201]:
            result = f"❌ VULNERABLE  | {desc} ({filename}) — Server accepted!"
        elif status == 500:
            result = f"⚠️  WARNING    | {desc} ({filename}) — Server error!"
        else:
            result = f"✅ SAFE        | {desc} ({filename}) — Blocked (HTTP {status})"
        log_callback(result)
        results.append(result)

    log_callback("\n📋 Scan Complete!")

    # Save report
    with open("report.txt", "w") as f:
        f.write("File Upload Vulnerability Scan Report\n")
        f.write(f"Target: {base_url}\n\n")
        for r in results:
            f.write(r + "\n")
    log_callback("💾 Report saved to report.txt")