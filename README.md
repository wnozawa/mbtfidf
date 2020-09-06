# README

## ファイル説明
- AllQA.csv
	Q&Aのリスト。１列目にQ、２列目にA。

- Procfile
	heroku上の実行方法を指定するファイル。

- README.md
	このREADME。

- TFIDF.py
	ユーザーからのクエリをベクトルに変換し類似度を算出するモジュール。main.pyで使用。

- get_tfidf_index.py
	herokuでの実行前の準備として、Q&Aリストの各QをTF-IDFベクトル化するファイル。index_tfidf.index、maqa.dict、tfidf.modelを生成する。heroku上では使用されない。

- index_tfidf.index
	Q&Aの各Qのベクトルを格納。これを使って類似度を計算する。get_tfidf_index.pyにより生成。

- main.py

- maqa.dict
	Q&Aに出現する単語のリスト。get_tfidf_index.pyにより生成。

- requirements.txt
	herokuで利用するPythonモジュールを指定するファイル。

- runtime.txt
	herokuで利用するPythonのバージョンを指定するファイル。

- tfidf.model
	TF-IDFを算出するモデル。get_tfidf_index.pyにより生成。



## 使い方
大雑把には、HerokuにdeployしてLINE messaging APIに繋げばOK。以下はその手順です。

1. LINE messaging APIでチャネルを作成。（参照：https://developers.line.biz/ja/docs/messaging-api/getting-started/）

2. Herokuでアプリを作成。Settingsタブ > Config Vars で環境変数を２つ設定。それぞれ、[LINE Developersコンソール](https://developers.line.biz/console/)でチャネルアクセストークン、チャネルシークレットを確認して入力。
	1. LINE_BOT_CHANNEL_TOKEN
	2. LINE_BOT_CHANNEL_SECRET

3.  Herokuの**Resources**タブの**Add-ons**の入力欄に「Postgres」と入力し、ドロップダウンで出てくるHeroku Postgresを追加。

4.  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)をインストールし、ログイン。
    ```
    $ heroku login
    ```
5.  このリポジトリをgit cloneしたディレクトリから以下の操作。（注：`{HEROKU_APP_NAME}`は手順2で指定したアプリ名です。）
    ```
    $ git add .
	$ git commit -a "initialize"
	$ heroku git:remote -a {HEROKU_APP_NAME}
	$ git push heroku master
    ```
6. Heroku Postgresにmessagelogという名前の３列のテーブルを追加。
    ```
    $ heroku pg:psql
	$ {HEROKU_APP_NAME}::DATABASE=> CREATE TABLE messagelog (message TEXT, response TEXT, time TEXT);
    ```
7.  [LINE Developersコンソール](https://developers.line.biz/console/)で、Messaging APIチャネルの［**Messaging API設定**］タブをクリックし、２つの操作。
	-  「`https://{HEROKU_APP_NAME}.herokuapp.com/callback`」というURL形式で、Webhook URLを入力します。  
	-  ［**Webhookの利用**］を有効にします。

8. [LINE Developersコンソール](https://developers.line.biz/console/)のチャネル設定から［Messaging API設定］タブにあるQRコードを読み取って、ボットが関連づけられているLINE公式アカウントを友だち追加し、動作を確認。

以上で完了です。
