from setuptools import setup
import re

version = ""
with open("discord/ext/dashboard/__init__.py") as f:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError("version is not set")
		

readme = ""
with open('README.md') as f:
	readme = f.read()
	

requirements = ["discord.py>=1.5.1"]

setup(name='discord-ext-dashboard',
      author='MaseZev',
      url='https://github.com/MaseZev/discord-ext-dashboard',
      version=version,
      packages=['discord.ext.dashboard'],
      license='mit',
      description='Веб-перехватчик и расширение discord.py на основе запросов для создания панели управления ботом.',
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires='>=3.5.3',
      classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
