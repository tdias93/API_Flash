import os
import configparser

from PIL import Image
#from struct import pack
#from ReportLog import Log
from datetime import datetime
from pdf2image import convert_from_path


#----------------------------------------------------------
#   CONVERTE IMAGEM PARA JPG
#----------------------------------------------------------
def Convertjpg(dirProvisorio, extArquivo, integracao, cnpjCliente, numeroNf, dtEmissao):

    """ Converte Imagens para o Formato JPG

        Args:
            dirProvisorio (str) : Caminho do nomArquivo que sera Convertido
            extArquivo    (str) : Extenção do Arquivo
            integracao    (str) : Nome da Integração 
            cnpjCliente   (str) : CNPJ do cliente responsavel
            numeroNf      (str) : Número da nota fiscal
            dtEmissao     (str) : Data de emissão do CTe
        
        Returns:
            dirProvisorio : Caminho do Arquivo Convertido
            ArquivoNew    : Nome do Arquivo
            url           : URL do Arquivo Convertido
            status        : Status da Conversão (OK ou Error)
            errorDesc     : Descrição do Erro

    """

    """ 
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(os.path.realpath(__file__))}\\system\\Config.ini")

    host = config.get('DIR', 'host')        # Le Arquivo .ini e retorna o host
    raiz = config.get('DIR', 'raiz')        # Le Arquivo .ini e retorna o dir raiz
    
    Log(event = 'CONVERTENDO IMAGEM', eventLog = 'INICIANDO CONVERSAO DE IMAGEM PARA JPG', terminal = False)  # Gera Log de Execução
    Log(event = 'CONVERTENDO IMAGEM', eventLog = f'Arquivo: {dirProvisorio}', terminal = False)                  # Gera Log de Execução
    """

    listMes = ['OUTROS','JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
    raiz = f'{os.path.dirname(os.path.realpath(__file__))}\\system'

    data = datetime.strptime(dtEmissao, '%Y-%m-%d')

    # Diretorio para salvar imagem
    dirArquivo = f'{raiz}\\{integracao}\\{str(data.year)}\\{listMes[data.month]}\\{str(data.day)}\\'

    # Valida se o diretorio existe
    if not os.path.exists(dirArquivo):
        os.makedirs(dirArquivo)

    # Renomei arquivo passando nova extensão
    dirArquivo = f'{dirArquivo}\\{cnpjCliente}_{numeroNf}.jpg'

    try:

        # Valida extenção da imagem
        if extArquivo.upper() == '.PDF':

            filePath = dirProvisorio
            popplerPath = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\poppler-0.68.0\\bin'

            # Abre arquivo da imagem
            imagem = convert_from_path(filePath, poppler_path = popplerPath)

            # Salva binario
            for rgbImg in imagem:
                rgbImg.save(dirArquivo, 'JPEG')

        else:

            # Abre arquivo da imagem
            imagem = Image.open(dirProvisorio)

            # Converte imagem para binario
            rgbImg = imagem.convert('RGB')

            # Salva binario
            rgbImg.save(dirArquivo)

        #Log(event = 'CONVERTENDO IMAGEM', eventLog = 'CONVERSÃO REALIZADA COM SUCESSO', terminal = False)        # Gera Log de Execução
        #Log(event = 'CONVERTENDO IMAGEM', eventLog = f'Arquivo: {dirArquivoNew + nomArquivo}', terminal = False) # Gera Log de Execução

        status = 'OK'

        return dirArquivo, status

    except Exception as err:
    
        status = 'ERROR'
        errorDesc = str(err)

        #Log(event = 'CONVERTENDO IMAGEM', error = errorDesc, terminal = False) # Gera Log de Execução

        return '', status, errorDesc


if __name__ == '__main__':
    Convertjpg(dirProvisorio = '', extArquivo = '', integracao = '', cnpjCliente = '', numeroNf = '', dtEmissao = '')