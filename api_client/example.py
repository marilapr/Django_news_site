from .client import NewsAPIClient

# Пример использования
if __name__ == '__main__':
    # Подключение к API
    client = NewsAPIClient('http://127.0.0.1:8000')

    # 1. Регистрация
    print("=== Регистрация ===")
    print(client.register('testuser', 'test@mail.ru', 'qwerty123'))

    # 2. Вход
    print("=== Вход ===")
    print(client.login('testuser', 'qwerty123'))

    # 3. Создание новости
    print("=== Создание новости ===")
    print(client.create_news(
        title='Моя первая новость',
        description='Это описание новости. Оно должно содержать минимум 50 символов, чтобы пройти валидацию. Этот текст достаточно длинный.'
    ))

    # 4. Получение всех новостей
    print("=== Все новости ===")
    news = client.get_news()
    print(news)

    # 5. Получение одной новости
    if news and 'results' in news and news['results']:
        news_id = news['results'][0]['id']
        print(f"=== Новость {news_id} ===")
        print(client.get_news(news_id))

    # 6. Обновление новости
    # print("=== Обновление ===")
    # print(client.update_news(news_id, title='Обновлённый заголовок'))

    # 7. Удаление новости ЧТОБЫ СРАЗУ НЕ УДАЛЯЛАСЬ ПРИ СОЗДАНИИ
    # print("=== Удаление ===")
    # print(client.delete_news(news_id))