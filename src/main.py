# Main File
from company.company import Company

def main() -> None:
    nit = input('Digite el nit: ')
    name = input('Digite el nombre: ')
    num_employee = int(input('Digite la cantidad de empleados: '))
    company1 = Company(nit, name, num_employee)


if __name__ == '__main__':
    main()