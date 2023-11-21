import subprocess
from datetime import datetime

import yaml


def update_yaml(file_name):
    # 현재 시간을 가져옵니다.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # YAML 파일을 읽습니다.
    with open(file_name, "r") as file:
        data = yaml.safe_load(file)

    # 'html' 섹션 내의 'extra_footer' 키에 현재 시간을 삽입합니다.
    if "html" in data and "extra_footer" in data["html"]:
        data["html"][
            "extra_footer"
        ] = f"based on jupyter-book, last updated: {current_time}"
    else:
        print("'extra_footer' key is not found in the YAML file.")

    # 파일에 변경사항을 다시 씁니다.
    with open(file_name, "w") as file:
        yaml.dump(data, file, default_flow_style=False)


def build_publish_jupyter_book():
    # Jupyter Book 빌드 명령을 실행합니다.
    subprocess.run(["jupyter-book", "build", "."])
    subprocess.run(["ghp-import", "-n", "-p", "-f", "./_build/html"])


def git_commit_push_and_merge(main_branch_name="main"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Update at {current_time}"

    # 현재 브랜치에서 변경사항을 커밋합니다.
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])

    # main 브랜치로 체크아웃합니다.
    subprocess.run(["git", "checkout", main_branch_name])
    # 변경사항을 원격 저장소에 푸시합니다.
    subprocess.run(["git", "push", "origin", main_branch_name])


if __name__ == "__main__":
    # YAML 파일 경로를 지정합니다. 이 경로는 필요에 따라 조정할 수 있습니다.
    yaml_file_path = "_config.yml"
    update_yaml(yaml_file_path)
    build_publish_jupyter_book()
    git_commit_push_and_merge()
