from urllib.parse import unquote_plus
from utils import load_data, load_template, add_note_to_file

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '') 
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[chave] = unquote_plus(valor)

        # Adiciona a nova anotação ao arquivo notes.json
        new_note = {'titulo': params.get('titulo', ''), 'detalhes': params.get('detalhes', '')}
        add_note_to_file(new_note)

        note_template = load_template('components/note.html')
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)

        return load_template('index.html').format(notes=notes).encode()

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes).encode()