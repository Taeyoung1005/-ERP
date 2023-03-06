from import_export import resources
from .models import *

#재직자
class HrResource(resources.ModelResource):
    class Meta:
        model = HR
        filter = {"재직or퇴직" : "재직"}
        # exclude = ['재직or퇴직']