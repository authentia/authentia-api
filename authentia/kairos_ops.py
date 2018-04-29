import requests,pprint,json

class Kairos:

	kairos_credentials = {
		'app_id':'c0da87a9',
		'app_key':'bd48f676be2614acae2ffcc8b2ddbc12'
	}

	def enroll_user(self,image_url,user_id):

		url = 'https://api.kairos.com/enroll'

		payload = {
			'subject_id':user_id,
			'gallery_name':'MyGallery'
			'image':image_url,
		}

		enroll_response = requests.post(url,headers=self.kairos_credentials,json=payload)
		enroll_response = json.loads(enroll_response.content.decode('utf-8'))
		pprint.pprint(enroll_response)

	def verify_user(self,image_url,user_id):

		url = 'https://api.kairos.com/verify'

		payload = {
			'image' : image_url,
			'subject_id' : user_id,
			'gallery_name' : 'MyGallery'
		}

		verify_response = requests.post(url,headers=self.kairos_credentials,json=payload)
		pprint(verify_response)
		verify_response = json.loads(verify_response.content.decode('utf-8'))
		pprint.pprint(verify_response)

	def list_gallerys(self):

		url = 'https://api.kairos.com/gallery/list_all'

		list_all_response = requests.post(url=url,headers=self.kairos_credentials)
		list_all_response = json.loads(list_all_response.content.decode('utf-8'))
		pprint.pprint(list_all_response)

if __name__ == '__main__':
	kairos = Kairos()
	kairos.list_gallerys()
