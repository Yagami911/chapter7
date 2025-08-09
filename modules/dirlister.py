import os

def run(**kwargs):
    """List files and directories in the current working directory (safe output)."""
    try:
        entries = os.listdir(".")
        # Limit to first 20 entries to avoid huge data
        safe_entries = entries[:20]
        result = "\n".join(safe_entries)
    except Exception as e:
        result = f"[dirlister error] {e}"

    print("[*] dirlister module executed")
    return result
