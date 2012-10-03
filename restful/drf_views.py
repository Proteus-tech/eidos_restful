# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from djangorestframework.views import ModelView
from djangorestframework.response import ErrorResponse
from djangorestframework import status

from serene.mixins import CreateModelMixin

class CreateModelWithFormView(CreateModelMixin, ModelView):
    """
    An extension to the CreateModelMixin that adds support to a GET request which will return the form
    that can be used to create the instance
    """

    action_url = None

    def get(self, request, *args, **kwargs):
        if not hasattr(self.resource, 'post_form'):
            raise ErrorResponse(status.HTTP_500_INTERNAL_SERVER_ERROR,
                u'The server did not implement this view correct.')

        context = RequestContext(request)
        context.update({
            'form': self.resource.post_form,
            'action': request.build_absolute_uri(self.action_url),
            'method': 'POST',
            'id': self.get_name() + "_form",
            'submit_value': 'Submit',
            })

        return render_to_response('restful/form.html', context)