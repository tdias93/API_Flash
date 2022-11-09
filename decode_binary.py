import base64
import random, string, os

class Decode():

    def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


    def DecodeBinary(file, extencao):

        """ Converte Binario para Arquivo

        Args:
            file (str)     : Código Binario
            extencao (str) : Extenção Original do Arquivo

        
        Returns:
            dirArquivo : Caminho do Arquivo Convertido
            ArquivoNew : Nome do Arquivo
            url        : URL do Arquivo Convertido
            status     : Status da Conversão (OK ou Error)
            errorDesc  : Descrição do Erro

        """
        
        nome = Decode.random_generator()

        try:

            if extencao.upper() == '.PDF':

                decoded_file = base64.b64decode(file)
                file_dir = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\file\\{nome}.PDF'

                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close

            else:

                decoded_file = base64.b64decode(file)
                file_dir = f'{os.path.dirname(os.path.realpath(__file__))}\\system\\file\\{nome}.JPG'

                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close


            return file_dir

        except:

            return 'Erro de Conversão Binario'
