import setuptools

setuptools.setup(
    name="shopping_assistant",
    description="Shopping assistant backend",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=[
        "fastapi==0.63.0",
        "pydantic==1.7.3",
        "pymongo==3.11.3",
        "uvicorn==0.13.3"
    ]
)
