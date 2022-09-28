def main():
    print("Введите вакансию для поиска")
    search_text = input("Вакансия: ")

    url_hh = 'https://api.hh.ru/vacancies'
    url_sj = ''

    # hh.ru
    for page in range(1, 71):
        hh_vacancies = ...  # Объект класса HH

        for vac in hh_vacancies:
            vacancies = ...  # Объект класса Vacancies

    # superjob.ru
    for page in range(1, 31):
        sj_vacancies = ...  # Объект класса Superjob

        for vac in sj_vacancies:
            vacancies = ...  # Объект класса Vacancies


if __name__ == '__main__':
    main()
