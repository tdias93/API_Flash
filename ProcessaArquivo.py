import os
import configparser

from PIL import Image
#from struct import pack
from ReportLog import Log
from datetime import datetime
from pdf2image import convert_from_path


#----------------------------------------------------------
#   CONVERTE IMAGEM PARA JPG
#----------------------------------------------------------
def ProcessaArquivo(dirProvisorio, extArquivo, integracao, cnpjCliente, numeroNf, dtEmissao):

    """ Converte Imagens para o Formato JPG

        Args:
            dirProvisorio (str) : Caminho do nomArquivo que sera Convertido
            extArquivo    (str) : Extenção do Arquivo
            integracao    (str) : Nome da Integração 
            cnpjCliente   (str) : CNPJ do cliente responsavel
            numeroNf      (str) : Número da nota fiscal
            dtEmissao     (str) : Data de emissão do CTe
        
        Returns:
            status     : True -> Proceeso OK | False -> Processo com Falha
            dirArquivo : Link Compartilhado

    """
     
    # Carrega informações de configuração
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(os.path.realpath(__file__))}/system/config.ini")

    host = config.get('DIR', 'host')        # Le Arquivo .ini e retorna o host
    raiz = config.get('DIR', 'raiz')        # Le Arquivo .ini e retorna o dir raiz
       
    Log(event = 'CONVERTENDO IMAGEM', eventLog = 'INICIANDO CONVERSAO DE IMAGEM PARA JPG', terminal = False)  # Gera Log de Execução
    Log(event = 'CONVERTENDO IMAGEM', eventLog = f'Arquivo: {dirProvisorio}', terminal = False)               # Gera Log de Execução
    
    # Lista com os meses do ano
    listMes = ['OUTROS','JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']

    # Converte data de string para date
    data = datetime.strptime(dtEmissao, '%Y-%m-%d')

    # Estrutura da pasta
    estruturaPasta = f'{integracao}\\{str(data.year)}\\{listMes[data.month]}\\{str("%02d" % data.day)}\\'

    # Diretorio raiz
    dirArquivo = f'{raiz}\\{estruturaPasta}'

    # Nome do arquivo
    nomeArquivo = f'{cnpjCliente}_{numeroNf}.jpg'
    
    # Valida se o diretorio existe
    if not os.path.exists(dirArquivo):
        os.makedirs(dirArquivo)

    # Diretorio absoluto
    dirArquivo = f'{dirArquivo}\\{nomeArquivo}'

    try:

        # Valida extenção da imagem
        if extArquivo.upper() == '.PDF':

            filePath = dirProvisorio
            popplerPath = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\poppler-0.68.0\\bin'

            if os.name == 'nt':

                # Abre arquivo da imagem
                # imagem = convert_from_path(filePath, poppler_path = popplerPath)

                for rgbImg in convert_from_path(filePath, poppler_path = popplerPath):
                    rgbImg.save(dirArquivo, 'JPEG')

            else:

                for rgbImg in convert_from_path(filePath):
                    rgbImg.save(dirArquivo, 'JPEG')

                # Abre arquivo da imagem
                #imagem = convert_from_path(filePath)


            # Salva binario
            """ for rgbImg in imagem:
                rgbImg.save(dirArquivo, 'JPEG') """

        else:

            # Abre arquivo da imagem
            imagem = Image.open(dirProvisorio)

            # Converte imagem para binario
            rgbImg = imagem.convert('RGB')

            # Salva binario
            rgbImg.save(dirArquivo)

        Log(event = 'CONVERTENDO IMAGEM', eventLog = 'CONVERSAO REALIZADA COM SUCESSO', terminal = False)        # Gera Log de Execução

        # Remove arquivo provisorio
        os.remove(dirProvisorio)

        status = True
        url = host + estruturaPasta.replace('\\', '/') + nomeArquivo

        return status, url

    except Exception as errorDesc:
    
        status = False

        Log(event = 'CONVERTENDO IMAGEM', error = errorDesc, terminal = False) # Gera Log de Execução

        # Remove arquivo provisorio
        os.remove(dirProvisorio)

        return status


if __name__ == '__main__':
    ProcessaArquivo(dirProvisorio = '', extArquivo = '', integracao = '', cnpjCliente = '', numeroNf = '', dtEmissao = '')