from behave import given, when, then
from src.stock import Stock
from src.stock_item import StockItem

@given(u'Ett tomt lager')
def step_impl(context):
    context.stock = Stock() # Skapa ett Stock objekt

@when(u'Lägger till en produkt "{name}" med antal {amount:d}')
def step_impl(context, name, amount):
    product = StockItem(name, amount) # Skapa ett StockItem objekt "glas"
    context.stock.add_product(product) # Lägger till glas i item[]

@then(u'Lagret ska innehålla en produkt med namnet {name} och antalet skall vara {amount:d} st')
def step_impl(context, name, amount):
    for item in context.stock.items: # Itererar genom items[]
        if item.name == name: # Hittat ett matchande namn på produkten
            assert item.amount == amount
            return # Avbryter loppen
    assert False, f"Produkten {name} finns inte i lagret" # Produkten finns inte i listan.


@given(u'Lagret har {amount:d} st {name}')
def step_impl(context,amount,name):
    context.stock = Stock()
    product = StockItem(name, amount)
    context.stock.add_product(product)

@when(u'Minskar antalet av {name} med {amount:d}')
def step_impl(context,name,amount):
    context.stock.decrease_product(name, amount)


@then(u'Det finns kvar {amount:d} {name} kvar på lagret.')
def step_impl(context, amount, name):
    for item in context.stock.items:
        if item.name == name:
            assert item.amount == amount
            return
    assert False, f"Produkten {name} finns inte i lagret"
