import urllib
from utils import load_data, load_template, add_note, build_response

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '') 
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave_valor = chave_valor.split('=')
            valor = urllib.parse.unquote_plus(chave_valor[1], encoding='utf-8', errors='replace')
            params[chave_valor[0]] = valor

        add_note(params)

        # Retorna o resultado de build_response para redirecionar após o POST
        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # Utiliza build_response para construir a resposta principal
    return build_response(body=load_template('index.html').format(notes=notes))
