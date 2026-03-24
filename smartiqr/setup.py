from setuptools import setup, find_packages  # setuptools library package build karayla use hote
# setup() main function ahe # find_packages() inner packages automatically detect karto

setup(
    name="smartiqr",  # PyPI var disnar package name (pip install smartiqr)
    version="0.1.0",  # Version format: major.minor.patch
    author="Vishakha",  # Author name
    author_email="badgujarvishakha8@gmail.com",  # Author email (optional but recommended)
    description="Automatic IQR-based outlier detection library",  # Short description
    long_description=open("README.md", encoding="utf-8").read(),  # README.md cha content PyPI var disel
    long_description_content_type="text/markdown",  # README markdown format madhe ahe
    packages=find_packages(),  # Inner smartiqr package automatically detect hoil
    install_requires=["pandas"], # He dependency automatic install hoil
    python_requires=">=3.8",  # Minimum Python version required
    license="MIT",  # MIT license use karto
    classifiers=[  # PyPI filtering sathi metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)