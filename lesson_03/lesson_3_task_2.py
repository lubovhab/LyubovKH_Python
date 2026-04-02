from smartphone import Smartphone

catalog = [Smartphone('Apple', 16, '+79111111111'),
           Smartphone('Samsung', 's25', '+79222222222'),
           Smartphone('Huawei', 'Pura', '+7933333333333'),
           Smartphone('Honor', 100, '+79444444444'),
           Smartphone('Xiaomi', 14, '+79555555555')]


for smart_ph in catalog:
    print(f'{smart_ph.brand} - {smart_ph.model}. {smart_ph.phone_number}')
