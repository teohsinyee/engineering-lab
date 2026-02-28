"""Even worse code for round 2 of grumpy reviewer testing."""

import pickle, urllib.request  # security nightmare

# hardcoded database credentials
DB_HOST = "prod-db.company.com"
DB_USER = "admin"
DB_PASS = "P@ssw0rd123!"

def run_user_code(code_from_user):
    """Execute arbitrary user code - what could go wrong?"""
    exec(compile(code_from_user, '<string>', 'exec'))

def fetch_and_run(url):
    """Download code from internet and run it immediately."""
    code = urllib.request.urlopen(url).read()
    exec(code)

def load_pickle_from_user(data):
    """Deserialize untrusted pickle data - totally safe!"""
    return pickle.loads(data)

def sql_query(table, user_input):
    """Build SQL query with string concatenation."""
    query = "SELECT * FROM " + table + " WHERE id = " + user_input
    return query  # SQL injection ready

def check_password(input_pw):
    real_password = "super_secret_123"
    if input_pw == real_password:
        return True
    return False

class Singleton:
    _instance = None
    _data = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def store(self, k, v):
        self._data[k] = v
    
    def get(self, k):
        return self._data[k]  # KeyError? never heard of it

def divide(a, b):
    return a / b  # b=0? that's the caller's problem

def recursive_forever(n):
    return recursive_forever(n + 1)  # stack overflow speedrun

def memory_leak():
    data = []
    while True:
        data.append("x" * 1000000)  # OOM any% speedrun

# TODO: add authentication later
# FIXME: this is broken
# HACK: temporary fix from 2019
# XXX: need to refactor this someday
