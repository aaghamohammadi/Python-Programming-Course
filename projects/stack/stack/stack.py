class Stack:
    CAPACITY: int = 10

    def __init__(self) -> None:
        self.__items = []

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def is_full(self) -> bool:
        return len(self.__items) == self.CAPACITY

    def push(self, item: int) -> None:
        if type(item) != int:
            raise TypeError("The item must be an integer")
        if not self.is_full():
            self.__items.append(item)
        else:
            raise OverflowError("Stack Overflow Error")

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.__items.pop()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.__items[-1]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        items = f"{self.__items}"
        return f"{self.__class__.__name__}({items[1:-1]})"
