import json

def convert_layer_for_json(layer : dict) -> dict:
    layer_for_json = {}
    for pos, tile_info in layer.items():
        pos_for_json = f"{pos[0]};{pos[1]}"
        layer_for_json[pos_for_json] = tile_info
    return layer_for_json

def save_level(layers: dict, level : int=0):
    data = {"layers" : {}}
    for i, layer in enumerate(layers, 1):
        data['layers'][f'layer_{i}'] = convert_layer_for_json(layer)
    try:
        with open(f"levels/level{level}.json", 'w', encoding='utf-8') as file:
            json.dump(data, file,ensure_ascii=False, indent=4)
        print('Succeful save level')
    except Exception as e:
        print('Eror save:', e)

def convert_layer_to_normal_style(layer : dict) -> dict:
    normal_layer = {}
    for pos, tile_info in layer.items():
        normal_pos = tuple(map(int, pos.split(';')))
        normal_layer[normal_pos] = tile_info
    return normal_layer

def load_level(level : int):
    if level == -1:
        return []
    try:
        with open(f"levels/level{level}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
    except:
        print('Ошибка данный уровень не существует')
        inp = input('Введите число уровня, если новый уровень введите -1 ')
        return load_level(int(inp))
    layers = []
    for i in range(len(data['layers'])):
        layers.append(convert_layer_to_normal_style(data['layers'][f'layer_{i + 1}']))
    return layers