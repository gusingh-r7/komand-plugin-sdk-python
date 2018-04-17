import komand
from .schema import ReturnBadJsonInput, ReturnBadJsonOutput
# Custom imports below


class ReturnBadJson(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='return_bad_json',
                description='This action will return JSON which doesn't match the spec',
                input=ReturnBadJsonInput(),
                output=ReturnBadJsonOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}

    def test(self):
        # TODO: Implement test function
        return {}
