from abc import ABC


class Job(ABC):
    def __init__(self, salary: int):
        self.salary = salary

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary) -> None:
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be greater than zero")


class Developer(Job):
    def __init__(self, prog_lang: str, salary: int):
        super().__init__(salary)
        self.__prog_lang: str = prog_lang

    @property
    def programming_language(self):
        return self.__prog_lang

    def __repr__(self):
        return f"{self.__class__.__name__}(prog_lang={self.programming_language}, salary={self.salary})"


class TechnicalManager(Job):
    def __init__(self, salary: int):
        super().__init__(salary)

    def __repr__(self):
        return f"{self.__class__.__name__}(salary={self.salary})"
