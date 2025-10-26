from setuptools import setup, find_packages

setup(
    name="promptingvc",
    version="0.1.0",
    description="Version control system for GPT prompts",
    author="PromptingVC",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "promptvc=promptingvc.cli:cli",
        ],
    },
    python_requires=">=3.8",
)
