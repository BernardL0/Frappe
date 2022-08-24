from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in basic_custom_app/__init__.py
from basic_custom_app import __version__ as version

setup(
	name="basic_custom_app",
	version=version,
	description="A basic custom app that uses the available hooks to modify strings before displaying them.",
	author="Bernard Louie Estioco",
	author_email="bernardlouiee0@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
