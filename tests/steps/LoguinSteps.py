from pytest_bdd import scenario, given, when, then

@scenario('Login.feature', 'Valid Message')
def test_publish():
    pass

@given("Open Browser Chrome")
def o_browser(self):
    self.open_browser()

@when("Validar mensaje")
def v_message(self):
    self.valid_message()

@then("Salir del Browser")
def c_browser(self):
  assert self.close_browser() == 'No results were found for your search "Hola"'

