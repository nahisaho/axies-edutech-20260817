# Copilot Instructions — 教育データ分析 (Copilot CLI + Jupyter + Jupyter MCP)

> このファイルは **GitHub Copilot CLI が本リポジトリで作業する際の共通ルール** を定義します。
> 対象は「ノンプログラマーの大学教職員」向け教育データ分析ワークフローです。

---

## 0. セキュリティ最優先ルール（違反した瞬間に危険）

本リポジトリは **公開 GitHub リポジトリ** です。以下は例外なく守ってください。

| 禁止事項 | 代替 |
|---------|------|
| Jupyter トークンをそのまま `prompts.md` / Notebook セル / ログに書く | 必ず `<JUPYTER_TOKEN_REDACTED>` にマスクして記録 |
| Copilot への依頼メッセージに生トークンを含める | 依頼時のみ入力し、記録は伏せ字化 |
| 認証済み URL（`?token=...` 付き）をコミット | クエリ文字列を除去してから貼る |
| 個人メール・学籍番号・成績等の実データを push | 合成データまたは十分な匿名化を経てから |

**コミット前チェック**（毎回実行）:

```bash
git diff --cached | grep -Ei 'token=|password|apikey|@[a-z0-9.-]+\.(ac|com|jp)'
```

漏洩に気づいたら **即座にトークンを失効** し（JupyterHub の Token ページで revoke）、履歴書き換えを検討してください。

---

## 1. プロジェクトの目的

- 大学教職員（教務・IR・学修支援・情報基盤）が **Python コードを書かずに** 自然言語だけで教育データを分析できる状態を再現する。
- **Notebook のセル作成・Python 実行・結果取得** は Copilot CLI から Jupyter MCP 経由で行う。
  - README 編集・Git 操作・fact-check ドキュメント作成などは通常のシェル/エディタ操作。
- 講演用のスライド・デモが公開再現可能であることを最優先する。

---

## 2. 実験環境（変更する前に必ず確認）

| 層 | ソフトウェア | 本リポジトリ検証時のバージョン |
|----|-------------|------------------------------|
| OS | Windows 11 Pro 24H2 + WSL2 Ubuntu 24.04 | — |
| AI | GitHub Copilot CLI | 1.0.72 |
| NB | JupyterHub (TLJH) | 5.5.0 |
| — | JupyterLab / Notebook | 4.5.7 / 7.5.6 |
| — | Python | 3.12.3 |
| MCP | `jupyter-mcp-server` (Datalayer) | 1.0.4 |
| MCP補助 | `jupyter-collaboration`, `jupyter-server-ydoc`, `pycrdt` | Notebook 側に導入必須 |
| Lib | pandas / numpy / matplotlib / japanize-matplotlib | 2.3.3 / 2.5.1 / 3.10.8 / 1.1.3 |

**バージョンを変更した場合は本ファイルと `README.md` の両方を必ず更新すること。**
**上記は検証済み構成であり、他バージョンでの動作は保証しません。**

---

## 3. Jupyter MCP セットアップ手順

### 3-1. Jupyter 側（TLJH ユーザー環境）に拡張を導入

Datalayer 版 `jupyter-mcp-server` は Notebook のリアルタイム編集に `jupyter-collaboration` 系拡張を要求します。**TLJH のユーザー環境**（`sudo -E /opt/tljh/user/bin/pip`）に導入してください（Hub 環境ではない点に注意）:

```bash
sudo -E /opt/tljh/user/bin/pip install \
    jupyter-collaboration jupyter-server-ydoc pycrdt
sudo tljh-config reload
```

導入後、JupyterLab を開き Notebook が普通に開閉できることを目視確認。

### 3-2. Copilot CLI に MCP サーバーを登録

```bash
copilot mcp add jupyter -- uvx jupyter-mcp-server@1.0.4
copilot mcp list   # jupyter が enabled と表示されればOK
```

登録後は `~/.copilot/mcp-config.json` に自動追記されます。

### 3-3. Jupyter トークンを発行（都度）

**環境変数への固定保存は禁止。都度発行・都度失効。**

1. JupyterHub にログイン → 右上メニュー **"Token"** または `https://<hub>/hub/token`
2. "Add new token" で **短期スコープ**（例: 1 hour）で発行
3. 表示されたトークンを安全な場所（1Password 等）に一時保存

### 3-4. Copilot CLI から接続（推奨: 動的接続）

Copilot に以下を自然言語で依頼します（**プロンプトに生トークンが残らないよう注意**）:

> Jupyter サーバーに接続してください。URL とトークンは対話で聞いてください。

Copilot が対話的にプロンプトすれば、履歴に残さず接続できます。ツール呼び出しは実際には:

```
jupyter-connect_to_jupyter(
    jupyter_url="https://<hub>/user/<username>/",
    jupyter_token="<token>",
    provider="jupyter"
)
```

