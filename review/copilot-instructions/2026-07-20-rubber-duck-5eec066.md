# Rubber-duck Review — copilot-instructions.md (2026-07-20)

- **対象**: `.github/copilot-instructions.md` @ commit `5eec066`
- **実行 LLM**: Claude Opus 4.7
- **検証 LLM**: GPT-5.6-Sol (via `task` sub-agent, 同一セッション内)
- **手法**: rubber-duck review（バグ・論理矛盾・設計欠陥・自己矛盾・幻覚検出）

## サマリ

| 重み | 件数 | 対応状況 |
|------|-----|---------|
| Critical | 5 | ✅ 全件反映（次コミット） |
| Important | 8 | ✅ 全件反映 |
| Minor | 2 | ✅ 反映 |

## Critical 指摘と対応

### C1: Jupyter トークンが公開リポジトリに漏洩する構造
- **問題**: 接続プロンプトに生トークンを含め、`prompts.md` として全記録コミット
- **対応**: §0「セキュリティ最優先ルール」新設。マスキング必須化、`git diff --cached | grep` チェック、失効手順記載

### C2: MCP サーバー登録手順が欠落
- **問題**: `connect_to_jupyter` は MCP 登録済み前提だが、`copilot mcp add` の記述なし
- **対応**: §3-2 に登録コマンド追加

### C3: JupyterHub URL / トークン取得手順が不正確
- **問題**: `?token=...` は「発行」機構ではない。TLJH のユーザーサーバー URL 構造 (`/user/<username>/`) を無視
- **対応**: §3-3 に `/hub/token` からの短期発行手順、§3-4 で正しい URL 構造、§3-5 で疎通確認 curl を追加

### C4: `connect_to_jupyter` の引数名が誤り
- **問題**: 実際は `jupyter_url` / `jupyter_token` / `provider`。`url` / `token` は動かない
- **対応**: §3-4 で正しい引数名に修正 + §12 禁止事項に追加

### C5: Jupyter 側必須拡張パッケージが未記載
- **問題**: `jupyter-collaboration` 等が Notebook 側に必要だが記載なし。TLJH ユーザー環境と Hub 環境の分離も未言及
- **対応**: §2 表に追加、§3-1 に TLJH ユーザー環境への導入コマンド明記

## Important 指摘と対応

### I6: config file 方式一律禁止の根拠不明
- **対応**: §3 末尾に「なぜ config file 方式を使わないか（本リポジトリの検証条件下で）」節を追加。TLJH プロキシ redirect 由来の環境依存であること、素の Jupyter Server では config 方式 OK と明記

### I7: 「すべての操作が MCP 経由」が README/Git 操作と矛盾
- **対応**: §1 で「Notebook セル作成・Python 実行・結果取得」に限定と明記

### I8: 画像保存パスの自己矛盾
- **対応**: §4 新設。Notebook cwd 前提 (`../assets/...`) と スクリプト cwd 前提 (`assets/...`) を分けて明記

### I9: 「原数値 106.3 万」も丸め値
- **対応**: §6-3 で整数値保持・精度超過禁止を明記

### I10: AI レビューを人間より前に必須化する順序固定
- **対応**: §7 冒頭で「両方を公開前に実施。順序は固定しません」に変更。個人情報・政策解釈は人間必須ゲート化

### I11: review 保存先の上書き問題
- **対応**: §7-2 で `review/demoNN/YYYY-MM-DD-*-<short-sha>.md` 形式を明示

### I12: コミットトレーラー `<...>` が無効メール
- **対応**: §11 で「実在するメールアドレスを使う」明記、プレースホルダー禁止

### I13: 合成値 vs 転載値 vs 派生値の区別なし
- **対応**: §6-2 で 4 分類を導入

## Minor 指摘と対応

### M14: `▲` は ASCII ではなく Unicode U+25B2
- **対応**: §8 で「Unicode U+25B2, IPAexGothic で表示可能な三角記号」に修正

### M15: `.ac.jp` = 一次資料 は不正確
- **対応**: §6-1 で発行主体・調査名・公表日・表番号・原/転載の 5 点確認ルールに置換

## 総評（GPT-5.6-Sol による）

> ブロッキング問題があります。特に「トークンをプロンプトへ入力し、その全記録をコミットする」構造と、MCP 登録・JupyterHub URL・引数名の不備は、公開デモ前に修正が必要です。

→ **すべて反映済み**。修正版コミットで公開可能な状態になります。
