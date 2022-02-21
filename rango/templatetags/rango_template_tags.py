from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    # print(Category.objects.all())
    return {'categories': Category.objects.all(),
            'current_category': current_category}
