# Import the setuptools module, which is used to package and distribute Python projects
import setuptools

# Open the README.md file in read mode with UTF-8 encoding and store its contents in long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Define key information about the repository, the author, and the source code
REPO_NAME = "Text-Summarization-End-to-End-NLP-Projects"  # The name of the repository
AUTHOR_USER_NAME = "SURESHBEEKHANI"  # The username of the author on GitHub
SRC_REPO = "textSummarizer"  # The name of the source directory or module
AUTHOR_EMAIL = "sureshbeekhani26@gmail.com"  # Author's email address

# Call setuptools.setup to define how the package should be installed and distributed
setuptools.setup(
    name=SRC_REPO,  # The name of the Python package
    version=__version__,  # The version of the package
    author=AUTHOR_USER_NAME,  # The author's username
    author_email=AUTHOR_EMAIL,  # The author's email address
    description="A small python package for NLP app",  # A brief description of the package
    long_description=long_description,  # A detailed description read from README.md
    long_description_content_type="text/markdown",  # Specifies that the long description is in Markdown format
    url=f"https://github.com/SURESHBEEKHANI/Text-Summarization-End-to-End-NLP-Projects.git",  # The URL of the GitHub repository
    project_urls={  # Additional URLs related to the project (e.g., bug tracker, documentation)
        "Bug Tracker": f"https://github.com/SURESHBEEKHANI/Text-Summarization-End-to-End-NLP-Projects.git",  # Link to bug tracker or issues page
    },
    package_dir={"": "src"},  # Specifies that the Python packages are located in the "src" directory
    packages=setuptools.find_packages(where="src"),  # Automatically finds all packages in the "src" directory
    classifiers=[  # A list of classifiers that provide metadata about the package
        "Programming Language :: Python :: 3",  # Specifies the Python version compatibility
        "License :: OSI Approved :: MIT License",  # The license type under which the package is distributed
        "Operating System :: OS Independent",  # The package can run on any operating system
    ],
    python_requires='>=3.6',  # Specifies the minimum required Python version (>= 3.6)
)
