import base64, random, string, os

from ReportLog import Log

class Decode():

    def random_generator(size=10):

        """ Gera String Aleatorio

        Args:
            size  (int) : Quantidade de Digitos da String Gerada

        Returns:
            text : Valor Gerado

        """

        text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

        return text


    def DecodeBinary(file, extencao):

        """ Converte Binario para Arquivo

        Args:
            file (str)     : Código Binario
            extencao (str) : Extenção Original do Arquivo

        Returns:
            status   : True -> Proceeso OK | False -> Processo com Falha
            file_dir : Caminho Absoluto do Arquivo

        """
        
        # Gera nome aleatorio para o arquivo
        nome = Decode.random_generator()

        try:

            Log(event = 'CONVERTENDO BINARIO', eventLog = 'INICIANDO CONVERSAO DE BINARIO PARA ARQUIVO', terminal = False)  # Gera Log de Execução
            Log(event = 'CONVERTENDO IMAGEM', eventLog = f'Arquivo: {file}', terminal = False)                              # Gera Log de Execução

            # Valida a extenção
            if extencao.upper() == '.PDF':

                # Decodifica o binaro
                decoded_file = base64.b64decode(file)

                # Monta o diretorio do arquivo
                file_dir = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\file\\{nome}.PDF'

                # Escreve o arquivo no diretorio apontado
                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close

            else:

                # Decodifica o binaro
                decoded_file = base64.b64decode(file)

                # Monta o diretorio do arquivo
                file_dir = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\file\\{nome}.JPG'

                # Escreve o arquivo no diretorio apontado
                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close


            Log(event = 'CONVERTENDO BINARIO', eventLog = 'CONVERSAO REALIZADA COM SUCESSO', terminal = False)  # Gera Log de Execução

            status = True

            return status, file_dir


        except Exception as errorDesc:

            status = False
            Log(event = 'CONVERTENDO IMAGEM', error = errorDesc, terminal = False) # Gera Log de Execução

            return status
