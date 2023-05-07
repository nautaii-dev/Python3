import requests
from googlesearch import search

def buscar_en_google(query, num_results=10):
    """
    Realiza una búsqueda en Google y devuelve los resultados.

    Args:
        query (str): La consulta que se desea buscar.
        num_results (int): El número máximo de resultados que se devuelven. El valor predeterminado es 10.

    Returns:
        list: Una lista de cadenas que representan los resultados de la búsqueda.
    """
    resultados = []
    for i, resultado in enumerate(search(query, num_results=num_results), start=1):
        resultados.append(f"{i}. {resultado}")

    return resultados

query = input("Introduce la palabra a buscar en Google: ")
resultados = buscar_en_google(query)

for resultado in resultados:
    print(resultado)

numero = int(input("Introduce el número del resultado para mostrar el HTML: "))

if numero <= len(resultados):
    url = resultados[numero-1].split(' ')[1]
    response = requests.get(url)
    print(response.text)
else:
    print("El número introducido no es válido.")
