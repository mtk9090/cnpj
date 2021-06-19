from flask import Flask,render_template, request
import requests



app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    pegar = request.form.get('cnpj')
    print(pegar)
    try:
        url = f'https://www.receitaws.com.br/v1/cnpj/{pegar}'
        req = requests.get(url)
        resp = req.json()
    except:
        return render_template('404.html')


    else:
        return render_template('cnpj.html', req=resp)




@app.errorhandler(404)
def page_not_found(e):

    ip_address = request.remote_addr

    use_agente = request.headers.get('User-Agent')

    return render_template('404.html',use_agente=use_agente,ip_address=ip_address), 404



 
if __name__ == '__main__':
    import os
 
    host = '0.0.0.0'
    port  = int(os.environ.get("PORT", 5000))
 
    app.run(host, port)
