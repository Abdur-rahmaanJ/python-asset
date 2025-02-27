# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools

# Package metadata.

name = "google-cloud-asset"
description = "Cloud Asset API API client library"
version = "3.3.0"
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    # NOTE: Maintainers, please do not require google-api-core>=2.x.x
    # Until this issue is closed
    # https://github.com/googleapis/google-cloud-python/issues/10566
    "google-api-core[grpc] >= 1.26.0, <3.0.0dev",
    "grpc-google-iam-v1 >= 0.12.3, < 0.13dev",
    "google-cloud-access-context-manager >= 0.1.2, < 0.2.0dev",
    "google-cloud-org-policy>=0.1.2, <2.0.0",
    "google-cloud-os-config >= 1.0.0, <2.0.0dev",
    "proto-plus >= 1.10.0",
    "packaging >= 14.3",
]

extras = {"libcst": "libcst >= 0.2.5"}

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("google")
]

# Determine which namespaces are needed.
namespaces = ["google"]
if "google.cloud" in packages:
    namespaces.append("google.cloud")

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/googleapis/python-asset",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    extras_requires=extras,
    python_requires=">=3.6",
    scripts=[
        "scripts/fixup_asset_v1_keywords.py",
        "scripts/fixup_asset_v1beta1_keywords.py",
        "scripts/fixup_asset_v1p1beta1_keywords.py",
        "scripts/fixup_asset_v1p2beta1_keywords.py",
        "scripts/fixup_asset_v1p4beta1_keywords.py",
        "scripts/fixup_asset_v1p5beta1_keywords.py",
    ],
    include_package_data=True,
    zip_safe=False,
)
