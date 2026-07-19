# Copilot Instructions — 教育データ分析 (Copilot CLI + Jupyter + Jupyter MCP)

> このファイルは **GitHub Copilot CLI が本リポジトリで作業する際の共通ルール** を定義します。
> 対象は「ノンプログラマーの大学教職員」向け教育データ分析ワークフローです。

---

## 1. プロジェクトの目的

- 大学教職員（教務・IR・学修支援・情報基盤）が **Python コードを書かずに** 自然言語だけで教育データを分析できる状態を再現する。
- すべての操作は **GitHub Copilot CLI → Jupyter MCP → Jupyter Notebook** の経路で行う。
- 講演用のスライド・デモが公開再現可能であることを最優先する。

---

## 2. 実験環境（変更する前に必ず確認）

| 層 | ソフトウェア | 現行版 |
|----|-------------|-------|
| OS | Windows 11 Pro 24H2 + WSL2 Ubuntu 24.04 | — |
| AI | GitHub Copilot CLI | 1.0.72 |
| NB | JupyterHub (TLJH) | 5.5.0 |
| — | JupyterLab / Notebook | 4.5.7 / 7.5.6 |
| — | Python | 3.12.3 |
| MCP | `jupyter-mcp-server` (Datalayer) | 1.0.4 |
| Lib | pandas / numpy / matplotlib / japanize-matplotlib | 2.3.3 / 2.5.1 / 3.10.8 / 1.1.3 |

**バージョンを変更した場合は `README.md` の対応表と本ファイルの両方を必ず更新すること。**

---

## 3. Jupyter MCP 接続手順

**必ず動的接続 (`connect_to_jupyter`) を使う。** MCP 設定ファイル方式は JupyterHub の redirect で失敗する。

```
1. TLJH の JupyterHub にログインし、ユーザーサーバーを起動
2. `?token=...` で発行された personal token を取得
3. Copilot CLI で以下を自然言語で依頼:
   「Jupyter サーバー http://localhost:8899 に token=<xxx> で接続して」
   → Copilot が `jupyter-connect_to_jupyter(url=..., token=...)` を呼ぶ
4. 続けて対象 notebook を `jupyter-use_notebook` でアクティブ化
```

**Notebook 保存先**: 各デモディレクトリ直下 (`demoNN_xxx/notebook.ipynb`)。cwd はそのディレクトリになるため、画像は `../assets/` で相対参照する。

---

## 4. 分析前チェックリスト（データを触る前に必ず作成）

新しい分析を始める際は、Copilot に **コード生成の前に** 以下 4 項目を書き出させる。`demoNN_xxx/README.md` に記録する:

| 項目 | 説明 |
|------|------|
| **問い (Question)** | 一文で明示。例: 「2005 年比で 2040 年の 18 歳人口は何割減か？」 |
| **予想 (Hypothesis)** | 数値付きで予想する。例: 「約 4 割減 (137→82 万人)」 |
| **反証条件 (Falsification)** | どのデータが得られたら予想が誤りだったと言えるか |
| **出典 (Source)** | 使う一次資料の URL とバージョン（例: 文科省 学校基本調査 令和 6 年確定値） |

**このステップを省略しないこと。** チェックリストがないまま生成されたグラフは循環論証やチェリーピッキングの温床になる。

---

## 5. 出典・数値の扱い

### 出典 URL 必須ルール
- すべての数値主張には **URL 付き一次資料** を付ける（`e-Stat`, `.go.jp`, `.ac.jp` を優先）
- 「各種 Web 記事」「〜と言われている」等の曖昧な引用は禁止
- 出典は `RESULTS.md` の末尾または本文中に `[[1]](#ref-1)` 形式で記載

