from googlesearch import search

query = input("Introduce la palabra a buscar en Google: ")

for j in search(query, num_results=10):
    print(j)
