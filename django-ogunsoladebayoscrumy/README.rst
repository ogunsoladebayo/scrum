=====
ogunsoladebayoscrumy
=====

ogunsoladebayoscrumy is a sample Django app to practice Django.

Quick start
-----------

1. Add "ogunsoladebayoscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ogunsoladebayoscrumy',
    ]

2. Include the ogunsoladebayoscrumy URLconf in your project urls.py like this::

    path('ogunsoladebayoscrumy/', include('ogunsoladebayoscrumy.urls')),

3. Run ``python manage.py migrate`` to create the ogunsoladebayoscrumy models.

4. Visit http://127.0.0.1:8000/ogunsoladebayoscrumy/ to use the app.