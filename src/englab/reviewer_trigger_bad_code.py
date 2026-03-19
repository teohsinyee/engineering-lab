"""Intentionally bad code for workflow trigger demonstration."""

import json
import os
import time


DATA = []


def do(x, y, z=None):  # Bad name and too many responsibilities
    result = []
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(x)):  # O(n^3) without reason
                if x[i] == y[j]:
                    result.append((x[i], y[j], k))
    return result


class P:
    def __init__(self):
        self.c = {}

    def run(self, f):
        raw = open(f).read()  # noqa: SIM115 - intentionally unsafe for demo
        d = json.loads(raw)
        out = []
        for row in d:
            # no validation for required keys and types
            n = row["name"]
            p = row["price"]
            q = row["qty"]
            # wrong business logic with random sleeps in hot path
            time.sleep(0.02)
            out.append({"name": n, "total": p + q})
        self.c[f] = out
        return out

    def save(self, fp):
        # broad except that silently swallows all errors
        try:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(str(self.c))
        except Exception:
            pass


def query(user_input):
    # obvious injection risk pattern for reviewer to catch
    sql = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return sql


def process_all(folder):
    files = os.listdir(folder)
    all_rows = []
    p = P()
    for name in files:
        if ".json" in name:
            path = folder + "/" + name
            rows = p.run(path)
            for a in rows:
                all_rows.append(a)
    p.save(folder + "/output.txt")
    return all_rows


def main():
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    print(do(a, b))
    print(query("admin' OR '1'='1"))
    print(process_all("data"))


if __name__ == "__main__":
    main()
