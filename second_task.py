import re
from typing import Callable
from collections.abc import Iterable

def generator_numbers(text: str) -> Iterable[float]:
    """
    Generator that parses input text and finds all numbers

    Yields:
        Numbers in provided text
    """
    pattern = r"\d+\.\d+"
    parsed_text = re.findall(pattern, text)
    for value in parsed_text:
        yield float(value)
def sum_profit(text: str, func: Callable) -> float:
    """
    Function that uses number generator to calculate total profit

    Returns:
        Total profit
    """
    profit = 0.0
    for number in func(text):
        profit += number
    return profit
