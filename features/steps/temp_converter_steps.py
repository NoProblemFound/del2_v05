from behave import given, when, then

@given(u'Givet {t:d}')
def step_impl(context,t):
    context.value = t

@when(u'Temperatur omvandlas från F till C')
def step_impl(context):
    context.result = (context.value - 32) / 1.8

@then(u'Den omvandlade temperaturen förväntas vara {resultat:d}')
def step_impl(context, resultat):
    assert context.result == resultat

@when(u'Temperatur omvandlas från C till F')
def step_impl(context):
    context.result = (context.value * 1.8) + 32

