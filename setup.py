from setuptools import setup, find_packages
import django_redshift_backend

setup(
    name='django_redshift',
    version=1,
    url='https://github.com/thefyk/django-redshift',
    author='Michael Fyk',
    author_email='michael.fyk@vizio.com',
    py_modules=find_packages()
    packages=find_packages()
)
