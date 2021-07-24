import requests
import re

def extract_infos(function):
    def __inner__(text, author, title):
        resp = function(text)
        line = list()
        for i in resp["docs"]:
            dict_ = dict()
            dict_['title'] = i.get('title', '')
            dict_['year'] = re.sub(r'[\[\]\']', '', str(i.get('publish_year','')))
            dict_['author'] = re.sub(r'[\[\]\']', '', str(i.get('author_name', '')))
            line.append(dict_)
        return line
    return __inner__


@extract_infos
def mock_book(text, author=False, title=False):
    return {
        'docs':[
            {
                'nome' : 'JK',
                'title' : 'HP e o Pisonero de Aiskaban',
                'publish_year': 1900,
                'author_name' : 'None',
                'descricao' : 'NA'
            }]
        }


@extract_infos
def get_books(text, author=False, title=False):
  if author != False and title != False:
    print('Please choose only one method of search')
    exit

  text = text.replace(" ", "+")

  if author != False:
    return requests.get(f"http://openlibrary.org/search.json?author={text}").json()
  elif title != False:
    return requests.get(f"http://openlibrary.org/search.json?title={text}").json()
  else:
    return requests.get(f"http://openlibrary.org/search.json?q={text}").json()    



print(get_books('Lord Of The Rings', False, True))