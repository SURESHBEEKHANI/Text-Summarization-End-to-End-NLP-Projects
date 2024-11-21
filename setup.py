import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-End-to-End-NLP-Projects"
AUTHOR_USER_NAME = "SURESHBEEKHANI"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sureshbeekhani26@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/SURESHBEEKHANI/Text-Summarization-End-to-End-NLP-Projects.git",
    project_urls={
        "Bug Tracker": f"https://github.com/SURESHBEEKHANI/Text-Summarization-End-to-End-NLP-Projects.git",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