### 数値の桁と丸め
- **原数値（例: 106.3 万）で計算** してから最終出力で丸める。丸め値 (106 万) 同士の計算は誤差増幅の原因
- 変化率は原数値ベースで再計算する（例: `+2.6%` は `27,000 / 1,063,000` から算出。丸め値割り算の `+2.8%` は不正確）
- 進学率など「3 年前中卒者数ベース」など **分母定義が非自明な指標** は必ず注記する

---

## 6. AI クロスモデル検証（Fact-check / Rubber-duck）

**Human-in-the-Loop より前に、必ず AI 同士のクロスモデル検証を挟む。**

| 検証 | 実施方法 | 期待出力 |
|------|---------|---------|
| **Fact-check** | 実行 LLM と **異なるモデル**（例: Claude Opus で生成 → GPT-5 系で検証）で数値・出典を突合 | CORRECT / NEEDS VERIFICATION / INCORRECT の 3 段階判定 |
| **Rubber-duck review** | 同じく別モデルに「循環論証・因果誇張・チェリーピッキング」を探させる | Critical / Important / Minor の重み付き指摘 |

**別セッションを起動する必要はない。** Copilot CLI の `task` 機能でモデルを指定してサブエージェントを起動すれば足りる（同一セッション内で完結）。

**結果は `review/fact-check.md` と `review/rubber-duck.md` に必ず保存する。**

---

## 7. グラフ作成規約（スライド埋め込み用）

| 項目 | ルール |
|------|-------|
| 日本語フォント | `import japanize_matplotlib` （IPAexGothic）。**絵文字 (🔺 等) は使わない** — フォントで欠落する。`▲` (ASCII 三角) を使う |
| アスペクト比 | hero 図版は **16:9** (`figsize=(13.33, 7.5)`) |
| DPI | 180 以上（プレゼン投影・PDF 印刷両対応） |
| カラーパレット | Microsoft Fluent: `#0078D4`(青) / `#107C10`(緑) / `#D13438`(赤) / `#FFB900`(黄) / `#605E5C`(灰) |
| 保存先 | プレゼン最適化版は `assets/slides/slideNN_<用途>.png` |
| 情報密度 | 1 図 1 メッセージ。凡例 6 項目以内、注釈は矢印で該当点を明示 |
| 出典表記 | `fig.text(0.02, 0.015, "出典: ...", fontsize=10, color=COL_GRAY)` |

---

## 8. デモディレクトリ構造（必ず守る）

```
demoNN_<slug>/
├── README.md       # 分析前チェックリスト（問い/予想/反証/出典）
├── prompts.md      # Copilot に投げたプロンプト全記録（時系列）
├── notebook.ipynb  # Copilot が生成・実行した Notebook
└── RESULTS.md      # 実行結果、予想との差分、fact-check 反映履歴
```

`prompts.md` と `notebook.ipynb` を分離するのは、再現時に **プロンプトの言い回しがそのままコピー可能** であることが目的（Notebook 内コメントに埋めない）。

---

## 9. Copilot CLI への依頼テンプレート

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

## 10. Git コミット規約

```
content: <概要>    # デモ本体（notebook / prompts / RESULTS）
docs: <概要>       # README, ドキュメント
data: <概要>       # デモ用データセット
review: <概要>     # クロスモデル検証結果
chore: <概要>      # スクリプト、環境ファイル
```

コミット末尾には `Co-authored-by: Copilot <...>` を付ける。

---

## 11. やってはいけないこと

- ❌ 一次資料を確認せず AI の生成値をそのまま数値主張として使う
- ❌ 分析前チェックリストなしで `matplotlib.pyplot.plot()` を走らせる
- ❌ 絵文字 (🔺 ⚠️) をグラフ内テキストに使う（IPAexGothic で欠落）
- ❌ prompts.md を残さず notebook だけコミットする（再現不可になる）
- ❌ fact-check / rubber-duck をスキップして人間レビューに直行する
- ❌ Jupyter MCP 接続を config file 方式で試みる（JupyterHub redirect で失敗する）

---

**最終更新**: 2026-07-20 / Session bb0f192 → d441922
