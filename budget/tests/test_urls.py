from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from budget.views import project_list, project_detail, ProjectCreateView

"""
class TestCheck(SimpleTestCase):

    def test_the_testsetup(self):
        #assert 1 == 2 # returns     assert 1 == 2 AssertionError
"""
"""
urls to unit test from urls.py
        urlpatterns = [
    path('', views.project_list, name='list'),
    path('add/', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>/', views.project_detail, name='detail')
]
"""

class TestUrls(SimpleTestCase):

    def list_resolves(self):
        url = reverse('list')
        print(resolve(url)) #use resolve function to pass the url

        """
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ResolverMatch(func=budget.views.project_list, args=(), kwargs={}, url_name=list, app_names=[], namespaces=[])
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.007s

        OK
        """
        self.assertEquals(resolve(url).func, project_list)

        """
        ----------------------------------------------------------------------
        Ran 1 test in 0.008s

        OK
        """

    def add_resolves(self):
        url = reverse('add')
        #self.assertEquals(resolve(url).func, ProjectCreateView) # ProjectCreateView is a class based view so throws an error below
        """
        ======================================================================
        FAIL: test_list_url_is_resolved (tests.test_urls.TestUrls)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "F:\Dominic\Python\django-testing-dslove\django-testing-dslove\budgetproject\budget\tests\test_urls.py", line 48, in test_list_url_is_resolved
            self.assertEquals(resolve(url).func, ProjectCreateView)
        AssertionError: <function ProjectCreateView at 0x0000023CFBE7EDC8> != <class 'budget.views.ProjectCreateView'>

        ----------------------------------------------------------------------
        Ran 1 test in 0.008s

        FAILED (failures=1)
        Destroying test database for alias 'default'...

        """
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView) # func.view_class fixes the foregoing aror
        
        """
        ----------------------------------------------------------------------
        Ran 1 test in 0.005s

        OK
        Destroying test database for alias 'default'...
        """
    def detail_resolves(self):
        url = reverse('detail', args=['a-slug']) # args included as url definition uses a slug
        self.assertEquals(resolve(url).func, project_detail) 
        
        """
         ----------------------------------------------------------------------
        Ran 1 test in 0.007s

        OK
        Destroying test database for alias 'default'...
        """