from ._anvil_designer import CadetTemplate
from anvil import *
import anvil.server
import anvil.users

class Cadet(CadetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = self.item['login'] + ':' + self.item['displayname']
    self.image_1.source = self.item['image']['versions']['small']

    # Any code you write here will run before the form opens.
