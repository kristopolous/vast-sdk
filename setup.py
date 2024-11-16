from setuptools import setup, find_packages

setup(
    name="vastai_sdk",
    version="0.2.0",
    description="SDK for Vast.ai GPU Cloud Service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Chris McKenzie",
    author_email="chris@vast.ai",
    url="https://github.com/yourusername/vastai-sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25",
        "jsonschema>=3.2",
		"xdg>=1.0.0",
		"argcomplete==3.5.1",
		"requests==2.32.3",
		"borb==2.0.17",
		"python-dateutil",
		"pytz",
		"urllib3==2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)