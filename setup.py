from setuptools import find_packages, setup

requirements = ["typer[all]==0.9.0", "rich==13.4.2", "textual==0.32.0"]

setup(
    name="oartui",
    version="0.2.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "oartui = oartui.main:entry_point",
            "oarui = oartui.main:entry_point",
            "oui = oartui.main:entry_point",
        ],
    },
    install_requires=requirements,
    package_data={
        "oartui": ["css/*"],
    },
)
