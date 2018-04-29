from django.contrib.gis.db import models
from django.core import signing
from django.conf import settings

from users.models import AuthentiaAbstractBaseUser, TokenUserModel
from base.models import BaseModel
from helpers import upload_to_kwargs, upload_to_generic

import requests, pprint, json, os


class AuthentiaUser(AuthentiaAbstractBaseUser):
    kairos_credentials = {
        'app_id':os.getenv('KAIRO_APP_ID'),
        'app_key':os.getenv('KAIRO_APP_KEY'),
    }

    token = models.OneToOneField(TokenUserModel, related_name="user_token", null=True, blank=True, on_delete=models.CASCADE, max_length=250)

    def generate_sign(self):
        return signing.dumps(self.pk)

    def __str__(self):
        return "{} {} {}".format(self.pk, self.full_name, self.token)

    def enroll_user(self, image_url):

        url = 'https://api.kairos.com/enroll'

        payload = {
            'subject_id':"{}".format(self.pk),
            'image':image_url,
            'gallery_name':'auhtenia-users'
        }
        print(payload)
        enroll_response = requests.post(url,headers=self.kairos_credentials,json=payload)
        print('>>>>>>', enroll_response)
        enroll_response = json.loads(enroll_response.content.decode('utf-8'))
        print('>>>>>>', enroll_response)
        pprint.pprint(enroll_response)
        return enroll_response

    def verify_user(self, image_url):
        print('entrooo')
        url = 'https://api.kairos.com/verify'

        payload = {
            'subject_id' : "{}".format(self.pk),
            'image' : image_url,
            'gallery_name' : 'auhtenia-users'
        }
        print('deded>>>')
        verify_response = requests.post(url, headers=self.kairos_credentials, json=payload)
        print(verify_response.json())
        verify_response = json.loads(verify_response.content.decode('utf-8'))
        pprint.pprint(verify_response)
        return verify_response


class PhotoEnroll(BaseModel):
    user = models.ForeignKey(AuthentiaUser, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=upload_to_kwargs(upload_to_generic, subfolder="photos-enrolled"))

    def __str__(self):
        return self.user.first_name
