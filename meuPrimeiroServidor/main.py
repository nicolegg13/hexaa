import flask


def main():
    app = flask.Flask(
        'meu servidor',
        template_folder='templates',
        static_folder='static'
    )

    @app.route('/', methods=['GET'])
    def main_page(): #roteamento para pagina inicial
        return flask.render_template(
            'index.html',
            meu_novo_paragrafo='<p>Parágrafo gerado por servidor</p>'
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

        response = flask.jsonfy({'jogador': jogador})
        response.headers.add('Access-Control-Allow-Origin', '*') #a
        return response #retorna resposta para pagina inicial


    app.register_error_handler(404, page_not_found)

    app.run(debug=True)

if __name__ == '__main__':
    main()
