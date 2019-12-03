from distutils.core import setup

setup(
    name="django-postgreconnect",
    packages=["django-postgreconnect",],
    version="0.3",
    description="A Django backend that automatically reconnects to postgres if the connection is lost.",
    author="Jared Mackey",
    author_email="jared@mackeydevelopments.com",
    url="https://github.com/mackeyja92/django-postgreconnect",
    keywords=["django", "postgres"],
    classifiers=[],
)
