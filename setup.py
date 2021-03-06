from setuptools import setup, find_packages

setup(
    name='saml2sp',
    version='0.0.2',
    description='SAML 2.0 Django Application',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read(),
    author='Unomena',
    author_email='dev@unomena.com',
    license='BSD',
    url='http://github.com/unomena/django-saml2-sp',
    packages = find_packages(),
    install_requires = [
    ],
    tests_require=[
        'django-setuptest>=0.1.2',
        'pysqlite>=2.5'
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
