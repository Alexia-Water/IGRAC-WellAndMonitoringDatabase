from django.urls import reverse
from gwml2.forms import WellQualityMeasurementForm
from gwml2.models.well import WellQualityMeasurement
from gwml2.views.form_group.form_group import FormGroupGet, FormGroupCreate


class QualityMeasurementGetForms(FormGroupGet):
    """ Collection form for general information section """

    def get(self):
        """ return forms in dictionary
        :return: dictionary of forms
        :rtype: dict
        """
        form = WellQualityMeasurementForm()
        if self.well.id:
            form.url_chart = reverse(
                'well-measurement-chart',
                kwargs={
                    'id': self.well.id, 'model': 'WellQualityMeasurement'})
        return {
            'quality_measurement': form,  # manytomany form
        }


class QualityMeasurementCreateForm(FormGroupCreate):
    """ Collection form for general information section """
    measurements = []

    def create(self):
        """ create form from data
        """
        self.measurements = []
        if self.data.get('quality_measurement', None):
            for measurement in self.data['quality_measurement']:
                if not measurement['time']:
                    return
                obj = WellQualityMeasurement.objects.get(
                    id=measurement['id']) if measurement['id'] else WellQualityMeasurement()

                self.measurements.append(
                    self._make_form(
                        obj, WellQualityMeasurementForm, measurement
                    )
                )

    def save(self):
        """ save all available data """
        for measurement in self.measurements:
            measurement.instance.well = self.well
            if not measurement.instance.created_by:
                measurement.instance.created_by = self.well.created_by
            measurement.instance.last_edited_by = self.well.last_edited_by
            measurement.instance.last_edited_at = self.well.last_edited_at
            measurement.save()
