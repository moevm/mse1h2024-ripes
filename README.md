## Итерация 2 
#### Решенные задачи:
 - Реализован сервер для обработки/отправки запросов на Flask
 - Настроен moodle для подключения ripes 
 - Создана инструкция для настройки подключения moodle к ripes
 - Создан UI для отображения условия заданий в ripes*  
 - Реализован выбор заданий в ripes
 - Реализованна проверка заданий на синтаксические ошибки
   
#### Задачи в процессе решения:
 - Отправка response в moodle 
 - Обработка request от moodle
 - Первый прототит

#### Инструкция по сборке
Первым шагом будет клонирование репозитория.
Для запуска проекта необходимы последние версии Ripes для Ubuntu(Linux) и для WASM'a.
WASM: https://github.com/moevm/mse1h2024-ripes/actions/runs/8870046065
Ubuntu: https://github.com/moevm/mse1h2024-ripes/actions/runs/8912469010 (Release executable)
Их можно скачать, пройдя по ссылкам выше. Сначала нужно перейти в раздел "Summary", затем в самом разделе пролистать до заголовка "Artifacts", под ним кликнуть по значку загрузки справа от нужного архива.
Архив с исполняемым файлом для Ubuntu нужно распаковать в папку /lti_server/server/infra/tasks, переименовать его в "Ripes" и разрешить исполнение.
Архив с файлами для WebAssembler нужно распаковать в папку /lti_server/server/static/, при небходимости заменить уже существующие файлы с таким же названием.
```bash
cd lti_server/
docker build -t lti_server -f Containerfile
docker run -p 5000:5000 lti_server:latest
```

## Итерация 3
[Презентация](https://github.com/moevm/mse1h2024-ripes/blob/master/Ripes3.pdf)


## Implementation of moodle with ripes interaction, configuration of connection to service from moodle side.
Configuring the External Tool it is done through received editing rights then add an external tool for subsequent configuration.
<p align="center">
	<img src="https://github.com/moevm/mse1h2024-ripes/blob/master/resources/images/externaltool.jpg" />
</p>
Add name, URL and select LTI version.
<p align="center">
    <img src="https://github.com/moevm/mse1h2024-ripes/blob/master/resources/images/nameurl.jpg" />
</p>
That’s it.
<p align="center">
    <img src="https://github.com/moevm/mse1h2024-ripes/blob/master/resources/images/reslti.jpg" />
</p>
