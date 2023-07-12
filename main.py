from importCSV import run as importCSV;
from importPostgres import run as importPostgres;
from exportJson import run as exportJson;

if __name__ == "__main__":
  importCSV();
  importPostgres();
  #exportJson();
    