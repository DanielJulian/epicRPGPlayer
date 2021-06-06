import re
import json

regex_signs = '<[^>]+>'

class InventoryCache:
    
   items = dict()
   consumables = dict()

   def update_inventory(self, field):
      json = self.get_json(field['value'])
      if (field['name'] == 'Items'):
         self.items = json
         print("Items inventory updated: " + str(json))
      elif (field['name'] == 'Consumables'):
         self.consumables = json
         print("Consumables inventory updated: " + str(json))
         

   def get_json(self, string):
      string = string.replace('\n', ',').replace('**', '"')
      string = re.sub(regex_signs, '', string)
      string = "{" + string + "}"
      return json.loads(string)

   def get_items(self):
      return self.items

   def get_consumables(self):
      return self.consumables
