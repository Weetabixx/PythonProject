import plotly as py
import plotly.graph_objs as go


class Stonepounds:  # a stone and pounds data type
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
        dateparts = date.split("/")  # this part converts the date to a number
        datenumbers = []
        for x in dateparts:
            datenumbers.append(int(x))
        self.day = datenumbers[0]  # add days
        self.day += datenumbers[2]*365  # add years
        self.day += int(datenumbers[2] / 4)  # add leap days
        self.day -= int(datenumbers[2] / 100)  # remove century leap days
        self.day += int(datenumbers[2] / 400)  # add every 400 years leap day
        if datenumbers[2] % 4 == 0:
            if datenumbers[1] < 2:  # if leap year but before end of february
                self.day -= 1
        if datenumbers[1] == 1:  # add month case for january, february ...
            self.day += 0
        elif datenumbers[1] == 2:
            self.day += 31
        elif datenumbers[1] == 3:
            self.day += 59
        elif datenumbers[1] == 4:
            self.day += 90
        elif datenumbers[1] == 5:
            self.day += 120
        elif datenumbers[1] == 6:
            self.day += 151
        elif datenumbers[1] == 7:
            self.day += 181
        elif datenumbers[1] == 8:
            self.day += 212
        elif datenumbers[1] == 9:
            self.day += 243
        elif datenumbers[1] == 10:
            self.day += 273
        elif datenumbers[1] == 11:
            self.day += 304
        elif datenumbers[1] == 12:
            self.day += 334
        else:
            print("that month does not seem to exist")
        if datenumbers[0] > 31:
            print("that day does not seem to exist")

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
        if len(splitline) >= 3:
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


def addd():
    print("for whom is this entry:")
    name = input()
    print("what day was this measurement taken? dd/mm/yyyy")
    date = input()
    gotmeasurement = False
    while gotmeasurement == False:
        print("is the measurement in kilo(kg) or stone(st)? write kg or st")
        type = input()
        if type == "st":
            print("how many stone?")
            stone = int(input())
            print("how many pounds?")
            pounds = float(input())
            w = Stonepounds(stone, pounds)
            kilo = w.convert()
            gotmeasurement = True
        elif type == "kg":
            print("how many kg?")
            kilo = float(input())
            gotmeasurement = True
        else:
            print("sorry i don't understand that measurement type")
    measurement = Entry(date, name, kilo)
    print("adding: ")
    measurement.display()
    return measurement


def graph(rawdata):
    print("would you like a kg graph or a stone graph?(write kg or st)")
    choice = input()
    stone = False
    if choice == "st":
        stone = True
    peopleweight = {}
    peopledate = {}
    for x in rawdata:
        peopleweight[x.name] = []
        peopledate[x.name] = []
    for x in rawdata:
        peopleweight[x.name].append(x.kilo)
        peopledate[x.name].append(x.day)
    lines = []
    for person in peopleweight:
        linex = go.Scatter(
            x=peopledate[person],
            y=peopleweight[person],
            mode='lines+markers',
            name=person
        )
        lines.append(linex)
    layout = go.Layout(
        title='Weight Progress'
    )
    fig = go.Figure(data=lines, layout=layout)
    py.offline.plot(fig, filename='WeightProgress.html')
    #plotly.offline.plot({
    #    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1], mode='lines+markers', name='line')],
    #    "layout": Layout(title="Weight Progress")
    #}, filename='weight-graph.html')


def menu():
    print("reading existing entries...")
    try:
        data = readEntries("weight.txt")  # change this to whatever file has the entries
        for e in data:
            e.display()
    except IOError:
        print("could'nt find any entries")
        data = []
    command = ""
    while command != "exit":
        print("what would you like to do?")
        print("add - adds a entry")
        print("graph - creates a graph of the current entries")
        print("exit - exits application")
        print("data - prints existing data points")
        command = input()
        if command == "add":
            newEntry = addd()
            data.append(newEntry)
            writeEntry("weight.txt", newEntry)
        elif command == "graph":
            graph(data)
        elif command == "data":
            for e in data:
                e.display()
        elif command != "exit":
            print("sorry, i couldn't understand you.")


if __name__ == '__main__':
    menu()

    # code to test plotly library
    # plotly.offline.plot({
    #     "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    #     "layout": Layout(title="hello world")
    # })

    # code to test writing and reading entries to file
    # e = Entry("02/06/2017", "robin", 77.5)
    # writeEntry("t.txt", e)
    # p = readEntries("t.txt")
    # for x in p:
    #     x.display()

    # code to test conversion methods
    # print "81kg in st is:"
    # print kiloToStone(81)
    # print "and 13st0 in kg is:"
    # stone = Stonepounds(13, 0)
    # print stone.convert()
