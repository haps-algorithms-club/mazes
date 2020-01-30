"""Setup script for hapsmazes."""
from setuptools import setup, find_packages


setup(
    name="hapsmazes",
    author="Konrad Jałowiecki",
    author_email="dexter2206@gmail.com",
    entry_points={"console_scripts": ["generate-maze=hapsmazes.scripts.generate_maze:main"]},
    requires=["numpy", "matplotlib"],
    packages=find_packages(),
)
