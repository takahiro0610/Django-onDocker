# Pythonの公式イメージをベースに使用 3.8を指定
FROM python:3.8

# 環境変数を設定 この場合、Pythonが標準出力と標準エラーにすぐに書き込む
ENV PYTHONUNBUFFERED=1

# Docker内の作業ディレクトリを設定
WORKDIR /code

# ホストのrequirements.txtをDockerイメージの/codeにコピー
COPY requirements.txt /code/

# pipを使ってrequirements.txtに記載されているパッケージをインストール
RUN pip install -r requirements.txt

# ホストの存在しているすべてのファイルをDockerイメージの/codeにコピー
COPY . /code/