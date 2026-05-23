from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="spiderchain",
    version="1.0.0",
    author="PlayWebit / CipherVault",
    description="Cross-table hash architecture for tamper-proof blockchain data integrity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/playwebit/spiderchain-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "supabase": ["supabase>=1.0.0"],
        "postgres": ["sqlalchemy>=1.4.0", "psycopg2-binary>=2.9.0"],
        "mysql": ["sqlalchemy>=1.4.0", "pymysql>=1.0.0"],
        "evm": ["web3>=6.0.0"],
        "all": [
            "supabase>=1.0.0",
            "sqlalchemy>=1.4.0",
            "psycopg2-binary>=2.9.0",
            "web3>=6.0.0",
            "requests>=2.28.0"
        ]
    }
)
