
class Stonepounds:
    def __init__(self, stone, pounds):
        self.stone = stone
        self.pound = pounds

    def convert(self):
        kilo = 6.35029 * self.stone
        kilo += 0.453592 * self.pound
        return kilo

class Entry:
    def __init__(self, date, name, kilo):
        self.date = date
        self.name = name
        self.kilo = kilo

def kiloToStone(kilo):
    stone = int(kilo * 0.157473)
    pounds = 14* ((kilo * 0.157473) %1 )
    return (stone, pounds)

def read_entries(filename):
    rawdata = open(filename, "r")

def write_entry(filename, entry):
    file = open(filename, "a")
    date = entry.date
    name = entry.name
    kilo = entry.name

if __name__ == '__main__':
    print "81kg in st is:"
    print kiloToStone(81)
    print "and 13st0 in kg is:"
    stone = Stonepounds(13, 0)
    print stone.convert()