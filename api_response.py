class api_response:

    def __init__(self, output):
        self.output = output

    def true_output(self):
        return {"status": "success",
                "data": self.output}

    def error_req(self):
        return {"code": 500,
                "status": "error",
                "message": "internal server error"}

    def error_output(self):
        return {"code": 400,
                "status": "error",
                "message": "bad request",
                "data": []}
