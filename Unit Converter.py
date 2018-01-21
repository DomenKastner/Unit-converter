# -*- coding: utf-8 -*-

#Pretvornik iz gramov v unče ter obratno

#Plan:

#Program pozdravi uporabnika in predstavi kaj počne.
#Program prosi uporabnika, naj vnese enoto za pretvorbo.
#Uporabnik vnese težo.
#Program pretvori grame v unče in izpiše rezultat v terminalu.
#Program vpraša uporabnika, če želi narediti novo pretvorbo.
#Če uporabnik odgovori z "da", potem se proces ponovi.
#Če ne, se program poslovi in konča.
#Program naj neprenehoma teče, vsaj dokler ne bo uporabnik želi delati pretvorbe.

print("Pozdravljeni v pretvorniku teže zlata.\nS tem programom lahko pretvorimo grame v unče ali obratno")
# 1 g = 0.035274 oz
g = 1
oz = 1

while True:
        merska_enota = str(raw_input("Želite pretvoriti v g ali oz? :"))
        teza = int(raw_input("Vnesi težo:"))


        if merska_enota == "g":
                print ("V gramih je to: "), teza / 0.035274

        if merska_enota == "oz":
                print ("V unčah je to: "), teza * 0.035274

        ponovi = str(raw_input("Želite ponovno zagnati pretvornik? (da/ne):"))
        if ponovi != "da":
            break
