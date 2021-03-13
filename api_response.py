class api_response:

    def __init__(self, output):
        self.output = output

    def true_output(self):
        return {"status": "success",
                "data": self.output}

    def error_output(self):
        return {"code": 500,
                "status": "error",
                "message": "internal server error",
                "data": []}

    def error_req(self):
        return {"code": 404,
                "status": "error",
                "message": "bad request"}
