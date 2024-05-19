# <ruby>masumani<rp>(</rp><rt>ますまにゴミさっさと滅ぶべきてかなんでますまにイキってるの？中学生だから？陰キャだから？とりあえずなんでもいいや！ｗとりあえずこのプロジェクトを完成させよ！ｗ</rt><rp>)</rp></ruby>
ますまにのアンチとして<ruby>活動<rp>(</rp><rt>かつどう</rt><rp>)</rp></ruby>するゴミサイト！
## <ruby>How to build<rp>(</rp><rt>ハウトゥービルド</rt><rp>)</rp></ruby>
<ruby>仮想環境<rp>(</rp><rt>かそうかんきょう</rt><rp>)</rp></ruby>を<ruby>作<rp>(</rp><rt>つく</rt><rp>)</rp></ruby>る<ruby>方法<rp>(</rp><rt>ほうほう</rt><rp>)</rp></ruby>もありますがこの<ruby>README.md<rp>(</rp><rt>りーどみー.まーくだうん</rt><rp>)</rp></ruby>は<ruby>解説<rp>(</rp><rt>かいせつ</rt><rp>)</rp></ruby>しません。
### 0. <ruby>必要<rp>(</rp><rt>ひつよう</rt><rp>)</rp></ruby>なもの
- <ruby>Windows<rp>(</rp><rt>うぃんどうず</rt><rp>)</rp></ruby>か<ruby>Mac<rp>(</rp><rt>まっく</rt><rp>)</rp></ruby>か<ruby>Linux系<rp>(</rp><rt>りなっくすけい</rt><rp>)</rp></ruby><ruby>OS<rp>(</rp><rt>オペレーティングシステム</rt><rp>)</rp></ruby>が入ったパソコン
### 1. <ruby>Python<rp>(</rp><rt>ぱいそん</rt><rp>)</rp></ruby>をインストール
<ruby>Python<rp>(</rp><rt>ぱいそん</rt><rp>)</rp></ruby> 3.11がおすすめ
### 2. このリポジトリをクローン
フォークじゃないよ。
```bash
git clone https://github.com/nennneko5787/masumani.git
```
### 3. <ruby>環境変数<rp>(</rp><rt>かんきょうへんすう</rt><rp>)</rp></ruby>を<ruby>設定<rp>(</rp><rt>せってい</rt><rp>)</rp></ruby>
<ruby>適当<rp>(</rp><rt>てきとう</rt><rp>)</rp></ruby>に<ruby>環境変数<rp>(</rp><rt>かんきょうへんすう</rt><rp>)</rp></ruby>を<ruby>定義<rp>(</rp><rt>ていぎ</rt><rp>)</rp></ruby>しましょう。
.envファイルを<ruby>作<rp>(</rp><rt>つく</rt><rp>)</rp></ruby>ってもいいかもしれません。
```ini
dsn=(データベースのDSN)
```
### 4. <ruby>設定<rp>(</rp><rt>せってい</rt><rp>)</rp></ruby>を変更
config.ymlファイルを<ruby>弄<rp>(</rp><rt>いじ</rt><rp>)</rp></ruby>って<ruby>色々<rp>(</rp><rt>いろいろ</rt><rp>)</rp></ruby>と<ruby>設定<rp>(</rp><rt>せってい</rt><rp>)</rp></ruby>を<ruby>変<rp>(</rp><rt>か</rt><rp>)</rp></ruby>えましょう。
### 5. <ruby>起動<rp>(</rp><rt>きどう</rt><rp>)</rp></ruby>
<ruby>最後<rp>(</rp><rt>さいご</rt><rp>)</rp></ruby>に、<ruby>以下<rp>(</rp><rt>いか</rt><rp>)</rp></ruby>のコマンドで<ruby>起動<rp>(</rp><rt>きどう</rt><rp>)</rp></ruby>できます。
```bash
uvicorn main:app --host 127.0.0.1 --port <ポート>
```