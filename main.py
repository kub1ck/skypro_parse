from utils import *


def main() -> None:
    clean_json_file()

    print("Введите вакансию для поиска")
    search_text = input("Вакансия: ")

    # Парсим hh.ru
    website = 'hh'
    print("\nПарсим hh.ru...")
    parce_page(search_text, 10, website)

    # Парсим superjob.ru
    website = 'sj'
    print("\nПарсим superjob.ru...")
    parce_page(search_text, 10, website)

    data = get_data()

    while True:
        print("\n'1' - вывести топ 10 вакансий по зарплате",
              "'2' - вывести случайное количество вакансий",
              "'другие' - выход\n",
              sep='\n')

        user_request = input("Введите цифру: ")
        match user_request:
            case '1':
                result = get_top10_salary(data)
            case '2':
                number_vacancies = int(input("Введите количество вакансий: "))
                result = get_random_vacancies(data, number_vacancies)
            case _:
                result = []

        if not result:
            break

        for res in result:
            vacancy = Vacancy(res)
            print(vacancy)


if __name__ == '__main__':
    main()
