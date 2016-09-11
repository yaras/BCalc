from io import StringIO

class WynagrodzenieChorobowePrettyPrinter:
    def __init__(self, separatorLength=50):
        self.separatorLength = separatorLength

    def format(self, ch):
        val = StringIO()

        print('Wyliczenie wynagrodzenia chorobowego', file=val)
        print('-' * self.separatorLength, file=val)

        print('Dni choroby:                     {: >12,.2f}'.format(ch.choroba), file=val)
        print('Procent składki:                 {: >12,.2f} %'.format(ch.procent_skladki * 100), file=val)
        print('Średnia miesięczna:              {: >12,.2f} {}'.format(ch.srednia, ch.waluta), file=val)
        print('Podstawa miesięczna:             {: >12,.2f} {}'.format(ch.podstawa, ch.waluta), file=val)
        print('Zasiłek dziennie:                {: >12,.2f} {}'.format(ch.zasilek_dziennie, ch.waluta), file=val)
        print('-' * self.separatorLength, file=val)
        print('', file=val)
        print('Zasiłek chorobowy:               {: >12,.2f} {}'.format(ch.wynagrodzenie_chorobowe, ch.waluta), file=val)
        print('Potrącenie z pensji:             {: >12,.2f} {}'.format(ch.potracenie, ch.waluta), file=val)
        print('Różnica (potr.- zasiłek:)        {: >12,.2f} {}'.format(ch.potracenie - ch.wynagrodzenie_chorobowe, ch.waluta), file=val)
        print('Wynagrodzenie z potrąceniem:     {: >12,.2f} {}'.format(ch.wynagrodzenie, ch.waluta), file=val)
        print('Brutto (wynagrodzenie+zasiłek):  {: >12,.2f} {}'.format(ch.wynagrodzenie_zasilek, ch.waluta), file=val)

        return val.getvalue()
