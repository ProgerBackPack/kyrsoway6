from django.forms import ModelForm

from blog.models import Blog


class BlogCreateForm(ModelForm):
    """
    Форма для создания блога.
    """
    class Meta:
        model = Blog
        exclude = ('views_count',)