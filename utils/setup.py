from setuptools import setup

setup(
    name="utils",
    version="0.1.0",
    packages=["utils"],
    package_dir={"utils": "."},
    install_requires=[
        "clickhouse-driver>=0.2.0",
        "pandas>=1.5.0",
        "sqlalchemy>=2.0.0",
        "clickhouse-sqlalchemy>=0.2.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.12",
)
