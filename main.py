from functions import real_number
from functions import root
from functions_2 import ComplexNumber

# polecam opisywać to co zrobiliscie oraz rzucać wyjątki typu raise Exception("coś tam") żeby pilnować typów
def main():
    list_of_op = [None] * 10
    for x in range(0, 10):
        func = int(input("Wybierz co chcesz zrobić:\n 1 -> coś obliczyć \n 2 -> wczytać wcześniejsze działania "
                         " \n 3 -> wyczyścić pamięć \n"))  # początkowe menu
        if func == 1:  # if dla obliczeń
            num_type = int(input("Na jakich liczbach chcesz przeprowadzić działanie: \n 1 -> rzeczywistych \n"
                                 " 2 -> zespolonych\n"))  # menu wyboru liczb dla obliczeń
            if num_type == 1:  # input dla rzeczywistych
                print("Podaj dane w formacie: \n liczba x \n operator \n liczba y"
                      "\nJeśli chcesz potęgować użyj operatora '^', a w przypadku pierwiastka 'pierw'")
                list_of_op[x] = (real_number(int(input(" x: ")), input(" operator: "), int(input(" y: "))))
            elif num_type == 2:  # tutaj wpisać input dla urojonych!
                num_type_2 = int(input("Jakie operacje chcesz przeprowadzić na licznach zespolonych: \n "
                                       "1 -> podstawowe działania matematyczne \n "
                                       "2 -> moduł liczby zespolonej \n"
                                       "3 -> argument główny liczby zespolonej \n"))
                if num_type_2 == 1:
                    print("Podaj dane w formacie: \n liczba x \n operator \n liczba y")
                    list_of_op[x] = (ComplexNumber(input(" x: "), input(" operator: "), input(" y: ")))
                elif num_type == 2:
                    print("Podaj liczbe zespoloną w posatci algebraiccznej (np. 4+5j): \n")
                    list_of_op[x] = (ComplexNumber(input(" x: "), op="abs"))
                elif num_type == 3:
                    pass
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
                print(root(list_of_op[x].x,list_of_op[x].y))
            elif list_of_op[x].op == 'abs':
                print(abs(list_of_op[x]))

        if func == 2:  # if dla wczytywania zadań
            pass
            # Piotrek ~tablica list_of_op przechowuje 10 operacji, a gdy chcemy zapisać 11 zapisuje na miejscu pierwszej
            # operacji, musisz wykminić coś co w przypadku gdy ktoś zapisał 15 operacji i chce wczytać 10 ostatnich no i
            # ogolnie to wczytywanie

        if func == 3:  # if dla czyszczenia pamięci
            pass



        if x == 9:
            x = 0

if __name__ == '__main__':
    main()