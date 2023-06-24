from django.urls import path
from home import views


urlpatterns = [
    path('redundant_icmr_all', views.redundant_icmr_all , name = 'redundant_icmr_all'),
    path('redundant_icmr_s_all', views.redundant_icmr_s_all , name = 'redundant_icmr_s_all'),
    path('redundant_icmr_umc_all', views.redundant_icmr_umc_all , name = 'redundant_icmr_umc_all'),
    path('redundant_icmr_pn_all', views.redundant_icmr_pn_all , name = 'redundant_icmr_pn_all'),
    path('diff_res_jn', views.diff_res_jn , name = 'diff_res_jn'),
    path('diff_res_jn_pcr', views.diff_res_jn_pcr , name = 'diff_res_jn_pcr'),
    path('redundant_lab_id', views.redundant_lab_id , name = 'redundant_lab_id'),


    path('redundant', views.redundant_ids , name = 'redundantids'),
    path('mapss', views.mapss , name = 'mapss'),
    path('mapss_html', views.mapss_html , name = 'mapss_html'),
    path('slogans', views.slogans , name = 'slogans'),





]