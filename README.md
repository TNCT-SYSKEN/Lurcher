# Lurcher

## 環境構築

### 環境

- Python 3.6.6
- Node v8.11.4

以下の手順ではMacOS・Linuxによる開発を想定しています、Windowsの場合は適宜読み替えてください。

なお、以下の全てのコマンドはコマンドプロンプトまたはシェルで実行します。

### 1. リポジトリをクローン

``` bash
$ git clone git@github.com:TNCT-SYSKEN/Lurcher.git
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

## プロジェクトについて

### ディレクトリ構造

```
Lurcher
├── README.md
├── db.sqlite3
├── lurcher
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mainsite
│   ├── __init__.py
│   ├── admin.py
│   ├── ...
├── manage.py
├── node_modules
│   ├── abbrev
│   ├── ajv
│   ├── ...
├── package-lock.json
├── package.json
├── requirements.txt
├── src
│   ├── images
│   ├── scripts
│   └── styles
└── static
    └── styles
```

`npm run dev` を実行すると `src` ディレクトリ以下がコンパイル、またはコピーされて `static` ディレクトリに配置されます。

### 開発者の扱う範囲

開発者が主に扱うディレクトリは

- `lurcher` … Djangoの実際のPythonパッケージ
- `mainsite` … Djangoのmainsiteアプリケーションディレクトリ
- `src` … 静的ファイル（Image, JavaScript, CSS or SCSS）のソースディレクトリ

の3つです

### 基本的な開発の流れ

`lurcher` ディレクトリ内でHTMLテンプレートやテンプレートを表示するためのURLルーティングを記述し、HTMLテンプレート内で `static` ディレクトリに出力された静的ファイルを適宜参照しながら開発する流れとなります。

### 使用可能な補助技術

- Django
  * Webフレームワークの一種
  * [https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/django/](https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/django/)

- Sass(SCSS)
  * CSSをよりプログラミングに近い形で記述することを可能にした言語

- Bootstrap4
  * CSSフレームワークの一種
  * Bootstrapが提供するCSSをHTMLのクラスに適用するだけで、デザインが可能となる