**引数名は `jupyter_url` / `jupyter_token` です**（`url` / `token` ではない）。

続けて `jupyter-use_notebook` で対象 Notebook をアクティブ化。

### 3-5. 疎通確認

```bash
curl -H "Authorization: token <token>" \
    https://<hub>/user/<username>/api/contents
```

`200 OK` が返れば接続情報は正常です。

### なぜ config file 方式を使わないか（本リポジトリの検証条件下で）

TLJH の `/user/<username>/` プロキシ経由で **セッション redirect が挟まる** ため、Datalayer 版が期待する Direct API アクセスに失敗するケースを検証時に観測しました。動的接続 API を用いれば回避できます。オンプレの素の Jupyter Server では config file 方式で問題なく動きます。**環境依存の回避策**であって、公式非推奨ではありません。

---

## 4. Notebook 内の画像保存先

Notebook の cwd は各デモディレクトリ (`demoNN_xxx/`) になります。リポジトリ直下の `assets/` に保存するため、**相対パス `../assets/`** を使ってください:

```python
# デモ実行用の画像（demo01/notebook.ipynb 内）
plt.savefig("../assets/demo01_18sai_jinkou.png", dpi=150, bbox_inches="tight")
```

スライド埋め込み用のプレゼン最適化 PNG は、Notebook からでも別スクリプトからでも同じ相対パスで参照:

```python
# 単発スクリプト（scripts/generate_slide_charts.py）は
# リポジトリ直下から実行するので "assets/slides/..." で保存
fig.savefig("assets/slides/slide28_demo1_hero.png", ...)
```

Notebook から Slide 用 PNG を作る場合は `../assets/slides/...`。**cwd を意識してパスを分けてください。**

---

## 5. 分析前チェックリスト（データを触る前に必ず作成）

新しい分析を始める際は、Copilot に **コード生成の前に** 以下 4 項目を書き出させ、`demoNN_xxx/README.md` に記録する:

| 項目 | 説明 |
|------|------|
| **問い (Question)** | 一文で明示。例: 「2005 年比で 2040 年の 18 歳人口は何割減か？」 |
| **予想 (Hypothesis)** | 数値付きで予想する。例: 「約 4 割減 (137→82 万人)」 |
| **反証条件 (Falsification)** | どのデータが得られたら予想が誤りだったと言えるか |
| **出典 (Source)** | 使う一次資料の URL・発行主体・調査名・公表日・表番号 |

**このステップを省略しないこと。** チェックリストがないまま生成されたグラフは循環論証やチェリーピッキングの温床になる。

---

## 6. 出典・数値の扱い

### 6-1. 一次性の判定

「ドメインが `.go.jp` / `.ac.jp` だから一次資料」とは限りません。以下 5 点をセットで確認:

- 発行主体（政府省庁・研究機関自体か、それとも転載サイトか）
- 調査名称（例: 「学校基本調査」）
- 公表日（速報値 / 確定値の別を含む）
- 表番号または該当ページ URL
- 原データか派生値か

### 6-2. 数値の分類と扱い

すべての数値は以下 4 カテゴリに分類し、`RESULTS.md` に明示してください:

| 分類 | 例 | 記録すべき情報 |
|------|-----|--------------|
| 一次資料転載値 | 学校基本調査の入学者数 | 出典 URL + 表番号 + 公表日 |
| 派生値（計算） | 変化率 `+2.6%` | 入力値・計算式・計算に使ったコードセル |
| 推計値 | 社人研 R5 中位推計 | 推計モデル名・公表日 |
| 合成・説明用データ | DEMO 3 の都道府県別値 | **「合成」明示** + 参考にした一次資料 |

### 6-3. 計算精度

- 一次資料に整数値（人数など）がある場合は **整数値のまま計算** する
- 千人単位・万人単位に丸めた値同士で変化率を計算しない（誤差増幅の原因）
- 表示精度を超える小数点以下の変化率を出さない（`106.3 万 → 108.9 万` から `+2.4489...%` は誤り、`+2.6%` 程度に留める）
- 進学率など **分母定義が非自明な指標**（学校基本調査は 3 年前中卒者数ベース）は必ず注記

---

## 7. AI クロスモデル検証 + 人間レビュー

**両方を公開前に実施。順序は固定しません。** ただし、以下は必ず **人間レビュー必須ゲート**:

- 個人情報の混入可能性
- 政策的解釈・提言
- 特定機関・個人への影響が及ぶ内容

### 7-1. AI クロスモデル検証

実行 LLM と **異なるモデル** で検証します。Copilot CLI の `task` 機能でサブエージェントを起動すれば **同一セッション内で完結**（別セッション化不要）。

