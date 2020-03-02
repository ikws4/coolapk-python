class User:

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.uid = kwargs['uid']
        self.token = kwargs['token']

    def __str__(self):
        return self.username
