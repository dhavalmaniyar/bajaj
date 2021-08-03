from typing import List
from django.db import models

class ResponseDto(models.Model):
    def __init__(self, is_success, user_id, odd, even):
        self.is_success = is_success
        self.user_id = user_id
        self.odd = odd
        self.even = even
