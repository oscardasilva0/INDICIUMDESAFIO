from arquivo import Arquivo
import csv

def run():
    with open('order_details.csv') as file:
        ler_csv = csv.DictReader(file)
        arquivo = Arquivo('order_details', 'csv')
        arquivo.escreverArquivo(ler_csv)
if __name__ == "__main__":
    run();

    


