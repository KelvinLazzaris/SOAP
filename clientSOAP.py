import zeep

link = 'http://www.dneonline.com/calculator.asmx?WSDL'

client = zeep.Client(wsdl = link)

resultado = client.service.Add(intA = 10, intB = 5)
print("Resultado da adição:", resultado)

resultado = client.service.Subtract(intA = 10, intB = 5)
print("Resultado da subtração:", resultado)

resultado = client.service.Multiply(intA = 10, intB = 5)
print("Resultado da multiplicação:", resultado)

resultado = client.service.Divide(intA = 10, intB = 5)
print("Resultado da divisão:", resultado)