import setuptools

with open('README.md', 'r') as in_:
    long_description = in_.read()

setuptools.setup(
    name='deploynow',
    version='1.0.0',
    author='Anushka Yohan',
    author_email='aliyanage44@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yohanAnush/code-deploy-now',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"
                 ],
    install_requires=['boto3'],
    scripts=['scripts/deploynow']
)
