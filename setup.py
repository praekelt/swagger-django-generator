from setuptools import setup, find_packages

setup(
    name="swagger-django-generator",
    version="0.0.1",
    description="Generate Django code from a Swagger specification",
    long_description="""
    This utility parses Swagger specifications and creates `urls.py`, `views.py`
    and `schemas.py` files that can be dropped into any existing Django 
    application.
    """,
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    tests_require=[],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
