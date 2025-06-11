from setuptools import find_packages, setup

about = {}
with open("mq_gen/__about__.py") as fp:
    exec(fp.read(), about)

with open("README.md") as fp:
    long_description = fp.read()

setup(name='mq-generator',
      version=about["__version__"],
      description=about["__summary__"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Zachary Cutlip",
      author_email="uid000@gmail.com",
      url="TBD",
      license="MIT",
      packages=find_packages(),
      entry_points={
          'console_scripts': ['mq-gen=mq_gen.cli:main'], },
      python_requires='>=3.10',
      install_requires=[],
      package_data={'mq_gen': ['config/*']},
      )
