from bs4 import BeautifulSoup
import requests

base_url = "http://www.ufcstats.com/statistics/fighters?char="

# a .. z
chars = [chr(c) for c in range(97, 123)]

# base_url + a..z
urls = ["http://www.ufcstats.com/statistics/fighters?char=" + c for c in chars]

class Fighter:
    def __init__(self, name, record, nickname, stance, dob):
        self.name = self._format_name(name)
        self.record = self._format_record(record)
        self.nickname = self._format_nickname(nickname)
        self.stance = self._format_stance(stance)
        self.dob = self._format_dob(dob)

    def print(self):
        print(f'{self.name}: {self.record}')

    @staticmethod
    def _format_name(name):
        return name
    
    @staticmethod
    def _format_record(record):
        return record
    
    @staticmethod
    def _format_nickname(nickname):
        return nickname
    
    @staticmethod
    def _format_stance(stance):
        return stance
    
    @staticmethod
    def _format_dob(dob):
        return dob
    
if __name__ == '__main__':
    fighters = []

    for url in urls:
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, features="html.parser")
        for link in soup.find_all('a'):
            try:
                potential_fighter_link = link.get("href")
                if "http://www.ufcstats.com/fighter-details/" in potential_fighter_link:
                    fighters.append(potential_fighter_link)
            except:
                pass
    
    fighters = list(set(fighters))
    
    webpage = requests.get(fighters[0])
    soup = BeautifulSoup(webpage.content, features="html.parser")
    fighter_name = soup.find(attrs={'class': 'b-content__title-highlight'}).get_text().strip()
    fighter_record = soup.find(attrs={'class': 'b-content__title-record'}).get_text().strip()
    fighter_nickname = soup.find(attrs={'class': 'b-content__Nickname'}).get_text().strip()
    fighter_stance = soup.find(attrs={'class': 'b-list__box-list-item b-list__box-list-item_type_block'}).get_text().strip()
    fighter_dob = soup.find(attrs={'class': 'b-list__box-list-item b-list__box-list-item_type_block'}).get_text().strip()
    
    fighter = Fighter(fighter_name, fighter_record, fighter_nickname, fighter_stance, fighter_dob)
    fighter.print()