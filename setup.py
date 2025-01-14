from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="hdw_tools",
    version="0.0.6",
    description="Horizon Data Wave Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="HorizonDataWave",
    author_email="pip@horizondatawave.ai",
    url="https://github.com/horizondatawave/hdw-tools",
    license="MIT",
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=[
        "requests~=2.32.3",
        "llama-index-core~=0.11.22",
        "pydantic~=2.10.5",
        "pydantic-settings~=2.6.1",
        "crewai-tools~=0.25.8",
    ],
)
