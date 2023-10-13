from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.users
from Cadet import Cadet

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.item_template = Cadet
    self.repeating_panel_1.items = [
      {'id': 163553, 'email': 'mamir-ra@student.42kl.edu.my', 'login': 'mamir-ra', 'first_name': 'Mohammad ridhwan', 'last_name': 'Amir rashidi', 'usual_full_name': 'Mohammad Ridhwan Amir Rashidi', 'usual_first_name': None, 'url': 'https://api.intra.42.fr/v2/users/mamir-ra', 'phone': 'hidden', 'displayname': 'Mohammad Ridhwan Amir Rashidi', 'kind': 'student', 'image': {'link': 'https://cdn.intra.42.fr/users/cfdce4c2634407e0bcab61498d0c533d/mamir-ra.jpg', 'versions': {'large': 'https://cdn.intra.42.fr/users/67e1f034b026daf1ebf8d0c47f41e75a/large_mamir-ra.jpg', 'medium': 'https://cdn.intra.42.fr/users/caee63460326394caab36664a9ce0142/medium_mamir-ra.jpg', 'small': 'https://cdn.intra.42.fr/users/e6b713f7fad6539ca412bc407dc0136d/small_mamir-ra.jpg', 'micro': 'https://cdn.intra.42.fr/users/d5810e2e7ad61103905b37c4e50b2c46/micro_mamir-ra.jpg'}}, 'staff?': False, 'correction_point': 10, 'pool_month': 'september', 'pool_year': '2023', 'location': None, 'wallet': 0, 'anonymize_date': '2026-09-11T00:00:00.000+08:00', 'data_erasure_date': '2026-09-11T00:00:00.000+08:00', 'created_at': '2023-08-23T15:19:31.875Z', 'updated_at': '2023-09-28T08:24:23.445Z', 'alumnized_at': None, 'alumni?': False, 'active?': False},
      {'id': 166377, 'email': 'aberbar@student.42kl.edu.my', 'login': 'aberbar', 'first_name': 'Alexandre', 'last_name': 'Berbar', 'usual_full_name': 'Alexandre Berbar', 'usual_first_name': None, 'url': 'https://api.intra.42.fr/v2/users/aberbar', 'phone': 'hidden', 'displayname': 'Alexandre Berbar', 'kind': 'student', 'image': {'link': 'https://cdn.intra.42.fr/users/92f5b23eba328ddfe2bef4a35375dbbc/aberbar.jpg', 'versions': {'large': 'https://cdn.intra.42.fr/users/a3be5a2bb0b11bd0ad72a5f6abf67b90/large_aberbar.jpg', 'medium': 'https://cdn.intra.42.fr/users/fabe0dc65aa040d48c79247ceabbcf0f/medium_aberbar.jpg', 'small': 'https://cdn.intra.42.fr/users/b5b940db55cc467d737ddff60da71cee/small_aberbar.jpg', 'micro': 'https://cdn.intra.42.fr/users/299e5943dde3f358725edbf3ead8ddc7/micro_aberbar.jpg'}}, 'staff?': False, 'correction_point': 7, 'pool_month': 'september', 'pool_year': '2023', 'location': None, 'wallet': 0, 'anonymize_date': '2026-10-05T00:00:00.000+08:00', 'data_erasure_date': '2026-10-05T00:00:00.000+08:00', 'created_at': '2023-09-09T11:28:31.669Z', 'updated_at': '2023-10-06T02:39:02.321Z', 'alumnized_at': None, 'alumni?': False, 'active?': False}
    ]
    self.repeating_panel_1.items = anvil.server.call('getStudentObject')
    

    # Any code you write here will run before the form opens.
