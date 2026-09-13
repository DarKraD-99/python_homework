from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "17 Pro Max", "+79031234567"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79133216587"),
    Smartphone("Xiaomi", "16 Ultra", "+79988764591"),
    Smartphone("HUAWEI", "Pura 80 Ultra", "+79619761263"),
    Smartphone("Honor", "Magic8 Pro", "+79546544564")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.numb}")
