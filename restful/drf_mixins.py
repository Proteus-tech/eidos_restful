# -*- coding: utf-8 -*-
from djangorestframework.response import ErrorResponse
from djangorestframework import status

from serene.views import InstanceModelView

from softdelete.models import SoftDeleteObject

class InstanceModelWithSoftDeleteView(InstanceModelView):
    def method_process(self, method, request, *args, **kwargs):
        try:
            result = getattr(super(InstanceModelWithSoftDeleteView, self), method)(request, *args, **kwargs)
        except ErrorResponse, err:
            model_class = self.resource.model
            if (err.response.status == status.HTTP_404_NOT_FOUND) and\
               (issubclass(model_class, SoftDeleteObject)):
                try:
                    # try finding from all_with_deleted
                    instance = model_class.objects.all_with_deleted().get(*args, **kwargs)
                    if instance.deleted_at:
                        # this has been soft deleted
                        raise ErrorResponse(status.HTTP_410_GONE)
                except model_class.DoesNotExist:
                    # it really does not exist, let the raise err code below does its job
                    pass

            raise err

        return result

    def get(self, request, *args, **kwargs):
        return self.method_process('get', request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.method_process('put', request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.method_process('delete', request, *args, **kwargs)

