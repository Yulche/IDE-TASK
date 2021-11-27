# Задание
1. На основании предыдущего проекта сделайте свой репозиторий на GitHub. Поместите туда ваш новый файл filter.py, также в репозиторий поместите первоначальный файл filter.py (old_filter.py).
2. Создайте новый проект. Подключите ваш репозиторий к IDE PyCharm. Загрузите оба файла с помощью Git в PyCharm к себе в проект на компьютер.
3. Добавьте в папку с вашим проектом тестовое изображение, из которого будете получать готовое изображение с фильтром.
4. Добавьте файл в репозиторий и отправьте его на сервер.
Предполагаем, что ваш новый filter.py работает как утилита, где нужно указать во время выполнения имя файла для конвертирования, а также размер блока, и количество градаций серого (также в нем все разделено на необходимые функции и используются все преобразования с матрицами с помощью библиотеки numpy).
5. Запустите с помощью встроенного профилизатора в PyCharm ваш новый filter.py, сделайте скриншот со временем выполнения.
6. Также запустите в профилизаторе old_filter.py. Посмотрите разницу во времени выполнения кода. Полученные скриншоты со временем выполнения с объяснением результатов поместите в файл README.MD
7. Поскольку в вашем файле большая часть времени выполнения затрачивается на ввод данных пользователем, поэтому создайте копию вашего файла filter_with_filename.py, добавьте его также в репозиторий, в котором сразу в код введите имя изображения для конвертирования, а также аналогичные параметры для конвертирования, которые указаны были в первоначальном old_filter.py, а именно размер блока 10 и 50 градаций серого. Также закомитьте полученные правки и отправьте их на сервер.
8. Запустите в профилизаторе файл filter_with_filename.py, сделайте скриншот со временем выполнения этого файла. Полученный скриншот, а также объяснение полученных результатов добавьте в файл README.MD. Также в файл README.MD с помощью wiki-разметки добавьте все изображения до преобразования и после.
9. К выделенным функциям, допишите документацию и doc-тесты в формате: docstring.
10. Проверьте запуск doc-тестов в PyCharm. Сделайте их скриншоты.
11. Закомитьте все изменения на github. Скриншоты doc-тесты с соответствующими комментариями прикрепите в файл README.MD.
12. Проинспектируйте ваш проект в PyCharm. Исправьте все замечания по PEP8. Закомитьте в репозиторий с соответствующей подписью в коммите.
13. Через отладчик вывести на экран в свойствах изображения ширину и высоту, а также тип изображения. Также в отладчике выведите значения ширины блока и количество градаций серого.
14. Сделайте скриншоты результата работы отладчика и вставьте их в файл README.MD. 

#Выполнение#

# 5.
![изображение](https://user-images.githubusercontent.com/73441333/143667056-19297a4a-e44b-41d9-b52e-2a638225c637.png)

# 6.
![изображение](https://user-images.githubusercontent.com/73441333/143623906-f44b2870-3144-4d35-ae73-5662c0c8ba2b.png)
Вывод:
Для нового filter.py
Большое кол-во времени тратится на ввод; Меньшее кол-во времени (но всё же много) тратится на методы convert_image_to_mosaic и get_average_brightness, т.к. в них используются матричные операции и множество циклов. Далее - встроенный метод numpy numpy.core._multiarray_umath.implement_array_function (это диспетчер, вызывающий numpy для каждого метода, вызываемого объектом numpy). Далее идут методы, отвечающие за получение и загрузку изображения. exec_module отвечает за загрузку и реализацию модулей, которые были импортированы в данное пространство имен; init.py - инициализация проекта, sum - метод numpy, неоднократно использующийся в методе pixel_brightness.

Для старого filter.py
В общем, затратные методы такие же, но времени на них потрачено гораздо больше

# 8.
![изображение](https://user-images.githubusercontent.com/73441333/143667643-822a7a41-0112-4062-a472-08fe3fdd8ca4.png)
Вывод: время работы программы сильно сократилось, посльку больше нет затрат на ручной ввод.

# 10.
для get_average_brightness
![изображение](https://user-images.githubusercontent.com/73441333/143668778-4f22ef92-529c-4c7d-96f5-70cb19625000.png)

# 11.
Доктесты успешно пройдены. Для функции convert_image_to_mosaic доктест не создан, поскольку результатом является изображение

# 13 - 14.
![изображение](https://user-images.githubusercontent.com/73441333/143669665-d82b5736-37be-4e5a-9b99-50f6e85df2b1.png)
