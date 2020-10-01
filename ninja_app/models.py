from django.db import models

class UserManager(models.Manager):

    def validate(self, postData):
        errors={}
        
        if len(postData['first_name'])< 1:
            errors['first_name']="Please type in your name."

        #if len(postData['user_input'])< 1:
            #errors['user_input']="Please type in the indicated word in the prompt."

        #NEED ERROR STATEMENT FOR ANTYHING OTHER THAN INDICATED WORD IN PROMPT
        #USE IF/ELSE BASED ON PROMPT INDCIATED WORD
        
           
        return errors

class User(models.Model):

    first_name = models.CharField(max_length = 45)
    #user_input = models.CharField(max_length = 45)

    objects = UserManager()

