# encode_resources.py
import base64
import os

def encode_file(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return None

# Кодируем файлы
files = ['icon.ico', 'Z.jpg', 'fon.jpg']
resources = {}

for f in files:
    data = encode_file(f)
    if data:
        resources[f.upper().replace('.', '_')] = data
        print(f"✅ {f} закодирован")
    else:
        print(f"❌ {f} не найден!")

# СОЗДАЁМ ФАЙЛ resources.py АВТОМАТИЧЕСКИ
with open('resources.py', 'w', encoding='utf-8') as f:
    f.write('# resources.py - автоматически сгенерирован\n')
    f.write('import base64\n')
    f.write('import os\n')
    f.write('import tempfile\n\n')
    
    for name, data in resources.items():
        f.write(f'{name} = """{data}"""\n')
    
    f.write('''

def get_temp_file(b64_data, filename):
    """Декодирует base64 и сохраняет во временный файл"""
    if not b64_data:
        return None
    
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"switchmenu_{filename}")
    
    if os.path.exists(temp_path):
        return temp_path
    
    try:
        data = base64.b64decode(b64_data)
        with open(temp_path, 'wb') as out:
            out.write(data)
        return temp_path
    except Exception as e:
        print(f"Ошибка декодирования {filename}: {e}")
        return None

def get_icon_path():
    return get_temp_file(ICON_ICO, 'icon.ico')

def get_photo_path():
    return get_temp_file(Z_JPG, 'Z.jpg')

def get_background_path():
    return get_temp_file(FON_JPG, 'fon.jpg')
''')

print("\n✅ Файл resources.py создан!")