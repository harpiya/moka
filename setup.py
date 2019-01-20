# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T17:55:20+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: setup.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T18:31:23+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri


from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='moka',
    version=version,
    description='Moka Ödeme Sistemi',
    author='Harpiya Yazılım Teknolojileri',
    author_email='info@harpiya.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
