import re
import bs4
import requests
import user_agent
import os
from tqdm import tqdm

folder_name = 'downloads'  # nombre de la carpeta donde se guardarán los archivos

# función para descargar el archivo y mostrar una barra de progreso
def download_file(url):
    # obtener el enlace de descarga de Mediafire
    link = get(url)

    # crear la carpeta de descarga si aún no existe
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # obtener el nombre del archivo del enlace de descarga
    file_name = link.split("/")[-1]

    # crear la ruta de archivo completa que incluya el nombre de la carpeta y el nombre del archivo
    file_path = os.path.join(folder_name, file_name)

    # descargar el archivo y mostrar una barra de progreso
    with requests.get(link, stream=True) as r, open(file_path, 'wb') as f, tqdm(unit='B', unit_scale=True, unit_divisor=1024, total=int(r.headers['Content-Length'])) as progress_bar:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            progress_bar.update(len(chunk))

    print("Archivo descargado exitosamente desde Mediafire.")

# función para obtener el enlace de descarga de Mediafire
def get(url):
    if re.match("download[0-9]*\.mediafire\.com", url.lstrip("https://").lstrip("http://").split("/")[0]):
        data = url.lstrip("https://").lstrip("http://").split("/")
        if len(data) <= 2:
            raise Exception("Invalid mediafire download url")
        unique_id = data[2]

    elif re.match("[w]*\.mediafire\.com", url.lstrip("https://").lstrip("http://").split("/")[0]):
        data = url.lstrip("https://").lstrip("http://").split("/")
        if len(data) <= 2:
            raise Exception("Invalid mediafire download url")
        unique_id = data[2]

    else:
        raise Exception("No se encontro ningun link de descarga")

    session = requests.Session()
    session.headers["User-Agent"] = user_agent.generate_user_agent()

    data = session.get(f"https://www.mediafire.com/file/{unique_id}/")
    wrp  = bs4.BeautifulSoup(data.text, "html.parser")
    btn  = wrp.find("a", attrs = {"id": "downloadButton"})
    if btn == None:
       raise Exception("Invalid download url")
    link = btn["href"]

    return link

# solicitar al usuario que ingrese la URL de descarga
url = input('Inserta la URL : ')

# descargar el archivo y mostrar una barra de progreso
print("Descargando archivo desde Mediafire...")
download_file(url)
