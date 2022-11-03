from flask import Flask, make_response, jsonify, request
from jsonschema import validate, ValidationError, SchemaError

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/comprovante', methods=['POST'])
def creat_nf():

    try:
        validate(instance=request.json, schema=schema)

        nf = request.json
        dados.append(nf)

        retorno = make_response(jsonify(status = 'OK', mensage = f'CADASTRO REALIZADO')), 200

    except SchemaError as err:
        retorno = make_response(jsonify(status = 'ERROR', mensage = err.message)), 400
    
    except ValidationError as err:
        if err.validator == 'type':
            retorno = make_response(jsonify(status = 'ERROR', mensage = f'JSON PATH: {err.path[0]}, MESSAGE: {err.message}')), 400
        else:
            retorno = make_response(jsonify(status = 'ERROR', mensage = err.message)), 400

    except:
        retorno = make_response(jsonify(mensage = f'Internal Server Error')), 500

    return retorno


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
    },
    "required":[
      "cnpj_faturado",
      "conhecimento",
      "nota_fiscal",
      "nome_integracao",
      "data_emissao",
      "imagem"
   ]
}

dados = [
    {
        "cnpj_faturado": "10750264000116",
        "conhecimento": "123456",
        "nota_fiscal": "1234",
        "nome_integracao": "Frete Rápido - 1",
        "data_emissao": "2022-10-03 13:58:00",
        "imagem": "basa64"
    }
]

# https://www.youtube.com/watch?v=LP8besicfH4
# https://opis.io/json-schema/2.x/formats.html
# https://www.devmedia.com.br/http-status-code/41222#4-1

app.run()