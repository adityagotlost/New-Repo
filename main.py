#!/usr/bin/env python3
"""
Beginner-friendly Python basics demo.

Run this file from a terminal:
  python main.py            # uses default name
  python main.py Alice      # greets the given name
"""
from __future__ import annotations

from typing import Dict, List, Optional


def greet_user(name: str) -> str:
    """Return a friendly greeting for the given name."""
    normalized_name = name.strip().title() if name.strip() else "World"
    return f"Hello, {normalized_name}!"


def is_even(number: int) -> bool:
    """Return True if the number is even, else False."""
    return number % 2 == 0


def calculate_factorial(n: int) -> int:
    """Return n! (factorial) for n >= 0 using an iterative loop.

    Raises:
        ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def summarize_numbers(numbers: List[int]) -> Dict[str, Optional[float]]:
    """Compute simple statistics for a list of integers."""
    if not numbers:
        return {
            "count": 0,
            "sum": 0.0,
            "min": None,
            "max": None,
            "average": None,
        }

    total = float(sum(numbers))
    return {
        "count": float(len(numbers)),
        "sum": total,
        "min": float(min(numbers)),
        "max": float(max(numbers)),
        "average": total / len(numbers),
    }


def main() -> None:
    import sys

    # 1) Variables (basic types)
    name_arg = sys.argv[1] if len(sys.argv) > 1 else "world"
    age: int = 20
    height_m: float = 1.75
    is_subscribed: bool = True

    print(greet_user(name_arg))
    print(f"Age: {age}")
    print(f"Height: {height_m} m")
    print(f"Subscribed: {is_subscribed}")

    # 2) Conditionals
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    # 3) Lists and loops
    numbers: List[int] = [1, 2, 3, 4, 5]
    even_numbers: List[int] = [n for n in numbers if is_even(n)]
    squares: List[int] = [n * n for n in numbers]

    print(f"Numbers: {numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Squares: {squares}")

    # For loop example
    for number in numbers:
        if is_even(number):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

    # While loop example
    countdown = 3
    while countdown > 0:
        print(f"Countdown: {countdown}")
        countdown -= 1
    print("Go!")

    # 4) Dictionaries
    person: Dict[str, object] = {
        "name": name_arg.title(),
        "age": age,
        "skills": ["Python", "Git"],
    }
    # Update dictionary
    casted_skills = person["skills"] if isinstance(person.get("skills"), list) else []
    if isinstance(casted_skills, list):
        casted_skills.append("Problem Solving")
    person["skills"] = casted_skills
    print(f"Person: {person}")

    # 5) Functions
    try:
        five_factorial = calculate_factorial(5)
        print(f"5! = {five_factorial}")
    except ValueError as exc:
        print(f"Error calculating factorial: {exc}")

    # 6) Simple stats
    summary = summarize_numbers(numbers)
    print("Summary:", summary)


if __name__ == "__main__":
    main()
