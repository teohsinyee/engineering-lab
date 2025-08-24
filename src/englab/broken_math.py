import os, sys  # unused imports for lint demo

def add(a: int, b: int) -> int:
    if a is None:      # type issue
        return "zero"  # wrong return type
    return a+b
