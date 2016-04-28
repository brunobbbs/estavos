from copy import deepcopy

from django import forms
from django.contrib import admin
from mezzanine.pages import admin as pages_admin
from .models import CategoryLink

CATEGORY_LINK_FIELDSETS = deepcopy(pages_admin.PageAdmin.fieldsets)
CATEGORY_LINK_FIELDSETS[0][1]['fields'].insert(1, 'blog_category')


class CategoryLinkForm(forms.ModelForm):
    class Meta:
        model = CategoryLink
        fields = ('blog_category', )


class CategoryLinkAdmin(pages_admin.PageAdmin):
    form = CategoryLinkForm
    fieldsets = CATEGORY_LINK_FIELDSETS

admin.site.register(CategoryLink, CategoryLinkAdmin)
