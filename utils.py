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
    # Ler o conteúdo do arquivo JSON
    with open(f'data/{file_name}', 'r', encoding='utf-8') as file:
        text = file.read()
        data = json.loads(text)

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
    response = f'HTTP/1.1 {code} {reason}\n'
    
    if headers:
        response += f'{headers}\n'

    response += '\n'
    response += body

    return response.encode()

def add_note(params):
    with open('data/notes.json', 'r') as file:
        data = json.load(file)

    # Adiciona a nova anotação à lista
    data.append(params)

    with open('data/notes.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)