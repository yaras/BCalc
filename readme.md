BCalc
===

BCalc (Business Calculator) is a script for calculating salary and taxes for wage in Poland.

Wymagania
---

* Python 3.x

Instalacja
---

```
python -m venv .env
.env\Scripts\activate
pip install https://github.com/yaras/BCalc/releases/download/v0.1.0/BCalc-0.1.0-py3-none-any.whl
```

Uruchomienie
---

Po instalacji *wheel* dostępne są dwa polecenia:

* `pensja`
* `chorobowe`

Opis składowych komponentów
---

pensja
---

Skrypt wyliczający składowe pensji. Opis tutaj: *[pensja](pensja.md)*.


chorobowe
---

Skrypt wyliczający wyskość zasiłku chorobowego dla podanej pensji. Opis tutaj: *[chorobowe](chorobowe.md)*

Nadpisywanie wartości konfiguracji
---

Wszystkie parametry służące do wyliczeń znajdują się w pliku `config.json`. Parametry te można nadpisać w tym pliku lub stworzyć nowy i wprowadzić zaktualizowane wartości parametrów na podstawie pliku `config.json`. W celu przekazania zmodyfikowanych wartości należy uruchomić skrypt z odpowiednim przełącznikiem. Zakładając, że w pliku `config_new.json` zapisano zmodyfikowane parametry, skrypt wczyta wszystkie parametry z `config.json` oraz nadpisze wszystkie wartości na podstawie pliku `config_new.json`. Uruchomienie dla pensji:

```
pensja -c config_new.json [...]
```

Parametry można również modyfikować pojedynczo:

```
pensja --param koszty_miejscowe=139.06 wypadkowa_pracodawca=0.0067
```

Opis parametrów w konfiguracji
---

Patrz *[config.md](config.md)*

Uruchomienie testów
---

```
nosetests --with-coverage --cover-html
```

Budowanie wheel
---

```
python setup.py bdist_wheel
```
