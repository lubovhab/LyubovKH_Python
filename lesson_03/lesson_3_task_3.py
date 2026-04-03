from address import Address
from mailing import Mailing


to_address1 = Address(456550, 'Korkino', 'Lenina', 1, 5)
from_address1 = Address(454004, 'Chelyabinsk', 'Pushkina', 8, 4)
cont1 = 500
track1 = '987654321'

post_letter = Mailing(to_address1, from_address1, cont1, track1)

print(f'Отправление {track1} из {to_address1} в {from_address1}.\
       Стоимость {cont1} рублей.')
