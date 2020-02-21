# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Triggers a greeting every interval"


class Input:
    
    INTERVAL = "interval"
    

class Output:
    
    GREETING = "greeting"
    

class EmitGreetingInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "How frequently (in seconds) to trigger a greeting",
      "default": 15,
      "order": 1
    }
  },
  "required": [
    "interval"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EmitGreetingOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "greeting": {
      "$ref": "#/definitions/person",
      "title": "Greeting",
      "order": 1
    }
  },
  "required": [
    "greeting"
  ],
  "definitions": {
    "person": {
      "type": "object",
      "title": "person",
      "properties": {
        "first_name": {
          "type": "string",
          "title": "First Name",
          "order": 1
        },
        "last_name": {
          "type": "string",
          "title": "Last Name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)