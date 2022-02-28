#Metric to Imperial Conversions and Vice Versa
def convertfeettometers() -> float:
    feet = float(input("Enter foot length: "))
    print("{} feet is {:.4f} meters.".format(feet, feet * 0.3048))


def convertmeterstofeet() -> float:
    meters = float(input("Enter meter length: "))
    print("{} meters is {:.8f} feet.".format(meters, meters / 0.3048))


def convertkilogramstopounds() -> float:
    kilograms = float(input("Enter weight in KG: "))
    print("{} kilograms is {:.2f} pounds.".format(kilograms, kilograms / 0.45359237))


def convertpoundstokilograms() -> float:
    pounds = float(input("Enter weight in LBS: "))
    print("{} pounds is {:.2f} kilograms.".format(pounds, pounds * 0.45359237))

def convertgramstoounces() -> float:
    grams = float(input("Enter weight in Grams: "))
    print("{} grams is {:.10f} ounces.".format(grams, grams / 28.34952))

def convertouncestograms() -> float:
    ounces = float(input("Enter weight in Ounces: "))
    print("{} ounces is {:.5f} grams.".format(ounces, ounces * 28.34952))

def convertfahrenheittocelsius() -> float:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    print("{} degrees fahrenheit is {:.2f} degrees celsius.".format(fahrenheit, (fahrenheit - 32) * (5/9)))

def convertcelsiustofahrenheit() -> float:
    celsius = float(input("Enter temperature in celsius: "))
    print("{} degrees celsius is {:.2f} degrees fahrenheit.".format(celsius, (celsius * (9/5)) + 32))

convertfeettometers()
convertmeterstofeet()
convertkilogramstopounds()
convertpoundstokilograms()
convertgramstoounces()
convertouncestograms()
convertfahrenheittocelsius()
convertcelsiustofahrenheit()