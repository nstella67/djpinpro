from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownerthip_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    # 성공 후 hello_world가 아니라 detail로 넘겨주고 싶은데, pk 넘길 수 없음. get_success_url 메서드 추가해준다
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 임시 데이터 저장
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownerthip_required, 'get')
@method_decorator(profile_ownerthip_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})