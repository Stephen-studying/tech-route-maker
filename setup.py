from setuptools import setup


setup(
    name="tech-route-maker",
    version="0.4.0",
    description="Evidence-grounded editable technical route diagrams for research and engineering projects.",
    packages=["tech_route_maker", "scripts"],
    install_requires=["python-pptx>=1.0.0"],
    entry_points={"console_scripts": ["trm=tech_route_maker.cli:main"]},
)
