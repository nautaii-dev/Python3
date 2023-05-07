import requests
from googlesearch import search
import os
from bs4 import BeautifulSoup

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

def obtener_texto_html(url):
    """
    Obtiene el texto HTML de una URL y devuelve solo el texto.

    Args:
        url (str): La URL del sitio web del que se desea obtener el texto HTML.

    Returns:
        str: El texto HTML de la URL sin las etiquetas HTML.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()
    return texto

def descargar_html(url, folder_name='download_html'):
    """
    Descarga el archivo HTML de una URL y lo guarda en la carpeta especificada.

    Args:
        url (str): La URL del sitio web del que se desea descargar el HTML.
        folder_name (str): El nombre de la carpeta donde se desea guardar el archivo. El valor predeterminado es 'download_html'.

    Returns:
        None
    """
    # crear la carpeta de descarga si aún no existe
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # obtener el nombre del archivo
    file_name = url.split("/")[-1]

    # crear la ruta de archivo completa que incluya el nombre de la carpeta y el nombre del archivo
    file_path = os.path.join(folder_name, file_name)

    # descargar el archivo
    with open(file_path, 'w', encoding='utf-8') as f:
        response = requests.get(url)
        f.write(response.text)

    print(f"Archivo HTML descargado exitosamente en la carpeta '{folder_name}'.")

def descargar_imagenes(url, folder_name='download_html'):
    """
    Descarga todas las imágenes de una URL y las guarda en la carpeta especificada.

    Args:
        url (str): La URL del sitio web del que se desea descargar las imágenes.
        folder_name (str): El nombre de la carpeta donde se desea guardar las imágenes. El valor predeterminado es 'download_html'.

    Returns:
        None
    """
    # crear la carpeta de descarga si aún no existe
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # obtener el HTML de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # descargar todas las imágenes en la página
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url.startswith('http'):
            img_file_name = img_url.split("/")[-1]
            img_file_path = os.path.join(folder_name, img_file_name)
            with open(img_file_path, 'wb') as f:
                f.write(requests.get(img_url).content)

    print(f"Todas las imágenes descargadas exitosamente en la carpeta '{folder_name}'.")

# solicitar al usuario que ingrese la consulta de búsqueda en Google
query = input("Introduce la palabra a buscar en Google: ")
resultados = buscar_en_google(query)

# mostrar los resultados de la búsqueda
for resultado in resultados:
    print(resultado)

# solicitar al usuario que elija una URL de los resultados de búsqueda
numero = int(input("Introduce el número del resultado para mostrar las opciones: "))

if numero <= len(resultados):
    url = resultados[numero-1].split(' ')[1]

    # mostrar el menú de opciones
    print("Seleccione una opción:")
    print("1. Obtener solo texto HTML")
    print("2. Descargar HTML")
    print("3. Descargar imágenes")
    opcion = int(input("Introduce el número de la opción: "))

    # realizar la opción seleccionada
    if opcion == 1:
        texto = obtener_texto_html(url)
        print(texto)
    elif opcion == 2:
        descargar_html(url)
    elif opcion == 3:
        descargar_imagenes(url)
    else:
        print("Opción inválida.")
else:
    print("El número introducido no es válido.")
