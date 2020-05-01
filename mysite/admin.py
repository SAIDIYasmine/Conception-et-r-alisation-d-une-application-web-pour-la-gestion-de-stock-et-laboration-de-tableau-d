from django.contrib import admin
from .models import ClientInfo
from .models import FournisseurInfo
from .models import ProduitInfo
from .models import EntreeInfo
from .models import SortieInfo
from .models import UtilisateurInfo


admin.site.register(ClientInfo)
admin.site.register(FournisseurInfo)
admin.site.register(ProduitInfo)
admin.site.register(EntreeInfo)
admin.site.register(SortieInfo)
admin.site.register(UtilisateurInfo)