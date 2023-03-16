# Main File

from company.company import Company
from user.person import Person

def main() -> None:
    name = input('Digite su nombre: ')
    lastname = input('Digite su apellido: ')
    age = int(input('Digite su edad: '))
    person1 = Person(name, lastname, age)
    nit = input('Digite el nit: ')
    name = input('Digite el nombre: ')
    num_employee = int(input('Digite la cantidad de empleados: '))
    company1 = Company(nit, name, num_employee)


if __name__ == '__main__':
    main()