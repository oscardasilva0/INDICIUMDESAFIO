import psycopg2

class PesquisaBanco:
    def __init__(self):
        self.connecao = psycopg2.connect(host='localhost',database='northwind',
        user='postgres', password='root');
        self.cur = self.connecao.cursor();
        
    
    def pesquisar(self, tabela):
        self.cur.execute('select * from {}'.format(tabela));
        recset = self.cur.fetchall();
        return recset;

    def fechar(self):
        self.connecao.close();