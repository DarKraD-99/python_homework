from yougile_api import YogileApi


base_url = "https://ru.yougile.com/api-v2"

api = YogileApi("https://ru.yougile.com/api-v2")


def test_positive_create_project():
    token = api.get_yougile_token()

    departments = api.get_id_departments(token)
    department_id = departments['content'][0]['id']

    resp = api.create_project(token, department_id)

    assert resp.status_code == 201


def test_negative_create_project():
    token = api.get_yougile_token()

    departments = api.get_id_departments(token)
    department_id = departments['content'][0]['id']

    invalid_token = 'invalid_token'

    resp = api.create_project(invalid_token, department_id)

    assert resp.status_code == 401


def test_positive_change_project():
    token = api.get_yougile_token()

    departments = api.get_id_departments(token)
    department_id = departments['content'][0]['id']

    project_id = api.create_project(token, department_id).json()['id']

    resp = api.change_project(token, project_id, department_id)
    body = api.get_project(token, limit=50, offset=0, title='Изменённая дз')

    assert resp.status_code == 200
    assert len(body['content']) > 0
    assert body['content'][0]['title'] == 'Изменённая дз'


def test_negative_change_project():
    token = api.get_yougile_token()

    departments = api.get_id_departments(token)
    department_id = departments['content'][0]['id']

    project_id = 'несуществующий_id'

    resp = api.change_project(token, project_id, department_id)

    assert resp.status_code == 404


def test_get_positive_project():
    token = api.get_yougile_token()

    body = api.get_project(token, limit=50, offset=0, title=None)

    assert 'content' in body
    assert 'paging' in body
    assert len(body['content']) > 0


def test_get_negative_project():
    token = api.get_yougile_token()

    body = api.get_project(
        token, limit=50, offset=0, title="Несуществующий проект"
    )

    assert len(body['content']) == 0
