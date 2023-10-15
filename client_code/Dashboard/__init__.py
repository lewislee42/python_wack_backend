from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.users
from .Coalition import Coalition

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    val = anvil.server.call('getStudentByLogin', 'lewlee')
    print(val)
    # self.repeating_panel_1.item_template = Coalition
    # self.repeating_panel_1.items = anvil.server.call('getStudentObject')

    # Any code you write here will run before the form opens.
