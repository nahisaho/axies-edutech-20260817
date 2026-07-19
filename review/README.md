# AI クロスモデル検証結果

本ディレクトリには、4 デモの再実験成果物に対して**別 LLM (GPT-5.6-Sol)** をサブエージェント
として起動し、fact-check と rubber-duck review を実施した結果を保管しています。

「同一セッション内で別モデルを使えば、別セッション化しなくても独立した AI 視点で
レビューできる」という運用を実証した記録です。

## ファイル

| File | 内容 |
|------|------|
| [`fact-check.md`](./fact-check.md) | GPT-5.6-Sol による 37 件の数値主張の一次資料照合 |
| [`rubber-duck.md`](./rubber-duck.md) | GPT-5.6-Sol による非プログラマー聴衆視点の論理・表現レビュー |

## 発見の要約

### Fact-check (37 claims)

- ✅ CORRECT: 32
- ⚠️ NEEDS VERIFICATION: 2 (DEMO 2 分母定義差、DEMO 4 AI 応答内の粗さ)
- ❌ INCORRECT: 3
  - DEMO 1: `+2.8%` は丸め値ベース → `+2.6%` (原数値ベース) に差し戻し
  - DEMO 1: `2007 生まれ` → `2006 生まれ` (2025 年に 18 歳になる世代は主に 2006 年出生)
  - DEMO 4: AI 応答内「2040 年代後半 70 万人以下」は社人研 R5 と不整合 (実際は 70 万人台)

### Rubber-duck (5 Critical + 6 Important)

- Critical #1: **DEMO 3 の循環論証** — 入力プロンプトで指定した分布を "発見" と主張する構造
  → 「地図可視化技術デモ + 合成データ」と再フレーミング
- Critical #2: **DEMO 2 の算術差** — 63.3 ÷ 106 ≠ 59.1% (分母定義差)
  → Fact-check メモに定義差の説明を追加、因果表現を弱める
- Critical #3: **DEMO 1 の予想/反証条件不整合** → 反証条件節を「長期 vs 単調」に分けて明示
- Critical #4: **再現性のためのデータ CSV 不足** → 一部対応、残りは今後の TODO
- Critical #5: **DEMO 4 仮想線とモデル一般化** → 「架空シナリオ」明示、「単一観測に留める」修正

## 教訓

1. **クロスモデル検証は AI 分析の信頼性を実質的に高める**
   - 単一モデルでは +2.8% を "正確な訂正" と判断してしまうが、別 LLM が原数値ベース検算を提示
2. **AI が事実訂正応答を返しても、その代替数値も検算対象**
   - DEMO 4 で Claude Opus 4.7 は前提を訂正したが、代替として提示した「70 万人以下」自体が
     誤り → fact-check の対象範囲は AI が発した全ての数値
3. **同一セッション内サブエージェント運用の実用性**
   - `task` tool の `model` パラメータで別 LLM を起動 → 別セッション化不要
   - ユーザー確認済み方針として user memory に保存

## 実施日時・環境

- 実施日: 2026-07-20
- Reviewer model: GPT-5.6-Sol (via task tool subagent)
- Reviewee model: Claude Opus 4.7
- 環境: WSL2 Ubuntu 24.04.4 / GitHub Copilot CLI 1.0.72
