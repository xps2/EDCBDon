# EDCBDon
EDCBからMastodonでトートする

## 準備
### トークン
* token.ini.sampleを、token.iniにリネームする。
* token.iniを自分が使用しているインスタンスに合わせて変更する。
* `python edcbdon.py --token`を実行する。
* edcbdon_clientcred.secret, edcbdon_usercred.secretが作成されていることを確認する。
* token.iniは不要なので削除する。
### バッチ
* edcbdon.ini.sampleをedcbdon.iniにリネームする
* edcbdon.iniを自分が使用しているインスタンスに変更する。
* edcbdon_clientcred.secret, edcbdon_usercred.secret, edcbdon.py, edcbdon.iniを任意のディレクトリにコピーする。

## 実行方法
* PostRecStart.batなどに`python edcbdon.py "トートしたい内容"`を記述する。
