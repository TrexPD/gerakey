from setuptools import setup, find_packages

setup(
    name='gerakey',
    version='0.0.4',
    license='MIT',
    author='Paulo Daniel',
    platforms=['Windows', 'Linux', 'BSD'],
    url='https://github.com/TrexPD/gerakey.git',
    download_url='https://github.com/TrexPD/gerakey.git',
    description='App CLI para gerar senhas, keys ou token de maneira aleatória!',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'rich'
    ],
    entry_points="""
    [console_scripts]
    gerakey = gerakey:gerador_keys
    """
)


# Versão antiga!

# setup(
#     name='gerakey CLI',
#     version='0.0.3',
#     license='MIT',
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=[
#         'click', 'rich'
#     ],
#     zip_safe=False,
#     entry_points={'console_scripts': ['gerakey = gerakey:gerador_keys']},
# )