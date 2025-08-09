import os
import re

# Pattern to match possible sensitive values (simple masking)
SENSITIVE_PATTERNS = [
    r"api[_-]?key",
    r"secret",
    r"password",
    r"token"
]

def mask_value(value):
    """Mask most of the value to avoid leaking secrets."""
    if not value:
        return ""
    if len(value) <= 4:
        return "***"
    return value[:2] + "***" + value[-2:]

def run(**kwargs):
    """Return environment variables with sensitive data masked."""
    try:
        env_vars = os.environ.items()
        safe_env = []
        for key, value in env_vars:
            if any(re.search(pattern, key, re.IGNORECASE) for pattern in SENSITIVE_PATTERNS):
                safe_env.append(f"{key}=***masked***")
            else:
                # Limit value length
                safe_env.append(f"{key}={mask_value(value) if len(value) > 50 else value}")
        # Limit to first 20 environment variables
        result = "\n".join(safe_env[:20])
    except Exception as e:
        result = f"[environment error] {e}"

    print("[*] environment module executed")
    return result
