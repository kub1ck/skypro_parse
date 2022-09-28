from abc import ABC, abstractmethod
import requests
import re
from bs4 import BeautifulSoup


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_formatted_data(self):
        pass


class HH(Engine):
    def __init__(self, url, *params):
        self.url = url
        self.params = {
            'text': params[0],
            'per_page': 20,
            'page': params[1]
        }

    def get_request(self):
        return requests.get(url=self.url, params=self.params).json()

    def get_formatted_data(self):
        universal_vacancies = []
        universal_vacancy = {}
        unformatted_data = self.get_request()

        for vacancy in unformatted_data['items']:
            universal_vacancy['name'] = vacancy['name']
            universal_vacancy['url'] = vacancy['alternate_url']
            universal_vacancy['salary'] = self.formate_salary(vacancy['salary'])
            universal_vacancy['snippet'] = self.formate_snippet(vacancy['snippet'])
            universal_vacancies.append(universal_vacancy.copy())

        return universal_vacancies

    @staticmethod
    def formate_salary(salary):
        if salary is None or salary['from'] is None:
            return 0

        return salary['from']

    @staticmethod
    def formate_snippet(snippet):
        if snippet["requirement"] is None:
            result = snippet["responsibility"]
        elif snippet["responsibility"] is None:
            result = snippet["requirement"]
        else:
            result = snippet["requirement"] + ' ' + snippet["responsibility"]

        return re.sub(r"<highlighttext>|</highlighttext>", '', result)


class Superjob(Engine):
    def __init__(self, url, *params):
        self.url = url
        self.params = {
            'text': params[0],
            'page': params[1]
        }

    def get_request(self):
        url = f'https://russia.superjob.ru/vacancy/search/?keywords={self.params["text"]}&page={self.params["page"]}'
        return requests.get(url)

    def get_formatted_data(self):
        result_dict = {}
        result_list = []

        response = self.get_request()

        soup = BeautifulSoup(response.text, 'lxml')

        names_and_urls = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
        salaries = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
        snippets = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')

        for i in range(len(names_and_urls)):
            result_dict = {
                'name': names_and_urls[i].text,
                'url': 'russia.superjob.ru/' + names_and_urls[i].a['href'],
                'salary': self.formate_salary(salaries[i].text),
                'snippets': snippets[i].text
            }

            result_list.append(result_dict.copy())

        return result_list

    @staticmethod
    def formate_salary(salary):
        salary = re.sub(r"от | | до|до |руб.", "", salary)

        if salary == "По договорённости":
            salary = '0'
        elif '—' in salary:
            salary = re.sub(r"—\d+", "", salary)

        return int(salary)
