from typing import List


class RequestDto:
    numbers: List[int]

    def __init__(self, numbers: List[int]) -> None:
        self.numbers = numbers
