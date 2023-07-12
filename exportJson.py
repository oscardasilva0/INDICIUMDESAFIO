
def run():
  arq = open("data/2023-07-11_21-39-53/postgres/orders.txt","r")
  linhas = arq.readlines()
  for linha in linhas:
      print(linha);
  arq.close();
if __name__ == "__main__":
    run();

    


