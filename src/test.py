import requests
import unittest
import json


url_01 = requests.get(' http://localhost:5000/books')
url_02 = requests.get(' http://localhost:5000/books/teste02')
url_03 = requests.get('http://localhost:5000/author/5ec44e21fc4168f0e37b1d74')

print(url_03.json()[0]["name"])

# print(r.json())
class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(url_01.status_code, 200)

    def test_02(self):
        self.assertEqual(url_01.json()[0]["name"], "teste01")

    def test_03(self):
        self.assertEqual(url_02.json()[0]["publication_year"], 2019)

    def test_04(self):
        self.assertEqual(url_03.json()[0]["name"], "Ali N. Meyer")


if __name__ == '__main__':
    unittest.main()
