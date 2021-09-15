"""
Demo type hints
"""

from typing import Dict, List, Union

a: int = 42
b: float = 2.0
c: bool = True
d: str = "Hello World"

def add(x: int, y: int) -> int:
    return x + y

print(add(4, 5))
# print(add(6, "7"))

def great(name: str = None) -> str:
    if name is None:
        name = "World"
    return "Hello " + name

print(great())
# print(great(100))

e: List[int] = [1, 2, 3]
f: Dict[str, float] = {"location": 4.0, "service": 4.9, "quality": 5.0}
g: Union[int, str] = 1
h: List[Union[int, str]] = [1, 2, "c"]

print(h)

# Type hints for classes
class MyClass:
    value: int = 42

    def __init__(self) -> None:
        pass

    
    def add(self, x: int, y: int) -> int:
        return x + y