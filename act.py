import bitly_api

# Pide al usuario que introduzca la URL que quiere acortar
url = input("Introduzca la URL que desea acortar: ")

# Crea una instancia del cliente de Bitly con tu access token
ACCESS_TOKEN = 'bd7a267a7c49335acbbafa1d634a95ceda76b777'
b = bitly_api.Connection(access_token=ACCESS_TOKEN)

# Imprime un mensaje de procesamiento
print("Procesando la URL...")

# Acorta la URL
short_url = b.shorten(url)['url']

# Imprime la URL acortada
print("Aquí está su URL acortada: " + short_url)
