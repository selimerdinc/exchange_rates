from setuptools import setup, find_packages

setup(
    name='exchange_rates',  # Paketinizin adı
    version='0.1',              # Paketinizin sürümü
    packages=find_packages(),   # Paketinizin içindeki paketleri otomatik olarak bulur
    install_requires=[          # Bağımlılıklarınız
        'requests',
        'beautifulsoup4',
        'flask',
        'flasgger'
    ],
    entry_points={              # Komut satırından çalıştırılabilir scriptler için
        'console_scripts': [
            'exchange_rates-cli=exchange_rates.cli:main',
        ],
    },
    author='selimerdinc',         # Paketin yazarı
    author_email='serdinc10@gmail.com',  # Yazarın e-posta adresi
    description='A Python library for fetching exchange rates.',  # Paketin kısa açıklaması
    license='MIT',              # Lisans türü
    url='https://github.com/selimerdinc/exchange_rates',  # Projenizin GitHub veya diğer URL'i
)
