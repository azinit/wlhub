from django.contrib.auth.decorators import login_required
from django.urls import reverse as reverse
from django.utils.decorators import classonlymethod
from django.utils.html import format_html


class ModelStrMixin(object):
    def __str__(self):
        return self.name or "..."


# based on https://gist.github.com/Vigrond/ac3c468377ce6d3e53f9b7059fd42569
class ListLinksMixin(object):
    """
    Support for list_links attribute.  Items in list_links must also be in list_display

    Usage to make 'fieldTwo' a link:
    list_display = ('fieldOne', 'fieldTwo',)
    list_links = ('fieldTwo',)

    """
    list_links = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.list_links:
            for field in self.list_links:
                if field in self.list_display:
                    func_name = field + '_link'
                    setattr(self, func_name, self._generate_link_func(field))
                    self.list_display = [func_name if item == field else item for item in self.list_display]

    def _generate_link_func(self, field):
        def _func(item):
            instance = getattr(item, field)
            if not instance:
                return None
            url = reverse(
                f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change', args=[instance.pk])
            return format_html(f'<a href="{url}">{instance}</a>')

        _func.short_description = field
        _func.admin_order_field = field

        return _func


class LoginRequiredViewMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)
