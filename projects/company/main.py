from company.company import Company
from company.employee import Employee
from company.job import Developer, TechnicalManager

if __name__ == '__main__':
    d1 = Developer("python", 100)
    e1 = Employee("Alireza Aghamohammadi", d1)
    t1 = TechnicalManager(200)
    e2 = Employee("Maliheh Izadi", t1)
    comp = Company([e1, e2])
    print(len(comp))
    print(comp)
    print(comp[0:])
    print(comp.search_by_name("Alireza Aghamohammadi"))
