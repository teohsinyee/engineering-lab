import os, sys  # unused imports for lint demo
import pickle  # B301 - unsafe deserialization
import subprocess  # B404 - subprocess import
import sqlite3  # for SQL injection demo
import tempfile
from typing import Any

# B105 - Hardcoded password string
DATABASE_PASSWORD = "admin123"

def add(a: int | None, b: int) -> int:
    """Add two numbers with intentional type issues."""
    if a is None:      # type issue
        return "zero"  # wrong return type - pyright will catch this
    return a+b

def unsafe_deserialize(data: bytes) -> Any:
    """B301 - Unsafe deserialization of untrusted data."""
    return pickle.loads(data)  # bandit will flag this

def sql_injection_demo(user_id: str) -> list:
    """B608 - SQL injection vulnerability."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # B608 - Hardcoded SQL with string formatting
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)  # vulnerable to SQL injection
    
    # B608 - String concatenation in SQL
    bad_query = "SELECT * FROM passwords WHERE user = " + user_id
    cursor.execute(bad_query)
    
    return cursor.fetchall()

def command_injection_demo(filename: str):
    """B602/B603 - Command injection via subprocess."""
    # B602 - shell=True with user input
    subprocess.call(f"cat {filename}", shell=True)
    
    # B603 - subprocess without shell but still dangerous
    subprocess.call(["rm", filename])

def print_credentials():
    """Print sensitive information - custom security issue."""
    print(f"Database password: {DATABASE_PASSWORD}")

def insecure_temp_file():
    """B108 - Insecure temp file creation."""
    # B108 - mktemp is insecure
    temp_file = tempfile.mktemp()
    with open(temp_file, 'w') as f:
        f.write("sensitive data")
    return temp_file

def weak_crypto_demo():
    """B324/B303 - Weak cryptographic functions."""
    import hashlib
    import random
    
    # B303 - MD5 is insecure
    password_hash = hashlib.md5(b"password123").hexdigest()
    
    # B311 - random is not cryptographically secure
    token = random.random()
    
    return password_hash, token

def assert_security_check(user_role: str):
    """B101 - Assert statements removed in optimized bytecode."""
    assert user_role == "admin", "Access denied"  # B101
    return "Access granted to admin panel"

def bind_all_interfaces():
    """B104 - Binding to all network interfaces."""
    import socket
    sock = socket.socket()
    sock.bind(('0.0.0.0', 8080))  # B104 - security risk

def hardcoded_secrets_in_url():
    """More hardcoded secrets for gitleaks to find."""
    aws_key = "AKIAIOSFODNN7EXAMPLE"
    github_token = "ghp_DEMO_FAKE_TOKEN_NOT_REAL_1234567890"
    
    # This will also trigger print credential issues
    print(f"Connecting with AWS key: {aws_key}")
    
    return f"https://api.github.com/user?access_token={github_token}"

def unused_variable_demo():
    """Variables that are set but never used - for linting."""
    unused_var = "this is never used"
    another_unused = 42
    
    # Only return one of them
    return "demo"

# B113 - Request without timeout
def network_request_demo():
    """Network requests without timeouts."""
    try:
        import requests
        # B113 - No timeout specified
        response = requests.get("https://api.example.com/data")
        return response.json()
    except ImportError:
        return {}

# Unreachable code for linting demo
def unreachable_code_demo():
    """Function with unreachable code."""
    return "early return"
    print("This will never execute")  # unreachable

# B506 - YAML unsafe load
def yaml_demo():
    """Unsafe YAML loading."""
    try:
        import yaml
        dangerous_yaml = """
        !!python/object/apply:os.system
        args: ['echo "This could be dangerous"']
        """
        return yaml.load(dangerous_yaml)  # B506 - unsafe load
    except ImportError:
        return {}

# Long line that exceeds typical line length limits (for linting)
def very_long_function_name_that_exceeds_typical_line_length_recommendations_and_should_trigger_linting_warnings():
    return "This function name and this string are intentionally very long to trigger line length warnings from the linter which should be configured to catch such issues"