from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from django.contrib.auth import get_user
# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'Abror',
                'username':'abror01',
                'email':'abrorkushshiyev@gmail.com',
                'password1':'qaswedfrtg',
                'password2':'qaswedfrtg',
            }
        )
        user=CustomUser.objects.get(username='abror01')
        self.assertEqual(user.first_name, 'Abror')
        self.assertEqual(user.email, 'abrorkushshiyev@gmail.com')
        self.assertTrue(user.check_password('qaswedfrtg'))
    
        second_response = self.client.get("/users/profile/abror01") 
        self.assertEqual(second_response.status_code, 200)   
        
        #login
        self.client.login(username='abror01', password='qaswedfrtg')
        
        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username':'abror2',
                'first_name':'Abror1',
                'last_name':'Kushshiyev',
                'email':'abrorkushshiyav@gmail.com',
                'phone_number':'+998931410111',
                'tg_username':'username',
            }
        )
        user = get_user(self.client)  
        print(user.is_authenticated)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '+998931410111')
        self.assertEqual(user.first_name, 'abror2')
        self.assertNotEqual(user.first_name, 'Abror')
        
        