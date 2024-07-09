from django.urls import path
from .views import Home,About,Contact,FAQS,Blogs,Service,PersonalBrand,imageconsulting,corporaterebranding,\
                   Blogdetails,service_home,launchpad,Policy,Questionsform,Works,Tdh,Carrers,Newsletter,Newslettertwo,Brand,Newsletterthree,Tenalidoublehorse,Suryacolours,Zavaine,Triplex,Rishikatdh,Vsb,Ourmedia,BrandRefresh,applyjobform,jobdetails,myexpertise,workdetails
from django.contrib.sitemaps.views import sitemap
from magsmenapp.sitemap import PostSitemap,StaticPagesSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'posts': PostSitemap,
    'static_pages': StaticPagesSitemap,
}


urlpatterns = [
    path('', Home , name='home'),
    path('ourstory/', About , name='ourstory'),
    path('faqs/', FAQS , name='faqs'),
    path('reach-us-out/', Contact , name='reach-us-out'),
    path('expertise/', service_home , name='expertise'),
    path('blogs/', Blogs , name='blogs'),
    path('brandconsulting/', Service , name='brandconsulting'),
    path('personalbrand/', PersonalBrand , name='personalbrand'),
    path('imageconsulting/', imageconsulting , name='imageconsulting'),
    path('launchpad/', launchpad , name='launchpad'),
    path('corporaterebranding/', corporaterebranding , name='corporaterebranding'),
    path('blog/<str:slug>', Blogdetails , name='blog'),
    path('questions/', Questionsform , name='questions'),
    path('privacy-policy/', Policy , name='privacy-policy'),
    path('works/', Works , name='works'),
    path('work-details/<str:slug>',workdetails,name="work-details"),
    path('tenali-double-horse/', Tdh , name='tenali-double-horse'),
    path('carrerspage/', Carrers , name='carrerspage'),
    path('news-letter-august-2023/',Newsletter,name='news-letter-august-2023'),
    path('brand-architecture/',Brand,name='brand-architecture'),
    path('brand-corner-october-edition/',Newslettertwo,name='the-name-of-the-article-indian-brand-success-stories'),
    path('brand-corner-november-edition/',Newsletterthree,name='brand-corner-november-edition'), 
    path('brand-refresh-vs-rebranding/',BrandRefresh,name="brand-refresh-rebranding") ,
    path('suryacolours/',Suryacolours,name='suryacolours'),  
    path('tenalidoublehorse/',Tenalidoublehorse,name='tenalidoublehorse'),
    path('triplex/',Triplex,name='triplex'),  
    path('zavaine/',Zavaine,name='zavaine'),
    path('rishikatdh/',Rishikatdh,name='rishikatdh'),  
    path('vsb/',Vsb,name='vsb'),
    path('gallery/',Ourmedia,name='gallery'),
    path('job-details/<str:slug>',jobdetails,name='jobdetails'),
    path('applyform/',applyjobform,name='applyform'),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),   
    path('robots.txt',TemplateView.as_view(template_name="uifiles/robots.txt", content_type="text/plain")),
    # path('myexpertise/',myexpertise,name="myexpertise"),
  

    
]