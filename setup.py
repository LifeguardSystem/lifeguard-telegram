from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lifeguard-telegram",
    version="1.1.2",
    url="https://github.com/LifeguardSystem/lifeguard-telegram",
    author="Diego Rubin",
    author_email="contact@diegorubin.dev",
    license="GPL2",
    scripts=[],
    include_package_data=True,
    description="Lifeguard integration with Telegram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["lifeguard", "python-telegram-bot==13.1", "telepot"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
    ],
    packages=find_packages(),
)
