from django.http import HttpResponse
from django.shortcuts import render
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def hello_view(request):
    return HttpResponse('hello')


def dish_view(request):
    dish = request.path[1:-1]
    servings = (request.GET.get('servings', 1))
    try:
        servings = int(servings)
    except ValueError:
        servings = 0
    if servings <= 0:
        data_context = {}
        return render(request, 'calculator/index.html', data_context)
    else:
        data_context = copy.deepcopy(DATA)
        for key, elem in DATA[dish].items():
            data_context[dish][key] *= servings
        context = {'recipe': data_context[dish], 'name': dish}
        return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
