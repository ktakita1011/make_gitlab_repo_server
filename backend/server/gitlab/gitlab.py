import os
import requests

from flask import Blueprint
gitlab = Blueprint('func', __name__)

def create_gitlab_project(access_token, project_name, group_id, url="https://gitlab.example.com/api/v4/projects"):
    """
    GitLabに新しいプロジェクトを作成する関数。
    
    :param access_token: GitLab APIを使用するためのアクセストークン
    :param project_name: 作成するプロジェクトの名前
    :param group_id: プロジェクトを作成するグループのID
    :param url: GitLab APIのエンドポイント（デフォルトで設定済み）
    :return: APIからのレスポンス
    """
    # ヘッダーとデータ辞書を作成
    headers = {"PRIVATE-TOKEN": access_token}
    data = {"name": project_name, "namespace_id": group_id}
    
    # POSTリクエストを送信
    response = requests.post(url, headers=headers, data=data)
    
    return response.text

@gitlab.route("/gitlab", method=["GET"])
def post_new_gitlab_project(project_name, group_id):
    # 関数を使用する例
    access_token = os.getenv("PRIVATE_TOKEN")
    gitlab_url = os.getenv("GITLAB_URL")
    response = create_gitlab_project(access_token, project_name, group_id, url=gitlab_url)
    print(response)
