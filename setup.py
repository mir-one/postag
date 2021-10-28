import io
import setuptools

#with io.open("README.md", mode="r", encoding='utf-8') as fh:
#    long_description = fh.read()

setuptools.setup(
    name="postag",
    version="0.0.1",
    author="Roman Inozemtsev",
    author_email="dao@mir.one",
    description="Part-of-Speech Tagger for Russian language",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/mir-one/postag",
    packages=setuptools.find_packages(),
    package_data={'postag': ['postag.config', 'postag.model']},
    include_package_data=True,
   
)
