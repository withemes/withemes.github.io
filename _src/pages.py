# -*- coding: utf-8 -*-
"""All pages, in sitemap order."""
from p_core import (HOME, ABOUT, SERVICE_HUB, PRICING_PAGE, PROCESS, PROJECTS,
                    FAQ_PAGE, CONTACT, THANKS, TERMS, PRIVACY)
from p_svc import SERVICES_PAGES
from p_kb import KB_PAGES

PAGES = ([HOME, ABOUT, SERVICE_HUB] + SERVICES_PAGES +
         [PRICING_PAGE, PROCESS, PROJECTS, FAQ_PAGE] + KB_PAGES +
         [CONTACT, THANKS, TERMS, PRIVACY])
