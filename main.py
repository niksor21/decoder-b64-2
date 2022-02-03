import base64
coded_string = input('Введите строку base64: ')
coded_string = base64.b64decode(coded_string)
print(coded_string)