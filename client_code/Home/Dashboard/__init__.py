from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.users
from Cadet import Cadet

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    Notification("Good luck figuring us out.",
                 title="Welcome to WH4CKY-2OO!",
                 style="success",
                 timeout=60).show()
    self.repeating_panel_1.item_template = Cadet
    self.repeating_panel_2.item_template = Cadet
    self.repeating_panel_3.item_template = Cadet
    self.repeating_panel_4.item_template = Cadet
    co_dat = anvil.server.call('getStudentObject')
    self.repeating_panel_1.items = co_dat[0]
    self.repeating_panel_2.items = co_dat[1]
    self.repeating_panel_3.items = co_dat[2]
    self.repeating_panel_4.items = co_dat[3]
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_4.visible = False if self.repeating_panel_4.visible else True

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_2.visible = False if self.repeating_panel_2.visible else True

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.visible = False if self.repeating_panel_1.visible else True

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_3.visible = False if self.repeating_panel_3.visible else True
