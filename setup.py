import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

 
setuptools.setup(
    name='AutoLocalizationTask',
    version='0.0.2',
    author='Faisal Alshargi',
    author_email='falsharg@amazon.com',
    description='Auto Localization Task package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alshargi/AutoLocalizationTask',
    project_urls = {
        "Bug Tracker": "https://github.com/alshargi/AutoLocalizationTask/issues"
    },
    license='MIT',
    packages=['AutoLocalizationTask'],
    package_data={'AutoLocalizationTask': ['models/*.txt', 'models/*.sav']}, 
    install_requires=['requests'],
)
