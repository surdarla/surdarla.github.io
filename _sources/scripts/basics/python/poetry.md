# Poetry 사용하기

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Poetry-github](https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white)](https://github.com/python-poetry/poetry)

: Python packaging and dependency management made easy\
`pyproject.toml`이라는 파일 하나로 setup.py, requirements.txt, pip등 어쩌구 저쩌구 대부분의 의존성 문제를 해결하려는 python의 노력들을 하나로 통합하는 라이브러리이다.

많은 장점들이 있는 것으로 보이지만 우선 간단하게 사용해본 결과로는 이렇다.

1. 프로젝트 격리: Poetry는 프로젝트의 종속성을 자동으로 격리된 가상 환경에 설치한다. 이는 pip에서는 수동으로 해야 하는 것이지만, Poetry에서는 자동으로 이루어진다.
2. 패키지 배포: pip는 패키지 설치 도구로 설계되었지만, Poetry는 패키지 생성 및 배포를 지원한다. 이는 프로젝트를 PyPI에 게시하고 다른 사람들이 사용할 수 있게 하는 데 도움된다.
3. 결정론적 설치: Poetry.lock 파일을 사용하여 프로젝트의 종속성을 정확하게 버전별로 추적한다. 이는 동일한 프로젝트를 다른 시스템에서 재현할 때 도움된다.

```toml
[tool.poetry]
name = "my-package"
version = "0.1.0"
description = "The description of the package"

license = "MIT"

authors = [
    "Sébastien Eustace <sebastien@eustace.io>"
]

repository = "https://github.com/python-poetry/poetry"
homepage = "https://python-poetry.org"

# README file(s) are used as the package description
readme = ["README.md", "LICENSE"]

# Keywords (translated to tags on the package index)
keywords = ["packaging", "poetry"]

[tool.poetry.dependencies]
# Compatible Python versions
python = ">=3.8"
# Standard dependency with semver constraints
aiohttp = "^3.8.1"
# Dependency with extras
requests = { version = "^2.28", extras = ["security"] }
# Version-specific dependencies with prereleases allowed
tomli = { version = "^2.0.1", python = "<3.11", allow-prereleases = true }
# Git dependencies
cleo = { git = "https://github.com/python-poetry/cleo.git", branch = "master" }
# Optional dependencies (installed by extras)
pendulum = { version = "^2.1.2", optional = true }

# Dependency groups are supported for organizing your dependencies
[tool.poetry.group.dev.dependencies]
pytest = "^7.1.2"
pytest-cov = "^3.0"

# ...and can be installed only when explicitly requested
[tool.poetry.group.docs]
optional = true
[tool.poetry.group.docs.dependencies]
Sphinx = "^5.1.1"

# Python-style entrypoints and scripts are easily expressed
[tool.poetry.scripts]
my-script = "my_package:main"
```

## main functions

차근차근 하나씩 따라가보면 이해된다.

```pwsh
# 설치 : py가 아니라 python으로 해줘야한다.
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# 프로젝트 생성
poetry new your-project-name

# 기존 폴더에 poetry 덮기
poetry init

# pyproject.toml 읽어서 poetry.lock 생성 - 가상환경도 생성
poetry install
poetry add your-package-name

# poetry.lock 갱신
poetry update

# 패키지 삭제
poetry remove your-package-name

# lock파일의 package 구성 확인
poetry show --tree

# poetry.lock 파일과 pyproject.toml 파일의 종속성이 동일한지 확인
poetry check
```

가상환경 사용

```pwsh
# venv 들어가기
poetry shell

# venv 나가기
exit

# 환경정보 확인
poetry env info --path
poetry env list
poetry env remove
```

## requirements.txt -> pyproject.toml

기존의 requirements.txt를 사용해서 poetry add를 일괄적으로 하는 방법도 존재한다. 그래도 꼴에 예전부터 사용하던 것이기 때문에 requirements.txt도 여전히 많이 사용되고 있다.

맥에서는 이렇게 해주면되고

```linux
cat requirements.txt | xargs poetry add
```

윈도우 powershell에서는 아래처럼 해주면 된다.

```powershell
Get-Content requirements.txt | ForEach-Object { poetry add $_ }
```

리눅스 명령어들이 바로 파워쉘에서는 사용되지 않기 때문에 조금 명령어가 다를 수 있다. `xargs`는 입력을 받아서 각각의 입력에 대해 특정 명령어를 실행하는 역할을 한다. 여기서는 js에서 처럼 foreach를 사용하는 모습을 보인다.

만약 스크립트 실행 권한이 비활성화 되어있으면 `Set-ExecutionPolicy remoteSigned`를 쳐준다.
