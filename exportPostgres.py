from arquivo import Arquivo
from pesquisa import PesquisaBanco

def run():
    tabelas = ['customer_customer_demo','customer_demographics','employee_territories','orders','customers','products','shippers','suppliers','territories','us_states','categories','region','employees'];
    for tabela in tabelas:
        pes = PesquisaBanco();
        arquivo = Arquivo(tabela, 'postgres');
        dadosTabela = pes.pesquisar(tabela);
        arquivo.escreverArquivo(dadosTabela);
        pes.fechar();

if __name__ == "__main__":
   run();
    


