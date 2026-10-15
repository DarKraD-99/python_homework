import requests


class YogileApi:

    def __init__(self, url):
        self.url = url
        self.login = 'ВАШ_ЛОГИН'
        self.password = 'ВАШ_ПАРОЛЬ'
        self.name = 'SkyPro'

    def get_companies(self):
        creds = {
            'login': self.login,
            'password': self.password,
            'name': self.name
        }
        resp = requests.post(self.url + "/auth/companies", json=creds)

        return resp.json()['content'][0]['id']

    def get_yougile_token(self):
        company_id = self.get_companies()
        creds = {
            'login': self.login,
            'password': self.password,
            'companyId': company_id
        }
        resp = requests.post(self.url + '/auth/keys', json=creds)

        return resp.json()['key']

    def get_id_users(self, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }

        resp = requests.get(self.url + '/users', headers=headers)
        return resp.json()

    def get_id_departments(self, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp = requests.get(self.url + '/departments', headers=headers)

        return resp.json()

    def create_project(self, token, department_id):
        project = {
            'title': 'Проект для дз',
            'departments': {
                department_id: {
                    'manager': 'admin',
                    'member': 'worker'
                }
            }
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        resp = requests.post(
            self.url + '/projects', json=project, headers=headers
        )
        return resp

    def change_project(self, token, project_id, department_id):
        project = {
            'deleted': False,
            'title': 'Изменённая дз',
            'departments': {
                department_id: {
                    'manager': 'admin',
                    'member': 'worker'
                }
            }
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        resp = requests.put(
            self.url + '/projects/' + project_id, json=project, headers=headers
        )
        return resp

    def get_project(self, token, limit, offset, title):
        project = {
            'includeDeleted': False,
            'limit': limit,
            'offset': offset,
            'title': title
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        resp = requests.get(
            self.url + '/projects', params=project, headers=headers
        )
        return resp.json()
