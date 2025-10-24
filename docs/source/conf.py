# # Configuration file for the Sphinx documentation builder.
# #
# # For the full list of built-in configuration values, see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html

# # -- Project information -----------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'My Notebooks'
# copyright = '2025, TJK'
# author = 'TJK'
# release = '0.1'

# # -- General configuration ---------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = [
#     "myst_parser",  # 让 Sphinx 支持 .md 文件
# ]

# templates_path = ['_templates']
# exclude_patterns = []

# language = 'zh_CN'

# # -- Options for HTML output -------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinx_rtd_theme"   #'alabaster'
# html_static_path = ['_static']
# -- Project information -----------------------------------------------------
project = 'My Notebooks'
copyright = '2025, TJK'
author = 'TJK'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",          # 支持 Markdown
    "sphinx.ext.mathjax",   # 用 MathJax 渲染公式
]

# 让 myst 支持 $...$ 和 $$...$$
myst_enable_extensions = [
    "amsmath",    # $$ 对齐环境
    "dollarmath"  # 行内和块公式
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
