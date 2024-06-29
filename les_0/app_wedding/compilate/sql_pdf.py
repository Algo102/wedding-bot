import imgkit


def create_jpg_html(result_data: dict, user_id):
    result_tuple = {
        'season': {
            'summer': 'Летом',
            'autumn': 'Осенью',
            'winter': 'Зимой',
            'spring': 'Весной'
        }.get(result_data['season'], None),
        'amount': {
            'two': 'Только вдвоем',
            'folks': 'Только близкие',
            'upto100': 'До 100',
            'morethan100': 'Более 100'
        }.get(result_data['amount'], None),
        'place': {
            'restaurant': 'Банкетный зал',
            'unique': 'Уникальная локация',
            'garden': 'Вечеринка в саду',
            'sea': 'Море'
        }.get(result_data['place'], None),
        'style': {
            'romantic': 'Романтическая свадьба',
            'vintage': 'Винтажная свадьба',
            'eccentric': 'Эксцентричная свадьба',
            'modern': 'Современная свадьба',
            'classic': 'Классическая свадьба',
            'travel': 'Свадьба в стиле travel'
        }.get(result_data['style'], None),
        'colors': {
            'emeraldGreen': 'Изумрудно-зеленая',
            'vanillaCream': 'Ванильная',
            'macchiato': 'Капучино',
            'dirtyRose': 'Пыльная роза',
            'wine': 'Винная',
            'quartzPink': 'Розовый кварц'
        }.get(result_data['colors'], None),
        'fashion': {
            'trapezoidal': 'Трапециевидный силуэт',
            'naiad': 'Русалка',
            'sheath': 'Футляр',
            'ballGown': 'Бальное платье',
            'overalls': 'Комбинезон',
            'retro': 'Ретро'
        }.get(result_data['fashion'], None),
        'costume': {
            'classicCostume': 'Классика',
            'tuxedo': 'Смокинг',
            'casual': 'Кэжуал',
            'modernCostume': 'Современный костюм'
        }.get(result_data['costume'], None)
    }

    photo_season_path = {
        'summer': 'summer',
        'spring': 'spring',
        'autumn': 'autumn',
        'winter': 'winter'
    }.get(result_data['season'], 'winter')

    photo_amount_path = {
        'two': 'two',
        'folks': 'folks',
        'upto100': 'upto100',
        'morethan100': 'morethan100'
    }.get(result_data['amount'], None)

    photo_place_path = {
        'restaurant': 'restaurant',
        'unique': 'unique',
        'garden': 'garden',
        'sea': 'sea'
    }.get(result_data['place'], None)

    photo_style_path = {
        'romantic': 'romantic',
        'vintage': 'vintage',
        'eccentric': 'eccentric',
        'modern': 'modern',
        'classic': 'classic',
        'travel': 'travel'
    }.get(result_data['style'], None)

    photo_colors_path = {
        'emeraldGreen': 'emeraldGreen',
        'vanillaCream': 'vanillaCream',
        'macchiato': 'macchiato',
        'dirtyRose': 'dirtyRose',
        'wine': 'wine',
        'quartzPink': 'quartzPink'
    }.get(result_data['colors'], None)

    photo_fashion_path = {
        'trapezoidal': 'trapezoidal',
        'naiad': 'naiad',
        'sheath': 'sheath',
        'ballGown': 'ballGown',
        'overalls': 'overalls',
        'retro': 'retro'
    }.get(result_data['fashion'], None)

    photo_costume_path = {
        'classicCostume': 'classicCostume',
        'tuxedo': 'tuxedo',
        'casual': 'casual',
        'modernCostume': 'modernCostume'
    }.get(result_data['costume'], None)

    with open('./app_wedding/compilate/index.html',
              'r', encoding='utf-8') as file:
        html_content = file.read()

    formatted_html = html_content.format(
        result_tuple['season'],
        photo_season_path,
        photo_season_path,
        photo_season_path,
        result_tuple['amount'],
        photo_amount_path,
        photo_amount_path,
        result_tuple['place'],
        photo_place_path,
        photo_place_path,
        photo_place_path,
        photo_place_path,
        result_tuple['style'],
        photo_style_path,
        photo_style_path,
        result_tuple['colors'],
        photo_colors_path,
        result_tuple['fashion'],
        photo_fashion_path,
        photo_fashion_path,
        photo_fashion_path,
        result_tuple['costume'],
        photo_costume_path,
        photo_costume_path,
        photo_costume_path
    )

    with open(f'./app_wedding/compilate/{user_id}.html',
              'w', encoding='utf-8') as file:
        file.write(formatted_html)

    path_wkhtmltoimage = r"C:\Program Files\
    wkhtmltopdf\bin\wkhtmltoimage.exe"

    config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)

    html_file_path = f"./app_wedding/compilate/{user_id}.html"
    output_image_path = f"./app_wedding/compilate/{user_id}.jpg"
    options = {
        'quiet': '',
        'enable-local-file-access': '',
    }
    imgkit.from_file(html_file_path,
                     output_image_path, options=options, config=config)
