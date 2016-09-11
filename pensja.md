pensja.py
===

Skrypt wyliczający składowe pensji na podstawie przekazanej kwoty wynagrodzenia zasadniczego (=kwoty brutto, =kwoty na umowie) dla zatrudnienia na umowy o pracę.

Uruchomienie
---

Przykładowe uruchomienie wyliczające składowe pensji dla wynagrodzenia zasadniczego wynoszącego 3 000 zł i standardowych wartości parametrów:

```
pensja -b 3000
```

Uruchomienie wyliczające składowe pensji dla wynagrodzenia zasadniczego 3 000 zł z nadpisaniem kosztów miejcowych oraz składki wypadkowej:

```
pensja -b 3000 --param koszty_miejscowe=139.06 wypadkowa_pracodawca=0.0067
```

Uruchomienie wyliczające składowe pensji dla wynagrodzenia netto 2 500 zł:

```
pensja -n 2500
```

Lista parametrów
---

```
pensja -h
```

Źródła
---

* http://www.wskazniki.gofin.pl/8,223,2,przykladowe-obliczenie-wynagrodzenia-netto.html
* http://kariera.pracuj.pl/kalkulator-wynagrodzen/
* http://www.finanse.mf.gov.pl/pp/kalkulatory/kalkulator-wynagrodzen
