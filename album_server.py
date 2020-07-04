# Перед запуском кода необходимо установить в проекте модуль bottle
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

# Импортируем необходимые функции из модуля album
from album import find
from album import connect_db
from album import Album


# Обработка GET-запросов
@route("/albums/<artist>")
def albums(artist):
    albums_list = find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        albums_count = len(albums_list)
        result = "Колличество альбомов у исполнителя - {}. <br> Список альбомов {}: <br> - ".format(albums_count, artist)
        result += ", <br> - ".join(album_names) + "."
    return result


# Обработка POST-запросов
# Чтобы сформировать POST-запрос к серверу можно воспользоваться утилитой http.
# Формат POST-запроса:
# http -f POST http://localhost:8080/albums year=1990 artist="New Artist" genre="Rock" album="Super"
@route("/albums/", method="POST")
@route("/albums", method="POST")
def user_album():
    user_album_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }

    session = connect_db()

    # Проверяем есть ли введенный пользователем альбом в базе
    if session.query(Album).filter(Album.album == user_album_data["album"]) is True:
        message = "Данные об альбоме {} уже есть в базе".format(user_album_data["album"])
        return HTTPError(409, message)

    # Проверка корректности ввода имени артиста, жанра и названия альбома
    try:
        str(user_album_data["artist"])
    except HTTPError:
        message = 'Ошибка ввода данных. Поля с именем артиста (artist) должно быть строкой (тип - str).'
        return HTTPError(400, message)

    try:
        str(user_album_data["genre"])
    except ValueError:
        message = "Ошибка ввода данных. Поле с наименованием жанра (genre) должно быть строкой (тип - str)."
        return HTTPError(400, message)

    try:
        str(user_album_data["album"])
    except ValueError:
        message = "Ошибка ввода данных. Поле с названием альбома (аlbum) должно быть строкой (тип - str)."
        return HTTPError(400, message)

    # Проверка корректности ввода года
    try:
        int(user_album_data["year"])
        if len(str(user_album_data["year"])) != 4:
            message = "Ошибка ввода данных. Год должен быть 4-х значным числом типа int."
            return HTTPError(400, message)
    except ValueError:
        message = "Ошибка ввода данных. Год должен быть 4-х значным числом типа int."
        return HTTPError(400, message)

    else:
        # Сохраняет введенные пользователем данные об альбоме в БД
        album = Album(
            year=user_album_data["year"],
            artist=user_album_data["artist"],
            genre=user_album_data["genre"],
            album=user_album_data["album"]
        )

        session.add(album)
        session.commit()

        return "Данные успешно сохранены!"


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
