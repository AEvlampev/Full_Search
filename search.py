import sys
import io
# Этот класс поможет нам сделать картинку из потока байт

import requests
from Samples import geocoder
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

coords, delta = geocoder.get_ll_span(toponym_to_find)

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": coords,
    "spn": delta,
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
Image.open(io.BytesIO(response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы