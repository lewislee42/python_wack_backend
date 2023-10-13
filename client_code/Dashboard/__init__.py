from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.users
from Cadet import Cadet

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('returnStudentJson')
    self.repeating_panel_1.item_template = Cadet
    

    # Any code you write here will run before the form opens.
