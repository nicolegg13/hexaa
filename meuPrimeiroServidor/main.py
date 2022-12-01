import sqlite3

import flask


def main():
    app = flask.Flask(
        'meu servidor',
        template_folder='templates',
        static_folder='static'
    )

    @app.route('/', methods=['GET'])
    def main_page(): #roteamento para pagina inicial
        with sqlite3.connect('static/database/test.db') as con: #comando sql com cursor
            cur = con.cursor()
            #retorna uma lista de tuplas
            cur.execute('SELECT valor, nome FROM jogadores;') #pega valor e nome - transformar em lista de tuplas
            texto_do_seletor = [] #lista vazia
            for line in answer: #para cada linha de resposta (jogador)
                texto_do_seletor.append(
                    '<option value="{0}">{1}</option>'.format( #formata string
                        line[0], line[1]  #e adiciona na lista
                    )
                )
            texto_do_seletor = '\n'.join(texto_do_seletor) #transforma em string


        return flask.render_template(
            'index.html',
            meu_novo_paragrafo='<p>brasil espancou macetou comeu servia</p>',
            meu_seletor=texto_do_seletor
        )

    @app.route('/hexa', methods=['GET'])
    def pagina_da_copa():  # roteamento para pagina do hexa
        return flask.render_template(
            'hexa.html',
            #meu_novo_paragrafo='<p>Hoje o Brasil espanca maceta debulha fode vergasta sova surra casca soca golpeia esbofeteia esmurra açoita amassa desanca esbordoa agride fustiga a Sérvia!!!</p>'
        )

    @app.errorhandler(404)
    def page_not_found(page):  # pagina de erro 404
        return flask.render_template('404.html'), 404

    @app.route('/jogadores', methods=['POST'])
    def hexa():
        jogador = flask.request.form.get('selecionado')
        print('o jogador selecionado foi ', jogador)

        response = flask.jsonify({'jogador': jogador})
        response.headers.add('Access-Control-Allow-Origin', '*') #a
        return response #retorna resposta para pagina inicial


    app.register_error_handler(404, page_not_found)

    app.run(debug=True)

if __name__ == '__main__':
    main()
