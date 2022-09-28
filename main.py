from utils import *


def main():
    clean_json_file()

    print("Введите вакансию для поиска")
    search_text = input("Вакансия: ")

    # Парсим hh.ru
    website = 'hh'
    parce_page(search_text, 3, website)

    # Парсим superjob.ru
    website = 'sj'
    parce_page(search_text, 2, website)

    # Топ 10 по зп
    vacancies = get_top10_salary()

    for vacancy in vacancies:
        print(vacancy)


if __name__ == '__main__':
    main()
