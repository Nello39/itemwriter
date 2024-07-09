# itemwriter
アイテムページを手打ちするのは大変なのでプログラムを組んで半自動化させました。
複数の項目が存在する場合、(ステータスや素材アイテムが複数ある場合)それぞれの項目の間に半角スラッシュ"/"を挿入してください。
itemwriter.pyではなく、test.pyがそれになります。
## 実行例
![image](https://github.com/Nello39/itemwriter/assets/160375936/04ef691e-e899-4dc6-8fba-55b1a1c0a084)
```返り値
|&attachref(item/テストアイテム.webp,60x60);&br;テストアイテム|9999|+10% やる気&br;+1% 根性|パッシブ‐テスト能力&br;Wikiの編集に協力すると特殊能力が手に入る|&attachref(item/やる気.webp,35x35);&attachref(item/根性.webp,35x35);&attachref(item/勇気.webp,35x35);|
```
![image](https://github.com/Nello39/itemwriter/assets/160375936/a20b108e-b2ed-437d-b5db-3ff42746bd10)

画像は[王者荣耀官方网站-腾讯游戏](https://pvp.qq.com/cp/a20220914wza/)より局内道具タブで画像をダウンロードした後、[item への添付 - 王者栄耀 オナーオブキングス JP Wiki*](https://wikiwiki.jp/hokwiki/?cmd=attach&page=item)に添付してください。ファイル名は原則「日本語武器名.拡張子」にしてください。中国語名や英語名の名前を用いないでください。
各ヒーロページは画像数が少ないためリンク直張り画像でもよかったですが、これは一覧ページになるのでページを軽量化するためにWikiへの画像アップロードをお願いしてもらっています。

後は、ページの中身を見てどうすればいいのか考えてください。間違った編集については管理人の方で発見次第勝手に修正するので気を張らずに編集をお願い致します。
