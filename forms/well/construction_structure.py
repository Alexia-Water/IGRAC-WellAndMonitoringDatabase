from django import forms
from django.forms.models import model_to_dict
from gwml2.forms.widgets.quantity import QuantityInput
from gwml2.models.construction import ConstructionStructure


class ConstructionStructureForm(forms.ModelForm):
    """
    Form for ConstructionStructure.
    """
    id_ = forms.CharField(required=False)

    class Meta:
        model = ConstructionStructure
        fields = ('id_', 'type', 'reference_elevation', 'top_depth', 'bottom_depth',
                  'diameter', 'material', 'description')
        widgets = {
            'top_depth': QuantityInput(unit_group='length'),
            'bottom_depth': QuantityInput(unit_group='length'),
            'diameter': QuantityInput(unit_group='length'),
        }

    @staticmethod
    def make_from_data(instance, data, files):
        """ Create form from request data
        :param instance: Casing object
        :type instance: Casing

        :param data: dictionary of data
        :type data: dict

        :param files: dictionary of files that uploaded
        :type files: dict

        :return: Form
        :rtype: CasingForm
        """
        return ConstructionStructureForm(data, files, instance=instance)

    @staticmethod
    def make_from_instance(instance):
        """ Create form from instance
        :param instance: Casing object
        :type instance: Casing

        :return: Form
        :rtype: CasingForm
        """
        data = model_to_dict(instance)
        data['id_'] = instance.id
        return ConstructionStructureForm(initial=data, instance=instance)