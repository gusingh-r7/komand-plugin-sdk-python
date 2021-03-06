# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class ReturnBadJsonInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The Name",
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReturnBadJsonOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "The greeting",
      "order": 1
    }
  },
  "required": [
    "message"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
