from ._anvil_designer import GoFrameTemplate
from anvil import *
import anvil.server
import anvil.users

#This is your startup form. It has a sidebar with navigation links and a content panel where page content will be added.
class GoFrame(GoFrameTemplate):
  def __init__(self, **properties):
    Notification("You found this page. Now, wonder what it does.",
                title="CONGRATULATIONS!!!",
                style="danger",
                timeout=None).show()
    # Set Form properties and Data Bindings.
    #self.init_components(**properties)
    #Present users with a login form with just one line of code:
    #anvil.users.login_with_form()

    #Set the Plotly plots template to match the theme of the app
    #Plot.templates.default = "rally"
    #When the app starts up, the Sales form will be added to the page
    #self.content_panel.add_component(Sales())
    #Change the color of the sales_page_link to indicate that the Sales page has been selected
    #self.sales_page_link.background = app.theme_colors['Primary Container']
    

  # def sales_page_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   #Clear the content panel and add the Sales Form
  #   self.content_panel.clear()
  #   self.content_panel.add_component(Sales())
  #   #Change the color of the sales_page_link to indicate that the Sales page has been selected
  #   self.sales_page_link.background = app.theme_colors['Primary Container']
  #   self.reports_page_link.background = "transparent"

  # def reports_page_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   #Clear the content panel and add the Reports Form
  #   self.content_panel.clear()
  #   self.content_panel.add_component(Reports())
  #   #Change the color of the sales_page_link to indicate that the Reports page has been selected
  #   self.reports_page_link.background = app.theme_colors['Primary Container']
  #   self.sales_page_link.background = "transparent"

  # #If using the Users service, uncomment this code to log out the user:
  # # def signout_link_click(self, **event_args):
  # #   """This method is called when the link is clicked"""
  # #   anvil.users.logout()
  # #   open_form('Logout')

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    arr = anvil.server.call("getStudentByLogin", self.text_box_1.text)
    self.image_1.display_mode = 'original_size'
    if arr is None:
      arr = anvil.server.call("getStudentByLogin", "thilvija")
      Notification("How bad are you at guessing that you can't even type a valid intra ID?",
                   title="Feeding you to THILA!!!",
                   style="info", timeout=None).show()
    student_image = arr['image']['versions']['small']
    if student_image is None:
      student_image = URLMedia('_/theme/whacky-too.png')
    self.image_1.source = student_image
    self.label_1.text = arr['usual_full_name']
    self.label_2.text = arr['login']
    pmon = str(anvil.server.call("monthToNumber", arr['pool_month']))
    pyer = anvil.server.call("numberToWords", arr['pool_year'])
    self.label_3.text = 'Pool: ' + pmon + ", " + pyer
    self.user_proj = arr['projects_users']
    pnames = [x['project']['name'] for x in self.user_proj]
    self.drop_down_1.include_placeholder = True
    self.drop_down_1.items = pnames
    self.drop_down_1.visible = True

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    psel = self.drop_down_1.selected_value
    pdat = [x for x in self.user_proj if x['project']['name'] == psel][0]
    pscore = anvil.server.call("numberToWords", pdat['final_mark']) if pdat['status'] == 'finished' else pdat['status']
    self.label_4.text = pscore.replace("_", " ")
    if pdat['status'] == 'finished':
      self.label_4.foreground = '#D64D47' if pdat['validated?'] else '#4caf50'
    else:
      self.label_4.foreground = '#E8C1A0'
    self.label_4.visible = True


    

 









