from address import Address
from mailing import Mailing

to_address = Address(199406, "Санкт-Петербург", "ул. Гаванская", "д. 35", "кв. 10")

from_address = Address(175300, "Валдаай", " ул. Белова,", "д. 8", "кв. -")
                       
my_mailing = Mailing(to_address, from_address, 1235, "122333444455555")

print(f"Отправление {my_mailing.getTrack()} из {from_address.getAddress()} в {to_address.getAddress()}. Стоимость {my_mailing.getCoast()} руб.")



