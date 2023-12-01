from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"

# "127.0.0.1:8000/account/hello_wourld"
# "accountapp:hello_world"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
