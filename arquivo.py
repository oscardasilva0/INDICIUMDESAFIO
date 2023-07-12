import datetime
import os
class Arquivo:
    def __init__(self, nomeArquivo, pastaMae):
        self.nomeArquivo = nomeArquivo;
        self.pastaMae = pastaMae;
    
    def pasta(self):
        data=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S");
        pasta = os.path.join(os.getcwd(), 'data',  data,self.pastaMae);
        os.makedirs(pasta, exist_ok=True);
        return pasta;

    def escreverArquivo(self,dados):
        pasta = self.pasta();
        arquivo = open("{}/{}.txt".format(pasta,self.nomeArquivo),'w');
        for dado in dados:
            arquivo.write(str(dado),';');
        arquivo.close();

