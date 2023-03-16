# Main File
from user.person import Person

def main() -> None:
    name = input('Digite su nombre: ')
    lastname = input('Digite su apellido: ')
    age = int(input('Digite su edad: '))
    person1 = Person(name, lastname, age)


if __name__ == '__main__':
    main()