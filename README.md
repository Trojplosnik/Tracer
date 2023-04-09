# Tracer

Для того чтобы запустить программу, нужно вписать в терминал:
"python путь_к_файлу_Tracer.py IP-адрес/доменное_имя"

После этого программа выведет на экран таблицу со всеми (первыми 15-ю) маршрутизаторами, которые проходит пакет по пути к указанному IP-адресу.

Формат таблицы: 

    Номер по порядку | IP-адрес | Сообщение о недоступности / (Номер Автономной системы | Страна | Провайдер)


Пример использования:

№1

    Ввод: python Tracer.py iichan.hk
    
    Вывод:
    N |     IP     |     AS     | COUNTRY | ISP
    1 | 192.168.1.1 | private range
    2 | 95.82.248.1 | AS12668 | Russia | MiraLogic Telecommunication Systems
    3 | 92.242.30.113 | AS12668 | Russia | MiraLogic Telecommunication Systems
    4 | 195.208.210.247 | AS8492 | Russia | "OBIT" Ltd.
    5 | 195.208.209.96 | AS8492 | Russia | "OBIT" Ltd.
    6 | 10.40.133.3 | private range
    7 | 193.233.63.14 | AS42745 | Argentina | Safe Value Limited



№2

    Ввод: python Tracer.py 8.8.8.8
    
    Вывод:
    N |     IP     |     AS     | COUNTRY | ISP
    1 | 192.168.1.1 | private range
    2 | 95.82.248.1 | AS12668 | Russia | MiraLogic Telecommunication Systems
    3 | 92.242.30.113 | AS12668 | Russia | MiraLogic Telecommunication Systems
    4 | 2.63.212.102 | AS12389 | Russia | JSC Rostelecom . Korporativniy Centr
    5 | 2.63.212.101 | AS12389 | Russia | JSC Rostelecom . Korporativniy Centr
    6 | 185.140.148.153 | AS12389 | Russia | PJSC Rostelecom
    7 | 72.14.209.89 | AS15169 | United States | Google LLC
    8 | 108.170.250.33 | AS15169 | United States | Google LLC
    9 | 108.170.250.34 | AS15169 | United States | Google LLC
    10 | 142.251.238.82 | AS15169 | United States | Google LLC
    11 | 142.251.238.68 | AS15169 | Canada | Google LLC
    12 | 172.253.51.245 | AS15169 | United States | Google LLC

№3

    Ввод: python Tracer.py ip-address

    
    Вывод:
    Something wrong in subprocess tracert.
    You may have entered a non-existent domain name or IP.

№4
    
    Ввод: python Tracer.py ip-address

    
    Вывод:
    Something wrong in subprocess tracert.
    You may have entered a non-existent domain name or IP.

№5

    Ввод: python Tracer.py 8.8.8.8 google.com

    
    Вывод:
    Wrong input.
