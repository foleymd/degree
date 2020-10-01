# from degree.minors.settings import STATIC_URL
from django.conf import settings

PROJECT_UTD_DEFAULTS = {'document_title': 'Minor/Certificate Administrative Suite',
                        'window_title': 'Minor / Certificate Awarding System',
                        'css_file': [settings.STATIC_URL + 'css/manage_student.css'],
                        'navbar_title': ['Search by EID', 'Search by Credential Code', 'Reports', 'Minor / Certificate Inventory System', 'Log'],
                        'navbar_type': ['L', 'L', 'L', 'L', 'L'],
                        'navbar_url': ['/apps/degree/minors/manage_student',
                                       '/apps/degree/minors/manage_student/search_by_code/',
                                       '/apps/degree/minors/manage_student/reports/',
                                       '/apps/degree/minors/',
                                       '/apps/degree/minors/log/',],
                        'api_key': '8B54A49X54',
                        }
PROJECT_UTD_DEFAULTS_ADMIN = {'document_title': 'Minor/Certificate Administrative Suite',
                              'window_title': 'Minor / Certificate Awarding System',
                              'css_file': [settings.STATIC_URL + 'css/manage_student.css'],
                              'navbar_title': ['Search by EID', 'Search by Credential Code', 'Late Add Inbox', 'Reports', 'Minor / Certificate Inventory System', 'Log'],
                              'navbar_type': ['L', 'L', 'L', 'L', 'L', 'L'],
                              'navbar_url': ['/apps/degree/minors/manage_student',
                                            '/apps/degree/minors/manage_student/search_by_code/',
                                            '/apps/degree/minors/manage_student/late_add_inbox/ ',
                                            '/apps/degree/minors/manage_student/reports/',
                                            '/apps/degree/minors/',
                                            '/apps/degree/minors/log',],
                                            'api_key': '8B54A49X54',
                            }