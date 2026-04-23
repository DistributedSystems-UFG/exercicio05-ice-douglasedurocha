import sys, Ice
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World!")
    printer.printUpperCase("hello world in uppercase")
    reversed_text = printer.reverse("Hello World!")
    print("Reversed:", reversed_text)

    base2 = communicator.stringToProxy("SimpleCalculator:default -p 11000")
    calculator = Demo.CalculatorPrx.checkedCast(base2)
    if not calculator:
        raise RuntimeError("Invalid proxy")

    result = calculator.add(10, 5)
    print("10 + 5 =", result)

    result = calculator.subtract(10, 5)
    print("10 - 5 =", result)
