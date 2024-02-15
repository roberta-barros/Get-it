from pathlib import Path
import json

def extract_route(request):
    # Encontrar a posição do primeiro espaço em branco após o primeiro caractere '/'
    first_space_index = request.find(' ') + 2
    
    # Encontrar a posição do segundo espaço em branco
    second_space_index = request.find(' ', first_space_index)
    
    # Extrair a rota entre o primeiro e o segundo espaço em branco
    route = request[first_space_index:second_space_index]
    
    return route

def read_file(file_path):
    # Verificar se o caminho existe
    if not Path(file_path).exists():
        raise FileNotFoundError(f'O arquivo {file_path} não foi encontrado.')

    # Ler o conteúdo do arquivo em modo binário
    with open(file_path, 'rb') as file:
        content = file.read()

    return content

def load_data(file_name):
    # Construir o caminho completo para o arquivo dentro da pasta 'data'
    file_path = Path('data') / file_name

    # Verificar se o arquivo existe
    if not file_path.exists():
        raise FileNotFoundError(f'O arquivo {file_name} não foi encontrado em data/.')

    # Ler o conteúdo do arquivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def load_template(template_name):
    # Construir o caminho completo para o arquivo dentro da pasta 'templates'
    template_path = Path('templates') / template_name

    # Verificar se o arquivo existe
    if not template_path.exists():
        raise FileNotFoundError(f'O arquivo de template {template_name} não foi encontrado em templates/.')

    # Ler o conteúdo do arquivo de template
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()

    return template_content

def build_response(body='', code=200, reason='OK', headers=''):
    # Constrói a resposta HTTP formatada
    response = f'HTTP/1.1 {code} {reason}\n'
    response += f'Content-Length: {len(body)}\n'
    
    if headers:
        response += f'{headers}\n'

    response += '\n'
    response += body

    return response.encode()

def add_note_to_file(new_note):
    file_path = Path('data') / 'notes.json'
    notes = load_data(file_path)

    notes.append(new_note)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)