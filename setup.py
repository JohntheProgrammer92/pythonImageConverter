from setuptools import setup

setup(
	name='pyImgConvert',
	version='1.0.0',
	license="MIT",
	description='Convert image types using CLI',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='http://github.com/Johntheprogrammer92',
	url='http://github.com/Johntheprogrammer92/pyImgConvert',
    install_requires=[
		'pillow>=7.2.0'],
    packages=['imgConvert'],
	
    entry_points={
		'console_scripts' : [
			'pic=pyImgConvert.imgConvert:main'
		]
	}
)
