from werkzeug.exceptions import HTTPException

class ValueError_http(HTTPException):
    code = 400
    message = 'No message specified'
class AccessError(HTTPException):
    code = 404
    message = 'No message specified'
