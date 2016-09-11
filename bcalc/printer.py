class Printer:
    def __init__(self, separatorLength=50):
        self.separatorLength = separatorLength

    def printSeparator(self, val):
        print('-' * self.separatorLength, file=val)

    def printLabelValue(self, label, value, curr, val):
        print('{: <34} {: >12,.2f} {}'.format(label + ':', value, curr), file=val)
