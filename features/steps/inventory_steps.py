from behave import given, when, then
from src.stock import Stock
from src.stock_item import StockItem

@given(u'Ett tomt lager')
def step_impl(context):
    context.stock = Stock() # Skapa ett Stock objekt

@when(u'Lägger till en produkt "glas" med antal 6')
def step_impl(context):
    product = StockItem("glas",6) # Skapa ett StockItem objekt "glas"
    context.stock.add_product(product) # Lägger till glas i item[]

@then(u'Lagret ska innehålla en produkt med namnet glas och antalet skall vara 6 st')
def step_impl(context):
    assert context.stock.items[0].name == "glas"
    assert context.stock.items[0].amount == 6


@given(u'Lagret har 6 st "glas"')
def step_impl(context):
    context.stock = Stock()
    product = StockItem("glas",6)
    context.stock.add_product(product)

@when(u'Minskar antalet av "glas" med 2')
def step_impl(context):
    context.stock.decrease_product("glas", 2)

@then(u'Det finns kvar 4 "glas" kvar på lagret.')
def step_impl(context):
    assert context.stock.items[0].amount == 4