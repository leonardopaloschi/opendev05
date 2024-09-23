import requests


def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    try:
        commit_info = info[0]['commit']['author']
    except KeyError:
        commit_info = {'date': '2024-09-23T10:00:00Z', 'name': 'Nenhum commit encontrado'}
    return commit_info['date'], commit_info['name']