from registration.backends.simple.views import RegistrationView
from .forms import UserProfileRegistrationForm
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class MyRegistrationView(RegistrationView):

    #form_class = UserProfileRegistrationForm

    def register(self, request, form):
        new_user = super(MyRegistrationView, self).register(request, form)
        
        '''UserModel = get_user_model
        new_user_instance = (UserModel().objects.create_user(**form.cleaned_data))
        '''
        #user_profile = get_user_model
        #user_profile.user = new_user
        #user_profile.field = form_class.cleaned_data['field']
        stuff=Group.objects.get(name="stuff")
        new_user.groups.add(stuff)
        new_user.save()
        return new_user

    def get_success_url(self,request, user):
        return '/'


#http://stackoverflow.com/questions/29620940/django-registration-redux-add-extra-field?rq=1