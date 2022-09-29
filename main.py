from utils import *


def main():
    clean_json_file()

    print("Введите вакансию для поиска")
    search_text = input("Вакансия: ")

    # Парсим hh.ru
    website = 'hh'
    print("Парсим хх...")
    parce_page(search_text, 10, website)

    # Парсим superjob.ru
    website = 'sj'
    print("Парсим superjob...")
    parce_page(search_text, 10, website)

    # Топ 10 по зп
    vacancies = get_top10_salary()

    print("\nТоп 10 вакансий по зарплате:")
    for vacancy in vacancies:
        vac = Vacancy(vacancy)
        print(vac)


if __name__ == '__main__':
    main()
