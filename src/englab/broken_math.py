import os, sys  # unused imports for lint demo

def add(a: int | None, b: int) -> int:
    if a is None:      # type issue
        return "zero"  # wrong return type
    return a+b
