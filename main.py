from flask import Flask, make_response, jsonify, request
from jsonschema import validate, ValidationError, SchemaError
from DecodeBinary import Decode
from ProcessaArquivo import ProcessaArquivo


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Rota do EndPoint
@app.route('/comprovante', methods=['POST'])
def Comprovante():

    try:

        # Valida Configuração do Json com a estrutura enviada
        validate(instance=request.json, schema=schema)

        nf = request.json

        # Transforma binario em arquivo
        processo = Decode.DecodeBinary(nf['imagem'], nf['extencao'])

        if processo[0]:

            # Converte arquivos para JPG e gera link compartilhado
            processo = ProcessaArquivo(processo[1], nf['extencao'], nf['nome_integracao'], nf['cnpj_faturado'], nf['nota_fiscal'], nf['data_emissao'])

            # Monta Json de Retorno
            retorno = make_response(jsonify(status = 'OK', mensage = f'CADASTRO REALIZADO', link = processo[1])), 200

        else: 

            # Monta Json de Retorno
            retorno = make_response(jsonify(mensage = f'Internal Server Error')), 500


    except SchemaError as err:

        # Monta Json de Retorno
        retorno = make_response(jsonify(status = 'ERROR', mensage = err.message)), 400
    
    except ValidationError as err:

        # Valida o tipo do erro na estrutura
        if err.validator == 'type':

            # Monta Json de Retorno
            retorno = make_response(jsonify(status = 'ERROR', mensage = f'JSON PATH: {err.path[0]}, MESSAGE: {err.message}')), 400
        else:

            # Monta Json de Retorno
            retorno = make_response(jsonify(status = 'ERROR', mensage = err.message)), 400

    except Exception as errorDesc:

        # Monta Json de Retorno
        retorno = make_response(jsonify(mensage = f'Internal Server Error')), 500

    return retorno

# https://www.youtube.com/watch?v=LP8besicfH4
# https://opis.io/json-schema/2.x/formats.html
# https://www.devmedia.com.br/http-status-code/41222#4-1


# Configuração da estrutura JSON
schema = {
    "type": "object",
    "properties": {
        "cnpj_faturado": {
            "type" : "string"
            },
        "conhecimento": {
            "type" : "string"
            },
        "nota_fiscal": {
            "type" : "string"
            },
        "nome_integracao": {
            "type" : "string"
            },
        "data_emissao": {
            "type": "string",
            "format": "date-time"
            },
        "imagem": {
            "type" : "string"
            },
        "extencao": {
            "type" : "string"
            },
    },
    "required":[
      "cnpj_faturado",
      "conhecimento",
      "nota_fiscal",
      "nome_integracao",
      "data_emissao",
      "imagem",
      "extencao"
   ]
}

if __name__ == '__main__':
    app.run()