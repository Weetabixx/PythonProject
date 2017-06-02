
class Stonepounds: # a stone and pounds datatype
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

    def display(self):
        stonepound = kiloToStone(self.kilo)
        s = self.date + " - " + self.name + " - " + str(self.kilo) + "kg - " + str(stonepound[0]) + "st" + str(stonepound[1])
        print s


def kiloToStone(kilo):
    stone = int(kilo * 0.157473)
    pounds = 14 * ((kilo * 0.157473) % 1)
    return (stone, pounds)


def readEntries(filename):
    rawdata = open(filename, "r")
    lines = rawdata.readlines()
    entryList = []
    for line in lines:
        splitline = line.split(" - ")
        date = splitline[0]
        name = splitline[1]
        kilokg = splitline[2]
        kilo = float(kilokg[:-2])
        e = Entry(date,name,kilo)
        entryList.append(e)
    return entryList

def writeEntry(filename, entry):
    file = open(filename, "a+")
    date = entry.date
    name = entry.name
    kilo = entry.kilo
    stonepound = kiloToStone(kilo)
    entrystring = date + " - " + name + " - " + str(kilo) + "kg - " + str(stonepound[0]) + "st" + str(stonepound[1]) + "\n"
    file.write(entrystring)
    file.close()
    print "added entry to file"
    print entrystring

if __name__ == '__main__':
    pass


    # code to test writing and reading entries to file
    # e = Entry("02/06/2017", "robin", 77.5)
    # writeEntry("t.txt", e)
    # p = readEntries("t.txt")
    # for x in p:
        # x.display()

    # code to test converstion methods
    # print "81kg in st is:"
    # print kiloToStone(81)
    # print "and 13st0 in kg is:"
    # stone = Stonepounds(13, 0)
    # print stone.convert()
