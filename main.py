from functions import real_number
from functions import root
from functions_2 import ComplexNumber
from typing import List, Optional, Union


# polecam opisywać to co zrobiliscie oraz rzucać wyjątki typu raise Exception("coś tam") żeby pilnować typów
def main():
    list_of_op: List[Optional[Union[real_number, ComplexNumber]]] = [None] * 10
    list_of_op_size = 0
    x = 0
    while True:
        func = int(input("Wybierz co chcesz zrobić:\n 1 -> coś obliczyć \n 2 -> wczytać wcześniejsze działania "
                         " \n 3 -> wyczyścić pamięć \n"))  # początkowe menu
        if func == 1:  # if dla obliczeń
            num_type = int(input("Na jakich liczbach chcesz przeprowadzić działanie: \n 1 -> rzeczywistych \n"
                                 " 2 -> zespolonych\n"))  # menu wyboru liczb dla obliczeń
            if num_type == 1:  # input dla rzeczywistych
                print("Podaj dane w formacie: \n liczba x \n operator \n liczba y"
                      "\nJeśli chcesz potęgować użyj operatora '^', a w przypadku pierwiastka 'pierw'")
                list_of_op[x] = (real_number(int(input(" x: ")), input(" operator: "), int(input(" y: "))))
            elif num_type == 2:  #input dla liczb zespolonych
                user_operation = int(input("Jakie operacje chcesz przeprowadzić na liczbach zespolonych: \n "
                                           "1 -> podstawowe działania matematyczne \n "
                                           "2 -> moduł liczby zespolonej \n "
                                           "3 -> argument główny liczby zespolonej w radianach \n"))
                if user_operation == 1:
                    print("Podaj dane w formacie: \n liczba x \n operator \n liczba y")
                    list_of_op[x] = (ComplexNumber(input("\tx: "), input("\toperator: "), input("\ty: ")))
                elif user_operation == 2:
                    print("Podaj liczbe zespoloną w posatci algebraiccznej (np. 4+5j): ")
                    list_of_op[x] = (ComplexNumber(input("\tx: "), op="abs"))
                elif user_operation == 3:
                    print("Podaj liczbe zespoloną w posatci algebraiccznej (np. 4+5j): ")
                    list_of_op[x] = (ComplexNumber(input("\tx: "), op="atan"))

            else:
                raise Exception("Błędne dane")
            if list_of_op[x].op == '+':
                print(list_of_op[x].x + list_of_op[x].y)
            elif list_of_op[x].op == '-':
                print(list_of_op[x].x - list_of_op[x].y)
            elif list_of_op[x].op == '*':
                print(list_of_op[x].x * list_of_op[x].y)
            elif list_of_op[x].op == '/':
                print(list_of_op[x].x / list_of_op[x].y)
            elif list_of_op[x].op == '^':
                print(list_of_op[x].x ** list_of_op[x].y)
            elif list_of_op[x].op == 'pierw':
                print(root(list_of_op[x].x, list_of_op[x].y))
            elif list_of_op[x].op == 'abs':
                print(abs(list_of_op[x]))
            elif list_of_op[x].op == 'atan':
                print(list_of_op[x].atan())

            list_of_op_size += 1
            if list_of_op_size > 10:
                list_of_op_size = 10
            x = (x + 1) % 10

        if func == 2:  # if dla wczytywania zadań
            tmp = int(input("ile do tyłu,maksymalnie({}):".format(list_of_op_size)))
            if tmp > list_of_op_size:
                raise Exception("za daleko do tyłu")
            else:
                for i in range(tmp):
                    x2 = (x - i - 1) % 10
                    if list_of_op[x2].op == '+':
                        print("{} = {}".format(list_of_op[x2], list_of_op[x2].x + list_of_op[x2].y))
                    elif list_of_op[x2].op == '-':
                        print("{} = {}".format(list_of_op[x2], list_of_op[x2].x - list_of_op[x2].y))
                    elif list_of_op[x2].op == '*':
                        print("{} = {}".format(list_of_op[x2], list_of_op[x2].x * list_of_op[x2].y))
                    elif list_of_op[x2].op == '/':
                        print("{} = {}".format(list_of_op[x2], list_of_op[x2].x / list_of_op[x2].y))
                    elif list_of_op[x2].op == '^':
                        print("{} = {}".format(list_of_op[x2], list_of_op[x2].x ** list_of_op[x2].y))
                    elif list_of_op[x2].op == 'pierw':
                        print("{} = {}".format(list_of_op[x2], root(list_of_op[x2].x, list_of_op[x2].y)))
                    elif list_of_op[x2].op == 'abs':
                        print("abs {} = {}".format(list_of_op[x2].x,abs(list_of_op[x2]) ))

                    elif list_of_op[x2].op == 'atan':
                        print("atan {} = {}".format(list_of_op[x2].x, list_of_op[x2].atan()))

        if func == 3:  # if dla czyszczenia pamięci
            list_of_op_size = 0




if __name__ == '__main__':
    main()
