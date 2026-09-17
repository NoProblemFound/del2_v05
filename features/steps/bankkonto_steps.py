from behave import given, when, then
from src.bank import BankAccount

@given(u'Ingen konto')
def step_impl(context):
    pass

@when(u'Skapa ett nytt konto')
def step_impl(context):
    context.new_account = BankAccount()

@then(u'Saldot är 0')
def step_impl(context):
    context.new_account.balance = 0



