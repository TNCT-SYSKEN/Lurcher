# Lurcher

## 環境構築

### 環境

- Python 3.6.6
- Node v8.11.4

以下の手順ではMacOS・Linuxによる開発を想定しています、Windowsの場合は適宜読み替えてください。

### 1. Python3の依存関係をインストール

```  bash
~/Lurcher$ pip3 install -r requirements.txt
```

### 2. Nodeの依存関係のインストール

``` bash
~/Lurcher$ npm install
```

### 3. 開発を始める

``` bash
~/Lurcher$ npm run dev
```

上記と並列して以下も実行する

``` bash
~/Lurcher$ python3 manage.py runserver
```

※開発が終わるまで閉じないこと
