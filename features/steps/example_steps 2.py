from behave   import given, when, then

@given('we have google installed')
def step_impl(context):
    pass

@when('we visit google')
def step(context):
   context.browser.get('http://www.google.com')

@then('it should have a title "Google"')
def step(context):
   assert context.browser.title == "Google"