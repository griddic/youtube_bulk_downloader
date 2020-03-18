# Использование
Выкачать этот репозиторий:
`git clone https://github.com/griddic/youtube_bulk_downloader.git`

Запустить один раз, чтобы установить зависимости:

`make init`

для каждого списка видео:
1. Скопировать ссылки в файл `video_list.txt` .
1. Выполнить `make clean download` .
1. Перенести файлы из папки `downloads` в нужное расположение.

# команды

* `make init` - установка зависимостей
* `make clean` - очистка папки с загрузками
* `make download` - загрузить видео из файла `video_list.txt`