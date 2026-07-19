# DEMO 1: 18 歳人口の推移 (1990-2050)

## 分析前チェックリスト

| 項目 | 内容 |
|------|------|
| **問い** | 日本の 18 歳人口は 1990-2050 でどう推移したか？ |
| **予想** | 全期間で単調減少しているだろう |
| **反証条件** | もし 2020 年以降が横ばい以上なら予想は誤り |
| **出典** | 文科省 学校基本調査 / 社人研 R5 推計 / 私学事業団 R7 志願動向 |

## 使用モデル・環境

- **AI モデル**: Claude Opus 4.7 (GitHub Copilot CLI 1.0.72 経由)
- **Notebook**: JupyterLab 4.5.7 + Python 3.12.3
- **接続**: jupyter-mcp-server 1.0.4
- **実行日時**: 2026-07-20

## 実行手順

1. `prompts.md` に記載の自然言語依頼を Copilot CLI に投入
2. Copilot が Jupyter MCP 経由で `notebook.ipynb` にセルを挿入・実行
3. 結果は `../assets/demo01_18sai_jinkou.png` に保存
4. 予想との差分は `RESULTS.md` に記録

## ファイル

- [`prompts.md`](./prompts.md) — 使用プロンプトの全記録
- [`notebook.ipynb`](./notebook.ipynb) — 実行済みノートブック
- [`RESULTS.md`](./RESULTS.md) — 実行結果と予想との差分
- [`../assets/demo01_18sai_jinkou.png`](../assets/demo01_18sai_jinkou.png) — 出力グラフ
