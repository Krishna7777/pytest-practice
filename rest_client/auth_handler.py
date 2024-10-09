import requests


class AuthHandler:
    def __init__(self, token = None, auth_tuple = None):
        self.token = token
        self.auth_tuple = auth_tuple

    def get_headers(self):
        if self.token is not None:
            return {'Authorization': 'Bearer ' + self.token}
        elif self.auth_tuple is not None:
            return requests.auth.HTTPBasicAuth(self.auth_tuple[0], self.auth_tuple[1])
        return {}