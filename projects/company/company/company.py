from typing import List

from company.employee import Employee


class Company:
    __employee: List[Employee]

    def __init__(self, lst: List[Employee] = None) -> None:
        self.__employee = []
        if lst:
            self.__employee.extend(lst)

    def add_employee(self, emp: Employee) -> None:
        self.add_employee(emp)

    def add_list_of_employees(self, lst: List[Employee]) -> None:
        self.__employee.extend(lst)

    def search_by_name(self, fullname: str) -> List[Employee]:
        found_employees = filter(lambda e: e.name == fullname, self.__employee)
        return list(found_employees)

    def __len__(self) -> int:
        return len(self.__employee)

    def __getitem__(self, item) -> Employee:
        return self.__employee[item]

    def __repr__(self):
        return str(self.__employee)

    def __str__(self) -> str:
        output = ""
        for e in self.__employee:
            output = output + str(e) + "\n"
        return output
