# Lurcher

## 環境構築

### 環境

- Python 3.6.6
- Node v8.11.4

以下の手順ではMacOS・Linuxによる開発を想定しています、Windowsの場合は適宜読み替えてください。

なお、以下の全てのコマンドはコマンドプロンプトまたはシェルで実行します。

### 1. リポジトリをクローン

``` bash
git clone git@github.com:TNCT-SYSKEN/Lurcher.git
```

### 2. Python3の依存関係をインストール

```  bash
$ cd Lurcher
~/Lurcher$ pip3 install -r requirements.txt
```

### 3. Nodeの依存関係のインストール

``` bash
~/Lurcher$ npm install
```

### 4. 開発を始める

``` bash
~/Lurcher$ npm run dev
```

上記と並列して、もう１つコマンドプロンプト・シェルを開いて以下も実行する

``` bash
~/Lurcher$ python3 manage.py runserver
```

※開発が終わるまで閉じないこと
