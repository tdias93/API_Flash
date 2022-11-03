from flask import Flask, make_response, jsonify, request, abort
from jsonschema import validate, ValidationError, Draft202012Validator, SchemaError

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/teste', methods=['POST'])
def creat_nf():

    try:
        validate(instance=request.json, schema=schema)

        nf = request.json
        dados.append(nf)

        retorno = make_response(jsonify(mensage = f'CADASTRO REALIZADO')), 200

    except SchemaError as e:
        print("There is an error with the schema")
    
    except ValidationError as err:
        retorno = make_response(jsonify(mensage = f'ERRO DE SINTAXE - JSON PATH: {err.path[0]}, MESSAGE: {err.message}')), 400
        #abort(400, 'ERRO DE SINTAXE - {err.message}', "TESTE")

    except:
        retorno = make_response(jsonify(mensage = f'ERRO DE SINTAXE')), 500

    return retorno


schema = {
    "type": "object",
    "properties": {
        "cnpj": {
            "type" : "string"
            },
        "nome": {
            "type" : "string"
            },
        "nota_fiscal": {
            "type" : "string"
            },
        "conhecimento": {
            "type" : "string"
            },
        "data_emissao": {
            "type" : "string"
            },
        "comprovante": {
            "type" : "string"
            },
    },
    "required":[
      "cnpj",
      "nota_fiscal",
      "conhecimento",
      "data_emissao",
      "comprovante"
   ]
}

dados = [
    {
        "cnpj": "10750264000116",
        "nome": "TESTE 01",
        "nota_fiscal": "1234",
        "conhecimento": "5678",
        "data_emissao": "10/05/2022",
        "comprovante": "IMAGEM - BINARIA"
    }
]

# https://www.youtube.com/watch?v=LP8besicfH4

app.run()