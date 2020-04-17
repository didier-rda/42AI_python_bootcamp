from book import Book
from recipe import Recipe
from datetime import datetime

feijoada = Recipe('Feijoada', 3, 120, ['Feijão', 'Porco', 'Couve', 'Laranja',
                                       'Pimenta', 'Arroz', 'Farofa'], 'lunch', 'Coloca tudo no fogo e já era.')
polpetone = Recipe('Polpetone', 4, 60, ['Carne', 'Tomate', 'Queijo', 'Farinha', 'Ovo'], 'lunch',
                   'Pegar a carne, faz uma bola, recheia com queijo, empana e frita. Depois joga molho de tomate')
fritas = Recipe('Batata Frita', 2, 30, [
                'Batata', 'Bacon', 'Cheddar'], 'starter', '')
salada = Recipe('Salada', 1, 5, [
                'Alface', 'Abacate', 'Mostarda'], 'starter', 'Mistura tudo e come')
sorvete = Recipe('Sorvete', 3, 40, ['Leite', 'Creme de Leite', 'Gema', 'Baunilha',
                                    'Açúcar'], 'dessert', 'Pega tudo joga na máquina deixar ficar gelado e come')
mousse = Recipe('Mousse', 1, 60, ['Leite condensado', 'Creme de leite',
                                  'Limão', 'Gelatina'], 'dessert', 'Mistura tudo e põe pra gelar')

book1 = Book('Livro vazio', {"starter": [], "lunch": [], "dessert": []})
book2 = Book('Livro de comidas', {"starter": [fritas, salada], "lunch": [
             feijoada, polpetone], "dessert": [sorvete, mousse]})

assert book1.get_recipe_by_name(
    'Mousse') not in book1.recipes_list['dessert'], "The element should not be on this list!"
assert book2.get_recipe_by_name(
    'Mousse') == mousse, "Could not find the recipe on the dessert list"
assert book2.get_recipe_by_name(
    'Feijoada') == feijoada, "Could not find the recipe on the lunch list"
assert book2.get_recipe_by_name(
    'Salada') == salada, "Could not find the recipe on the starter list"

assert book2.get_recipes_by_type(
    'lunch') == ['Feijoada', 'Polpetone'], "The list for lunch is not equal"
assert book2.get_recipes_by_type('starter') == [
    'Batata Frita', 'Salada'], "The list for starters is not equal"
assert book2.get_recipes_by_type('dessert') == [
    'Sorvete', 'Mousse'], "The list for desserts is not equal"

estrogonofe = Recipe('Estrogonofe', 2, 30, ['Frango', 'Ketchup', 'Mostarda', 'Creme de leite', 'Sal'], 'lunch',
                     'Uma comida muito saborosa, com um tom variando do alaranjado ao marrom terra, agrada as papilas gustativas de milhões de brasileiros.')

pudim = Recipe('pudim', 3, 90, ['ovo', 'leite condensado', 'leite'], 'dessert',
                     '')

paonachapa = Recipe('pão na chapa', 1, 5, ['pão francês', 'manteiga'], 'starter',
                     'coloca o pão na chapa com maiteiga e deixa até ficar dourado.')

print(
    f"Saída do objeto: {book2.add_recipe(estrogonofe).last_update}\nSaída datetime: {datetime.today()}")

# test recipe_type lunck
assert book2.recipes_list[estrogonofe.recipe_type][-1].name ==  estrogonofe.name

book2.add_recipe(pudim)
# test recipe_type dessert
assert book2.recipes_list[pudim.recipe_type][-1].name ==  pudim.name


book2.add_recipe(paonachapa)
# test recipe_type starter
assert book2.recipes_list[paonachapa.recipe_type][-1].name ==  paonachapa.name
