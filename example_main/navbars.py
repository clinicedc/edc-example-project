from copy import copy
from django.conf import settings
from edc_lab_dashboard.navbars import navbar as lab_navbar
from edc_review_dashboard.navbars import navbar as review_navbar
from edc_navbar import site_navbars, Navbar

navbar = Navbar(name=settings.APP_NAME)

navbar_item = copy([item for item in lab_navbar.items if item.name == "specimens"][0])
navbar_item.active = False
navbar_item.label = "Specimens"
navbar.append_item(navbar_item)


for item in review_navbar.items:
    navbar.append_item(item)

site_navbars.register(navbar)
