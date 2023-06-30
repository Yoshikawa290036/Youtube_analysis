# Youtube Analysis
Hololiveのライブ配信から，特定の期間のコメント情報を抽出して解析する．

## 環境構築
* [Chrome Driverのインストール方法](https://zenn.dev/ryo427/articles/7ff77a86a2d86a)
などを参考に，正しいバージョンのChrome Driverをインストールする．
* python3をインストールし，下記のライブラリーを導入する．cmdで以下のコマンドを実行する．
```
> python -m pip install beautifulsoup4 selenium yt-dlp pytchat moviepy
```

## 実行
go.batファイルのbeとenを，抽出したい期間に設定する．
cmdで以下のコマンドを実行する．
```
> go.bat
```
実行したら，しばらくプログラムの終了を待つ．

プロセスが終了している or それぞれのフォルダーの中にLiver_data.pickleファイルができている or .logファイルの最終行に「FINISHED !!!!!!!!」が表示されていれば，プログラムが終了している．

プログラムの終了後，analysis.pyを実行する．
```
> python analysis.py
```
