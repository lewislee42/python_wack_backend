from ._anvil_designer import CoalitionTemplate
from anvil import *
import anvil.server
import anvil.users
from .Cadet import Cadet

class Coalition(CoalitionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = 'Coalition'
    self.repeating_panel_1.item_template = Cadet
    self.repeating_panel_1.items = items[set]

    # Any code you write here will run before the form opens.
