from setuptools import find_packages,setup

setup(
    name='flaskr-mklthabo',
    version='1.0.0',
    author='Thabo Makola',
    author_email='mkl.thabo@gmail.com',
    description='flask blog application',
    url = 'https://github.com/MKLThabo/flask-tutorial.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

