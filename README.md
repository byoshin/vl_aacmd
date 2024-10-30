# vl_aacmd

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 概要
声orコマンドでチャット欄にアスキーアートを送信するツールです

## ✨ ファイルの詳細
- vl_aacmd.py:
  本体　40分で書いたコード お片付けも最適化もなにもしてない
  ちなみに今の設定だと音声認識精度がわるいです
  よみとった文字列の中にワードが含まれたら実行とかにすれば精度良くなります
  でもめんどいから勝手にやってください

  あとrequirementsも作ってないのでimportから自力で探すなりで
- config.json:
  アスキーアート辞書　アスキーアート追加したいならここ
  ```bash
  {
    "name" : "特に存在意義はない",
    "vc" : "聞き取りたい音声のローマ字",
    "command" : "コマンドの文字列",
    "output" : "アスキーアートを追加したかったらここからぶちこんでください"
  },
  
  
  
- vl_aacmd.exe:
  .pyをexeにしたやつ githubだと重くて上げれなかったから自分のサイトに上げとくね
  https://drive.byoshin.net/vl_aacmd/vl_aacmd.exe
  使用する際はconfigを同じ階層に入れてね
  これでパソコン壊れたりBANされたりしても全部自己責任だよ

## 🚀 option
起動するときに引数つけるとチーム内に限定できます

```bash
vl_aacmd.exe --team
```

## help

なんかわかんないことあったら連絡してね
https://x.com/Byoshin5149
