Первым шагом будет клонирование репозитория.  
Для запуска проекта необходимы последние версии Ripes для Ubuntu(Linux) и для WASM'a.  
WASM: https://github.com/moevm/mse1h2024-ripes/actions/runs/8870046065  
Ubuntu: https://github.com/moevm/mse1h2024-ripes/actions/runs/8912469010 (Release executable)  
Их можно скачать, пройдя по ссылкам выше. Сначала нужно перейти в раздел "Summary", затем в самом разделе пролистать до заголовка "Artifacts", под ним кликнуть по значку загрузки справа от нужного архива.  
Архив с исполняемым файлом для Ubuntu нужно распаковать в папку /lti_server/server/infra/tasks, переименовать его в "Ripes" и разрешить исполнение.  
Архив с файлами для WebAssembler нужно распаковать в папку /lti_server/server/static/, при небходимости заменить уже существующие файлы с таким же названием.  

```bash
xhost local:root
cd lti_server/
docker build . -t lti_server -f Containerfile
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -p 5000:5000 lti_server:latest
```
