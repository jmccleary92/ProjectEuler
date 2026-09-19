"""Run a Project Euler problem module by number.
Each problem should live in `problems/problem_XXX.py` and expose a `solve()` function.
Usage: `python run_problem.py 1` or `python run_problem.py 001`
"""
import sys
import importlib
import time


def run(problem_num: str) -> int:
    try:
        n = int(problem_num)
    except ValueError:
        print("Problem number must be an integer")
        return 1
    mod_name = f"problems.problem_{n:03d}"
    try:
        mod = importlib.import_module(mod_name)
    except Exception as e:
        print(f"Could not import {mod_name}: {e}")
        return 2
    if not hasattr(mod, "solve"):
        print(f"Module {mod_name} has no solve() function")
        return 3
    start = time.perf_counter()
    try:
        res = mod.solve()
    except Exception as e:
        print(f"solve() raised an exception: {e}")
        return 4
    elapsed = time.perf_counter() - start
    print(res)
    print(f"Time: {elapsed:.6f}s")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_problem.py <number>")
        sys.exit(1)
    sys.exit(run(sys.argv[1]))
