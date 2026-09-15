from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError

@given(u'Givet 32 F')
def step_impl(context):
    context.value = 32

@when(u'Temperatur omvandlas')
def step_impl(context):
    context.result = (context.value - 32) / 1.8

@then(u'Den omvandlade temperaturen förväntas vara 0')
def step_impl(context):
    assert context.result == 0

