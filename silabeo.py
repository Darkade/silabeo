#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


#1. Cuando una consonante está entre vocales se une a la vocal que la sigue.* Ejemplo: a-ni-llo, mo-ne-da
#2. Cuando hay dos consonantes entre vocales, la primera se une a la vocal precedente y la segunda, a la siguiente.* Ejemplos: al-to, ar-tis-ta
#3. De tres consonantes entre vocales, las dos primeras se unen a la vocal que las antecede y l aotra, a la que sigue.
#* Ejemplos: ins-tar, abs-ten-ción, pers-pi-caz
#* Excepciones: cuando hay grupos inseparables de consonantes: in-glés, am-pliar
#6. Cuando dos vocales forman un diptongo, éstas no se separan al silabear.
#* Ejemplos: ai (baile); au (pausa); ei (peine, ley); eu (feudo); ia (viaje); ie (pieza); io (odio); iu (ciudad); oi (oigo, hoy); ou (bou), ua(agua); ue (vuelta); ui (juicio); uo (arduo).



#4. Cuando hay cuatro consonantes entre vocales, entonces, las dos primeras se unen a la vocal anterior y las otras dos a la que sigue.
#* Ejemplos: ins-truir, trans-gre-sión

#5. Las consonantes forman grupos inseparables cuando se encuentran las letras “l” o “r” junto con alguna de las letras “b”, “c”, “d”, “f”, “g”, “p” o “t”.
#* Ejemplos: a-brir, a-gra-da-ble, de-plo-ra-ble


#r = re.compile('([^aiueo]|(?:\A[aiueo])[aiueo][aiueo]?(?:[^aiueo]{1,2}(?=[^aiueo]))?(?:[^aiueo](?=\Z))?)')
r = re.compile("""

(?:[bcdfgpotl][lr]|[^aiueo])?[aiueo]+
(?:
(?=[bcdfgpotl][lr])
|
[^aiueo][^aiueo](?=[^aiueo][^aiueo]|[^aiueo])
|
[^aiueo](?=[^aiueo]|\Z)
)?
"""








,re.X)


print r.findall('anillo'),'a ni llo'
print r.findall('moneda'),'mo ne da'
print r.findall('alto'),'al to'
print r.findall('artista'),'ar tis ta'
print r.findall('instar'),'ins tar'
print r.findall('abstencion'),'abs ten cion'
print r.findall('perspicaz'),'pers pi caz'
print r.findall('instruir'),'ins truir'
print r.findall('transgresion'),'trans gre sion'
print r.findall('abrir'),'a brir'
print r.findall('agradable'),'a gra da ble'
print r.findall('deplorable'),' de plo ra ble'
print r.findall('baile')
print r.findall('pausa')
print r.findall('peine')
print r.findall('feudo')
print r.findall('viaje')
print r.findall('pieza')
print r.findall('odio')
print r.findall('ciudad')
print r.findall('oigo')
print r.findall('hoy')
print r.findall('agua')
print r.findall('vuelta')
print r.findall('juicio')
print r.findall('arduo')
