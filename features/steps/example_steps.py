from behave   import given, when, then
from hamcrest import assert_that, equal_to
from calculator import Calculator

@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()

@when('I multiply "{x}" and "{y}"')
def step_impl(context, x, y):
    context.calculator.mul(int(x), int(y))

@then('the calculator returns "{expected}"')
def step_impl(context, expected):
    assert_that(context.calculator.result, equal_to(int(expected)))