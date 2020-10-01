# from degree.minors.settings import STATIC_URL
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

PROJECT_UTD_DEFAULTS = {'document_title': 'Minor / Certificate System',
                        'window_title': 'Minor / Certificate System',
                        'css_file': [settings.STATIC_URL + 'common/css/common.css'],
                        'navbar_title': ['Search by EID', 'Search by Credential Code', 'Reports', 'Minors System', 'Log'],
                        'navbar_type': ['L', 'L', 'L', 'L', 'L'],
                        'navbar_url': [reverse_lazy('search_by_eid'),
                                       reverse_lazy('search_by_code'),
                                       reverse_lazy('reports'),
                                       reverse_lazy('index_link'),
                                       reverse_lazy('search'),
                                       ],
                        'api_key': '8B54A49X54',
                        }