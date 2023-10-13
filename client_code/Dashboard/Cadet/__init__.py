from ._anvil_designer import CadetTemplate
from anvil import *
import anvil.server
import anvil.users

class Cadet(CadetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = self.item['displayname']
    self.label_2.text = self.item['login']
    student_image = self.item['image']['versions']['small']
    if student_image is None:
      student_image = URLMedia('_/theme/whacky-too.png')
    self.image_1.source = student_image
    self.image_1.display_mode = 'original_size'

    # Any code you write here will run before the form opens.
