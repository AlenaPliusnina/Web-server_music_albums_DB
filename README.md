# web-server_Albums_DataBase_B6.13

Описание проекта:

1. Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение с количеством альбомов исполнителя artist 
и списком названий этих альбомов.

   Пример:
   
   ![Иллюстрация к проекту](https://github.com/AlenaPliusnina/web-server_Albums_DataBase_B6.13/blob/master/screenshots/get_1.png)
   

2. Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем данные об альбоме. Данные передаются в формате веб-формы.

   Чтобы сформировать POST-запрос к серверу можно воспользоваться утилитой http. Формат POST-запроса:
   
          http -f POST http://localhost:8080/albums year=1990 artist="New Artist" genre="Rock" album="Super"

   Пример:
   
   ![Иллюстрация к проекту](https://github.com/AlenaPliusnina/web-server_Albums_DataBase_B6.13/blob/master/screenshots/get_post.png)
   
   ![Иллюстрация к проекту](https://github.com/AlenaPliusnina/web-server_Albums_DataBase_B6.13/blob/master/screenshots/get_2.png)
   
Если пользователь пытается передать данные об альбоме, который уже есть в базе данных, обработчик запроса отвечает HTTP-ошибкой 409 
и выводит соответствующее сообщение.

   Пример:
   
   ![Иллюстрация к проекту](https://github.com/AlenaPliusnina/web-server_Albums_DataBase_B6.13/blob/master/screenshots/http_error.png)
   
Для локального запуска проекта скачайте репозиторий и запустите сервер через командную строку:
 
        python album_server.py

    
