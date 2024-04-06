def get_display_items(style_element):
    display_items = []

    for item in style_element.find('display'):
        display_items.append({
            'metric': int(item.find('metric').text),
            'posx': int(item.find('posx').text),
            'posy': int(item.find('posy').text),
            'width': int(item.find('width').text),
            'height': int(item.find('height').text),
            'theme': int(item.find('theme').text),
            'color': int(item.find('color').text)
        })
    
    return display_items