| 検証 | 期待出力 |
|------|---------|
| **Fact-check** | 数値・出典の突合。CORRECT / NEEDS VERIFICATION / INCORRECT の 3 段階判定 |
| **Rubber-duck review** | 循環論証・因果誇張・チェリーピッキング等。Critical / Important / Minor の重み付き |

**注意**: 同一セッション内サブエージェントはコンテキストを共有し得るため、完全独立検証ではありません。重大判断は人間レビューで補完してください。

### 7-2. レビュー結果の保存

上書きされないよう、**デモ別・日付・対象コミット SHA** を含めてください:

```
review/demo01/2026-07-20-fact-check-<short-sha>.md
review/demo01/2026-07-20-rubber-duck-<short-sha>.md
```

集約が必要な場合は `review/README.md` にインデックスを作成。

---

## 8. グラフ作成規約（スライド埋め込み用）

| 項目 | ルール |
|------|-------|
| 日本語フォント | `import japanize_matplotlib` （IPAexGothic）。**絵文字 (🔺 ⚠️ 等) は使わない** — フォントで欠落する。代わりに `▲`（Unicode U+25B2, IPAexGothic で表示可能な三角記号）を使う |
| アスペクト比 | hero 図版は **16:9** (`figsize=(13.33, 7.5)`) |
| DPI | 180 以上 |
| カラーパレット | Microsoft Fluent: `#0078D4`(青) / `#107C10`(緑) / `#D13438`(赤) / `#FFB900`(黄) / `#605E5C`(灰) |
| 保存先 | プレゼン最適化版は `assets/slides/slideNN_<用途>.png`（Notebook からは `../assets/slides/...`） |
| 情報密度 | 1 図 1 メッセージ。凡例 6 項目以内、注釈は矢印で該当点を明示 |
| 出典表記 | `fig.text(0.02, 0.015, "出典: ...", fontsize=10, color="#605E5C")` |

---

## 9. デモディレクトリ構造（必ず守る）

```
demoNN_<slug>/
├── README.md       # 分析前チェックリスト（問い/予想/反証/出典）
├── prompts.md      # Copilot に投げたプロンプト全記録（トークン等はマスク）
├── notebook.ipynb  # Copilot が生成・実行した Notebook
└── RESULTS.md      # 実行結果、予想との差分、fact-check 反映履歴、数値分類（§6-2）
```

`prompts.md` と `notebook.ipynb` を分離するのは、再現時に **プロンプトの言い回しがそのままコピー可能** であることが目的。

---

## 10. Copilot CLI への依頼テンプレート

新しい分析を依頼するときは、以下のメタプロンプトを使うと精度が上がる:

```
これから私の目的を伝えます。目的達成のために必要な情報をあなたは
1 問 1 答で私に質問してください。すべての情報がそろったら、
最適なプロンプトを自分で組み立てて実行してください。

目的：<例> 過去 30 年の日本の 18 歳人口の推移を可視化し、
社人研推計を接続して 2050 年までの見通しを 1 枚のグラフにまとめる。
```

**1 問 1 答を守らせる**ことで、コンテキスト不足による幻覚を防ぐ。

---

## 11. Git コミット規約

```
content: <概要>    # デモ本体（notebook / prompts / RESULTS）
docs: <概要>       # README, ドキュメント
data: <概要>       # デモ用データセット
review: <概要>     # クロスモデル検証結果
chore: <概要>      # スクリプト、環境ファイル
```

AI 支援の開示として **コミット本文または PR 説明** に「本コミットは GitHub Copilot CLI との対話で作成」等を明記してください。`Co-authored-by:` トレーラーを使う場合は **実在するメールアドレス**（自分の GitHub 登録アドレスまたは Copilot の noreply アドレス）を使うこと。プレースホルダー `<...>` のままコミットしないでください。

---

## 12. やってはいけないこと（禁止事項の集約）

- ❌ Jupyter トークン・認証済み URL をプロンプト/Notebook/コミットに残す
- ❌ 一次資料を確認せず AI の生成値をそのまま数値主張として使う
- ❌ 分析前チェックリストなしでコード生成・実行に進む
- ❌ 絵文字 (🔺 ⚠️ 等) をグラフ内テキストに使う（IPAexGothic で欠落）
- ❌ `prompts.md` を残さず Notebook だけコミットする（再現不可）
- ❌ AI レビューだけで公開する（人間レビュー必須ゲートを飛ばす）
- ❌ MCP ツール引数名を推測で書く（`jupyter_url` / `jupyter_token` を確認）
- ❌ 合成データ・派生値を一次資料と混同して表示する
- ❌ Notebook cwd と リポジトリ直下 cwd を混同したパス指定
- ❌ 個人情報・成績等をマスキングなしで push

---

**最終更新**: 2026-07-20（rubber-duck review 反映版）
**検証済み構成**: 本ファイル §2 のバージョン組み合わせ。他バージョンは未検証。
