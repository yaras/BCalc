chorobowe.py
===

Skrypt wyliczający wysokość zasiłku chorobowego dla podanych pensji

Przykładowe uruchomienie
---

Dla przykładu [1] (składki są równe 0, poniewaz podana pensja jest juz po odliczeniu składek):

```
chorobowe -p 2553.69 -c 10 --param emerytalna_pracownik=0 rentowa_pracownik=0 chorobowa_pracownik=0
```

Dla przykładu z [2]:

```
chorobowe -p 3000 -c 5
```

Źródła
---

* [1] http://www.gofin.pl/skladki-zasilki-emerytury/17,2,110,125380,jak-prawidlowo-obliczyc-wynagrodzenie-chorobowe.html
* [2] http://praca.gazetaprawna.pl/artykuly/833810,jak-obliczyc-zasilek-chorobowy.html
* [3] http://poradnikpracownika.pl/-zwolnienie-lekarskie-a-wysokosc-wynagrodzenia
* [4] http://otwierambiznes.com.pl/jak-obliczyc-wynagrodzenie-chorobowe/
