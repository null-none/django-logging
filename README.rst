=======
Install
=======

.. code-block:: bash

    pip install django-logging

=======
Quick start
=======

1. Add "django_logging" to your INSTALLED_APPS settings like this:

.. code-block:: python
    INSTALLED_APPS = (
        ...
        'django_logging',
    )

2. Include the 'django_logging.middleware' middleware in your MIDDLEWARE_CLASSES like this:

.. code-block:: python
    MIDDLEWARE_CLASSES = [
        'django_logging.middleware',
        ...
    ]

=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
