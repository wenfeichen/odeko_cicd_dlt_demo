from setuptools import find_packages, setup
#from odeko_cicd_dlt_demo import __version__

setup(
    name="odeko_cicd_dlt_demo",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version="0.0.1",
    description="odeko_cicd_dlt_demo",
    author="wchen@odeko.com",
)
