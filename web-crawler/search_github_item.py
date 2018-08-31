import requests

get_code_api = "https://api.github.com/search/code?q="
get_repo_api = "https://api.github.com/search/repositories?q=language:python"


def get_code(language, size, repo):
    url = '{}language:{}+size:{}+repo:{}'.format(get_code_api, language, size, repo)
    info = requests.get(url).json()
    if 'items' in info:
        for i in info['items']:
            print(i['html_url'])


def get_project(last_week):
    info = requests.get(get_repo_api).json()
    for i in info['items']:
        updated_time = i['updated_at']
        if updated_time > last_week:
            repo = i['html_url'].replace("https://github.com/", "")
            get_code('python', '<200', repo)


if __name__ == '__main__':
    get_project("2017-01-3T00:00:00Z")
