from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "16", "79212345656"),
    Smartphone("Samsung", "самсунговый", "79162347898"),
    Smartphone("Xiaomi", "RedMi XXX", "79267893451"),
    Smartphone("Nokia", "3310", "79117569809"),
    Smartphone("Sony", "Xperia Z1", "75126774523")
    ]

for smartphone in catalog:
    smartphone.info()
