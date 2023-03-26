from flask import Flask,render_template,request
from models.filme import Filme
import requests
import json
app = Flask(__name__)
@app.route('/')
def index():
    res = requests.get(f'https://Restfull.williamrx777.repl.co')
    response=res.json()
   
    return render_template('index.html',
                           response=response                      
                           )
    pass
@app.route('/buscar', methods=["GET","POST"])
def buscar():
    try:
        api = Filme(request.form['id'],['nome'],['imagem'],['filme'])
        res = json.loads(requests.get(f'https://Restfull.williamrx777.repl.co/{api.id}').text)
        id = res['id']
        nome = res['nome']
        imagem = res['imagem']
        filme = res['filme']
        api.id = id
        api.nome = nome
        api.imagem = imagem
        api.filme = filme
    except:
       return '<h1>Não ha filmes</h1>'
    return render_template('index.html',
                          nome=api.nome,  
                          imagem=api.imagem,
                          filme=api.filme,
                          id=api.id  
    )   


if __name__=='__main__':
    app.run(debug=True, port=5555)    
