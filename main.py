from functions import real_number

def main():
    list_of_op = [None]*10
    number_type = [real_number, 'complex_number'] #tablica potrzebna przy określaniu klasy
    for x in range(0,10):
        func = int(input("Wybierz co chcesz zrobić:\n 1 -> coś obliczyć \n 2 -> wczytać wcześniejsze działania "
                     " \n 3 -> wyczyścić pamięć \n")) #początkowe menu
        if func == 1: # if dla obliczeń
            num_type = int(input("Na jakich liczbach chcesz przeprowadzić działanie: \n 1 -> rzeczywistych \n"
                             " 2 -> urojonych\n")) #menu wyboru liczb dla obliczeń
            if num_type == 1: # input dla rzeczywistych
                print("Podaj dane w formacie: \n liczba x \n operator \n liczba y")
                list_of_op[x] = (real_number(int(input(" x: ")),input(" operator: "),int(input(" y: "))))
            elif num_type == 2: #tutaj wpisać input dla urojonych
                pass
            else:
                raise Exception("Błędne dane")

if __name__ == '__main__':
    main()