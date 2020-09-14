# TODO: add mutations
# Create your views here.
from django.views.generic import TemplateView
from core.mixins import LoginRequiredViewMixin


class IndexView(LoginRequiredViewMixin, TemplateView):
    template_name = "dictionaries/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["areas"] = user.areas
        context["subjects"] = user.subjects
        context["tags"] = user.tags
        return context
