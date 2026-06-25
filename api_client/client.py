import requests


class NewsAPIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            self.session.headers.update({'Authorization': f'Token {token}'})

    def register(self, username, email, password):
        """Регистрация нового пользователя"""
        resp = self.session.post(
            f"{self.base_url}/api/users/",
            json={'username': username, 'email': email, 'password': password}
        )
        return resp.json()

    def login(self, username, password):
        """Вход и получение токена"""
        resp = self.session.post(
            f"{self.base_url}/api/token/",
            json={'username': username, 'password': password}
        )
        if resp.status_code == 200:
            token = resp.json().get('token')
            self.session.headers.update({'Authorization': f'Token {token}'})
        return resp.json()

    def create_news(self, title, description, image=None):
        """Создание новости"""
        data = {'title': title, 'description': description}
        files = {}
        if image:
            files = {'image': image}
        resp = self.session.post(
            f"{self.base_url}/api/news/",
            data=data,
            files=files
        )
        return resp.json()

    def get_news(self, news_id=None, params=None):
        """Получение новостей (одной или всех)"""
        if news_id:
            url = f"{self.base_url}/api/news/{news_id}/"
        else:
            url = f"{self.base_url}/api/news/"
        resp = self.session.get(url, params=params)
        return resp.json()

    def update_news(self, news_id, **kwargs):
        """Частичное обновление новости"""
        resp = self.session.patch(
            f"{self.base_url}/api/news/{news_id}/",
            json=kwargs
        )
        return resp.json()

    def delete_news(self, news_id):
        """Удаление новости"""
        resp = self.session.delete(f"{self.base_url}/api/news/{news_id}/")
        return resp.status_code