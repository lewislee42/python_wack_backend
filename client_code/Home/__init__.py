from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.users
from .Dashboard import Dashboard
from .GoFrame import GoFrame

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel_1.add_component(Dashboard())
    self.view = True

    # Any code you write here will run before the form opens.

  def link_go_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_1.clear()
    if self.view:
      self.column_panel_1.add_component(GoFrame())
      self.view = False
    else:
      self.column_panel_1.add_component(Dashboard())
      self.view = True

