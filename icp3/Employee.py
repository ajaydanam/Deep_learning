class Employee:
    no_of_employees = 0

    def __init__(self, name, family_name, salary, department):
        self.name = name
        self.family_name = family_name
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(employees):
        total_salary = sum(employee.salary for employee in employees)
        return total_salary / len(employees)


class FulltimeEmployee(Employee):
    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def fulltime_benefits(self):
        print("A Few benefits as a full-time Employee.")


def main():
    employees = []

    f1 = FulltimeEmployee("Ajay", "danam", 84000, "Architecture")
    f1.fulltime_benefits()
    employees.append(f1)

    f2 = FulltimeEmployee("sai", "nalla", 79000, "Archeology")
    f2.fulltime_benefits()
    employees.append(f2)

    e1 = Employee("lenin", "varma", 92000, "Astronaut")
    employees.append(e1)

    e2 = Employee("Sindhu", "Kasi", 112000, "Engineer")
    employees.append(e2)

    print("The Average Salary:", FulltimeEmployee.average_salary(employees))


if __name__ == "__main__":
    main()