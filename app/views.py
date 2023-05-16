from django.shortcuts import render

# Create your views here.'

from typing import Any,Dict
from django.views.generic import TemplateView

class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)

        EDCO['name']='junaid'
        EDCO['age']=24

        return EDCO
    

