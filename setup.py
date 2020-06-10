from setuptools import setup, find_packages

setup(name='pythonFiles',
      version='1.0',
      description='pythonFiles: Description',
      url='https://github.com/dmelwani99/PythonFileManagement',
      author='Deepak Melwani, Teague Henry',
      author_email='dmelwani99@gmail.com',
      license='MIT',
      python_requires='>=3.6',
      include_package_data=True,
      packages=find_packages(),
      install_requires=['pandas',
                        'numpy'
                        ],
      zip_safe=False
      )