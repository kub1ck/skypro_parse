import json
from classes import *


def clean_json_file() -> None:
    """
    Очищаем файл при повторном запуске программы
    """

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False, indent=2)


def update_json_file(res: list) -> None:
    """
    Добавляем данные в json файл
    """

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
        data.extend(res)
        with open('result.json', 'w', encoding='utf-8') as file2:
            json.dump(data, file2, ensure_ascii=False, indent=2)


def parce_page(search_text: str, total_page: int, web: str) -> None:
    """
    Парсит каждую страницу на сайтах и проводит запись в файл
    """

    for page in range(1, total_page+1):
        vacancies = HH(search_text, page) if web == 'hh' else Superjob(search_text, page)
        result = vacancies.get_formatted_data()
        if not result:
            break

        print(f"Парсинг {page} страницы..")
        update_json_file(result)


def get_top10_salary() -> list:
    """
    Сортируем вакансии по зарплате и возвращаем топ 10 вакансий
    """

    with open('result.json', encoding='utf-8') as file:
        return sorted(json.load(file), key=lambda v: v['salary'], reverse=True)[:10]
