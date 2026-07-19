# AXIES 2026 講演デモ — 再現アーカイブ

> **講演**: 「ノンプログラマーのための教育データ利活用入門：GitHub Copilot + Jupyter MCP ではじめる教育データ分析」
> **イベント**: AXIES 教育技術開発部会 第 23 回研究会
> **日時**: 2026 年 8 月 17 日
> **発表者**: nahisaho

本リポジトリは、講演で実演する 4 つのデモを **公開再現可能な形式** で保存したものです。
すべてのデモは **GitHub Copilot CLI + Jupyter MCP Server** を用いて、Python コードを一切手書きせず、**自然言語プロンプトのみ** で実行しました。

## デモ一覧

| # | ディレクトリ | 内容 | 使用モデル |
|---|-------------|------|-----------|
| DEMO 1 | [`demo01_18sai_jinkou/`](./demo01_18sai_jinkou/) | 18 歳人口の推移 (1990-2050) 実測 + 推計 | Claude Opus 4.7 |
| DEMO 2 | [`demo02_shingaku_ritsu/`](./demo02_shingaku_ritsu/) | 進学率 × 18 歳人口 × 入学者数の 2 軸グラフ | Claude Opus 4.7 |
| DEMO 3 | [`demo03_pref_heatmap/`](./demo03_pref_heatmap/) | 47 都道府県別ヒートマップ | Claude Opus 4.7 |
| DEMO 4 | [`demo04_reverse_prompt/`](./demo04_reverse_prompt/) | 逆質問デモ (循環設計の自己批判) | Claude Opus 4.7 |
| Review | [`review/`](./review/) | Fact-check / Rubber-duck review 結果 | GPT-5 系 (cross-model) |
| Slides | [`assets/slides/`](./assets/slides/) | 講演スライド埋め込み用 PNG 図版 (8 枚, 16:9) | — |
| Scripts | [`scripts/`](./scripts/) | 図版再生成スクリプト | — |

## 実験環境

再実験時 (2026-07-20) の実測構成:

| 層 | ソフトウェア | バージョン |
|----|-------------|-----------|
| OS | Windows 11 Pro | 24H2 (Build 10.0.26200.8893) |
| ↓ | WSL2 Ubuntu | 24.04.4 LTS |
| ↓ | Linux Kernel | 6.18.35 (WSL2) |
| AI | **GitHub Copilot CLI** | **1.0.72** |
| — | Node.js / npm | 22.22.1 / 11.18.0 |
| NB | **JupyterHub (TLJH)** | **5.5.0** |
| — | JupyterLab / Notebook | 4.5.7 / 7.5.6 |
| — | Python | 3.12.3 |
| 🔗 | **jupyter-mcp-server** | **1.0.4** (Datalayer) |
| Lib | pandas / numpy | 2.3.3 / 2.5.1 |
| — | matplotlib / japanize-matplotlib | 3.10.8 / 1.1.3 |
| — | mcp / fastmcp | 1.26.0 / 3.2.0 |

## ワークフロー

各デモディレクトリには以下の 4 ファイルが含まれます:

1. **`README.md`** — デモの概要、分析前チェックリスト（問い・予想・反証条件・出典）
2. **`prompts.md`** — 使用した自然言語プロンプトの全記録
3. **`notebook.ipynb`** — Copilot が生成・実行した Jupyter ノートブック
4. **`RESULTS.md`** — 実行結果、予想との差分、fact-check メモ

## スライド埋め込み用 図版

講演スライド (16:9) にそのまま貼り付け可能なプレゼン最適化 PNG を [`assets/slides/`](./assets/slides/) に収録:

| ファイル | 用途 | スライド |
|---------|------|---------|
| `slide09_bignum_hero.png` | 137→82 万人 大数字対比 | Slide 9 事実① |
| `slide26_thumb_line.png` | 予想通り側 サムネ折れ線 | Slide 26 |
| `slide28_demo1_hero.png` | DEMO 1 18 歳人口推移 (hero) | Slide 28 |
| `slide28_delta_bars.png` | 減少ペース加速 棒グラフ | Slide 28 補助 |
| `slide31_demo2_hero.png` | 進学率上昇で相殺 2 軸グラフ | Slide 31 |
| `slide32_kpi_shingaku.png` | +7.6pt KPI 強調 | Slide 32 |
| `slide34_demo3_hero.png` | 47 都道府県ヒートマップ (合成) | Slide 34 |
| `slide37_demo4_hero.png` | 実データ vs 仮想線 | Slide 37 |

**デザイン仕様**: Microsoft Fluent カラーパレット (`#0078D4` / `#107C10` / `#D13438` / `#FFB900`)、IPAexGothic フォント、DPI 180。
**再生成**: `python scripts/generate_slide_charts.py`

## クロスモデル品質検証

すべてのデモは、実行 LLM (Claude Opus 4.7) とは異なるモデル (**GPT-5.6-Sol**) による Fact-check と Rubber-duck review を経ています。結果は [`review/`](./review/) 参照。

| 検証 | 対象 | 主な指摘と反映 |
|------|------|--------------|
| Fact-check | 37 claims | 3 件 INCORRECT を検出 → 全件修正済（`+2.8% → +2.6%`, 「2007 生まれ → 2006 生まれが約 3 万人多」等）|
| Rubber-duck | 5 Critical + 6 Important | Critical 全件対応済（DEMO 3 循環論証を「合成データによる可視化技術デモ」に再フレーミング等）|

## 出典

- 文部科学省 学校基本調査 令和 6 年 (2024) 確定値
  https://www.mext.go.jp/b_menu/toukei/chousa01/kihon/kekka/1268046.htm
- 国立社会保障・人口問題研究所 令和 5 年推計 (中位)
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp2023_ReportALL.pdf
- 日本私立学校振興・共済事業団 令和 7 年度 志願動向
  https://www.shigaku.go.jp/s_center_d_shigandoukou.htm

## ライセンス

- 本リポジトリのソースコード・ノートブック: **MIT License** (`LICENSE` 参照)
- 引用した公的統計データ: 各出典元の利用規約に従う

## Copilot CLI で本リポジトリを使う方（再現する方）向け

このリポジトリを clone して自分の環境で再現する場合、[`.github/copilot-instructions.md`](./.github/copilot-instructions.md) が **GitHub Copilot CLI の共通ルール** として自動読み込みされます。以下を含みます:

- Jupyter MCP の動的接続手順（config file 方式が JupyterHub で失敗する回避策）
- 分析前チェックリスト（問い / 予想 / 反証条件 / 出典）の必須化
- 出典 URL・原数値ベース計算・分母定義注記のルール
- AI クロスモデル検証（Fact-check + Rubber-duck）の実施方法
- スライド埋め込み用グラフのデザイン規約（16:9 / Fluent palette / IPAexGothic）
- デモディレクトリ構造とコミット規約
- やってはいけないこと 6 箇条

## 免責

デモ用の一部数値（特に DEMO 3 の都道府県別充足率）は **公開合成データ / デモ用近似値** を含みます。政策判断や学術発表に用いる場合は、必ず一次資料（私学事業団、e-Stat 等）で再検証してください。
