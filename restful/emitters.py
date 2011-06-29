#!/usr/bin/env python

from django.template import loader
from django.template.context import RequestContext
from django import forms
from piston.emitters import Emitter
from piston.utils import Mimer

class HTMLEmitter(Emitter):
    """
    Emitter that returns HTML.
    
    As this format.
    
    .. code-block:: html

        <form action='' method="put">
            <p><label for="id_[field name]">[field name]:</label> <input type="text" name="[field name]" value="[field value]" id="id_[field name]" /></p>
            ...
            ...
            
            <p>
            <input type="submit" value="submit" />
            <input type="reset" value="reset" />
            </p>
        </form>

    
    """
    
    @staticmethod
    def create_simple_form(data):
        """
        For simple we assume data is dict.
        """
        fields = {}
        
        for key in data.keys():
            fields[key] = forms.CharField()
        
        form_type = type('SimpleForm', (forms.Form,), fields)
        
        return form_type
    
    def render(self, request):
        """
        Render HTML for request.
        """
        
        data = self.construct()
        context = RequestContext(request)
        if data:
            if hasattr(data, '__iter__') and not isinstance(data, dict):
                forms = map(lambda obj: self.create_simple_form(obj)(initial=obj), data)
                return loader.render_to_string('simple_form.html', {'forms': forms}, context_instance=context)
            else:
                form = self.create_simple_form(data)(initial=data)
                return loader.render_to_string('simple_form.html', {'form': form}, context_instance=context)
        else:
            return request.form.as_table()
        
