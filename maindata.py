import plotly
from plotly.graph_objs import Scatter, Layout

class Stonepounds:  # a stone and pounds datatype
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
        stlb = kiloToStone(self.kilo)
        s = self.date + " - " + self.name + " - " + str(self.kilo) + "kg - " + str(stlb[0]) + "st" + str(stlb[1])
        print(s)


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
        e = Entry(date, name, kilo)
        entryList.append(e)
    return entryList

def writeEntry(filename, entry):
    f = open(filename, "a+")
    date = entry.date
    name = entry.name
    kilo = entry.kilo
    stlb = kiloToStone(kilo)
    entrystring = date + " - " + name + " - " + str(kilo) + "kg - " + str(stlb[0]) + "st" + str(stlb[1]) + "\n"
    f.write(entrystring)
    f.close()
    print("added entry to file")
    print(entrystring)


def menu():
    data = readEntries("weight.txt")

if __name__ == '__main__':
    plotly.offline.plot({
        "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": Layout(title="hello world")
    })


    # code to test writing and reading entries to file
    # e = Entry("02/06/2017", "robin", 77.5)
    # writeEntry("t.txt", e)
    # p = readEntries("t.txt")
    # for x in p:
    #     x.display()

    # code to test converstion methods
    # print "81kg in st is:"
    # print kiloToStone(81)
    # print "and 13st0 in kg is:"
    # stone = Stonepounds(13, 0)
    # print stone.convert()
