from zeep import Client

client = Client('http://localhost:3000/mdc?wsdl')

x = int(input("Largura da imagem: "))
y = int(input("Altura da imagem: "))

mdc = client.service.CalculateMDC(x, y)
aspect_ratio = f'{x/mdc} : {y/mdc}'

print(f'MDC: {mdc}')
print(f'Aspect Ratio: {aspect_ratio}')