from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework.relations import SlugRelatedField


class CreatableSlugRelatedField(SlugRelatedField):
    """
    Custom SlugRelatedField that allows to create new objects
    """
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            obj, _ = queryset.get_or_create(**{self.slug_field: data})

            return obj
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')
