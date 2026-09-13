from address import Address
from mailing import Mailing

from_address = Address(620000, "Екатеринбург", "ул. Мира", "д.84", "кв. 71")
to_address = Address(630000, "Новосибирск", "ул. Ленина", "д.17", "кв. 35")
costing = 1300
track = "45005145009749"

my_mailing = Mailing(to_address, from_address, costing, track)

print(my_mailing)
