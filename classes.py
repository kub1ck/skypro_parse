from abc import ABC, abstractmethod
import requests
import re


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
        if salary is None:
            return [0, '']

        if salary['from'] is None:
            return [0, salary['currency']]

        return [salary['from'], salary['currency']]

    @staticmethod
    def formate_snippet(snippet):
        if snippet["requirement"] is None:
            result = snippet["responsibility"]
        elif snippet["responsibility"] is None:
            result = snippet["requirement"]
        else:
            result = snippet["requirement"] + ' ' + snippet["responsibility"]

        return re.sub(r"<highlighttext>|</highlighttext>", '', result)
