from behave import given, when, then
from src.bank import BankAccount, Bank

@given(u'Ingen konto')
def step_impl(context):
    pass

@when(u'Skapa ett nytt konto')
def step_impl(context):
    context.new_account = BankAccount()

@then(u'Saldot är 0')
def step_impl(context):
    context.new_account.balance = 0

@given(u'Ett nytt bankkonto')
def step_impl(context):
    context.new_account = BankAccount()


@when(u'Sätter in {amount:d} kronor')
def step_impl(context, amount):
    context.new_account.deposit(amount)

@then(u'Saldot ska vara {amount:d}')
def step_impl(context,amount):
    assert context.new_account.balance == amount


@given(u'Ett bankkonto med {amount:d} kronor')
def step_impl(context,amount):
    context.new_account = BankAccount()
    context.new_account.deposit(amount)

@when(u'Tar ut {amount:d} kronor')
def step_impl(context,amount):
    context.new_account.withdraw(amount)

@when(u'Applicerar ränta')
def step_impl(context):
    context.new_account.add_interest()


@given(u'Konto A har 200 kronor')
def step_impl(context):
    context.account_a = BankAccount()
    context.account_a.deposit(200)

@given(u'Konto B har 300 kronor')
def step_impl(context):
    context.account_b = BankAccount()
    context.account_b.deposit(300)

@when(u'Överför 100 kronor från konto A till konto B')
def step_impl(context):
    context.bank = Bank()
    context.bank.transfer(
        context.account_a,
        context.account_b,
        100
    )

@then(u'Saldot på konto A ska vara 100')
def step_impl(context):
    assert context.account_a.balance == 100

@then(u'Saldot på konto B ska vara 400')
def step_impl(context):
    assert context.account_b.balance == 400