from pprint import pprint

with open('recipes.txt', encoding='utf-8') as cook_file:
    cook_book = {}
    for line in cook_file:
        dish_name = line.strip()
        ingredients_counter = int(cook_file.readline())
        ingredients = []
        for i in range(ingredients_counter):
            ingredient = cook_file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_file.readline()
        cook_book[dish_name]=ingredients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list.keys():
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    shop_list[ingredient['ingredient_name']]=({
                                                                'measure': ingredient['measure'],
                                                                'quantity': int(ingredient['quantity']) * person_count
                                                               })
    return shop_list

pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос'], 3))