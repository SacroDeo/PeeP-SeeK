import subprocess
import os
import re

def search_username(username):
    sherlock_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sherlock'))
    
    try:
        result = subprocess.run(
            ["poetry", "run", "sherlock", username, "--print-found"],
            cwd=sherlock_dir,
            capture_output=True,
            text=True,
            timeout=120
        )

        # Debug: print Sherlock output
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)

        urls = []
        for line in result.stdout.splitlines():
            print("LINE:", repr(line))  # Debug line output
            match = re.match(r"\[\+\]\s+([^\:]+):\s+(https?://[^\s]+)", line)
            if match:
                site = match.group(1).strip()
                url = match.group(2).strip()
                urls.append({"site": site, "url": url})

        if not urls:
            return {"results": [], "message": "No profiles found."}

        return {"results": urls}

    except subprocess.TimeoutExpired:
        return {"error": "Username search timed out. Try again later."}
    except Exception as e:
        return {"error": str(e)}
