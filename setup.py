from setuptools import setup

setup(
	name='pythonImageConverter',
	version='1.0.7.4',
	license="MIT",
	description='Convert image types using CLI',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='http://github.com/Johntheprogrammer92',
	url='http://github.com/Johntheprogrammer92/pythonImageConverter',
	include_package_data=True,
    install_requires=[
		'pillow>=7.2.0','PyQt5>=5.15.1'],
    packages=['pythonImageConverter'],
	
    entry_points={
		'console_scripts' : [
			'pic=pythonImageConverter.pic:main'
		]
	}
)
