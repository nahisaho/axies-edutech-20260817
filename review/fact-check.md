# Fact-check Review (by GPT-5.6-Sol, 2026-07-20)

## Summary

- Total claims checked: 37
- CORRECT: 32
- NEEDS VERIFICATION: 2
- INCORRECT: 3

## Corrections Applied (2026-07-20)

以下の INCORRECT / NEEDS VERIFICATION 指摘を受け、ソースを修正しました:

1. **DEMO 1 Claim 5 (+2.8% → +2.6%)**: 丸め値ベースを原数値ベースに差し戻し、
   Notebook のグラフ注釈・RESULTS.md・slide-context-v1.2.md を更新
2. **DEMO 1 Claim 6 (2007 生まれ → 2006 生まれ)**: 出生数データを再確認し、
   2025 年 4 月に 18 歳になる世代 = 2006 年 4 月〜2007 年 3 月生まれ (主に 2006 年出生)
   と正確化
3. **DEMO 2 Claim 8**: 分母定義差 (3 年前中卒者数ベース) を RESULTS.md の Fact-check
   メモに追記し、「相殺」を因果ではなく記述的関係として説明
4. **DEMO 4 Claim 9 / 11**: AI 応答内の数値誤り (70 万人以下、100 万人前後) を、
   RESULTS.md の Fact-check メモに検証結果として追記。
   ※ AI 応答自体は verbatim 記録のため書き換えず、fact-check 注記で対応

## Detailed Findings

> [!NOTE]
> 関連する年次系列は、表全体を1件の claim として集計した。万人単位の値は、原数値を丸めた概数として判定している。

## DEMO 1

### Claim 1: 1990～2020年の18歳人口は 201、177、151、137、122、120、118万人
- Status: CORRECT
- Evidence: 文部科学省が公表する「18歳人口及び高等教育機関への入学者数・進学率等の推移」の概数と整合する。  
  https://www.mext.go.jp/b_menu/toukei/002/index.htm

### Claim 2: 2024年の18歳人口は106万人
- Status: CORRECT
- Evidence: 私学事業団の年度別18歳人口 1,063,247人を万人単位に丸めた値として妥当。文科省資料には定義の異なる「18歳人口」があるため、出典名を併記すると安全である。  
  https://www.shigaku.go.jp/files/shigan_doukouR7.pdf

### Claim 3: 2025年の18歳人口は109万人
- Status: CORRECT
- Evidence: 私学事業団「令和7年度 私立大学・短期大学等入学志願動向」は、令和7年度の18歳人口が前年度から約2.7万人増えたと説明しており、約109万人という丸め値と整合する。  
  https://www.shigaku.go.jp/files/shigan_doukouR7.pdf

### Claim 4: 2024→2025年に約3万人増加
- Status: CORRECT
- Evidence: 公式資料の「約2.7万人増」を万人単位で丸めれば「約3万人増」である。より厳密には「約2.7万人増」と書くのが望ましい。  
  https://www.shigaku.go.jp/files/shigan_doukouR7.pdf

### Claim 5: 2024→2025年の増加率は +2.8%
- Status: INCORRECT
- Evidence: 106万人と109万人という丸め後の値から計算した 2.83% であり、原数値ベースの比率ではない。私学事業団が示す増加幅約2.7万人と2024年度人口約106.3万人からは、おおむね **+2.5～2.6%** となる。発表では「約2.7万人（約2.6%）増」に修正すべきである。  
  https://www.shigaku.go.jp/files/shigan_doukouR7.pdf

### Claim 6: 一時増の原因は「2007年生まれ世代の出生数がわずかに多かったため」
- Status: INCORRECT
- Evidence: 出生数は2005年 1,062,530人、2006年 1,092,674人、2007年 1,089,818人であり、2007年は2006年より少ない。増加の主因は、学年コーホートに多く含まれる**2006年出生数が2005年より約3万人多いこと**である。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 7: 2030～2050年の18歳人口は 96、89、82、78、74万人
- Status: CORRECT
- Evidence: 社人研「日本の将来推計人口（令和5年推計）」の出生中位・死亡中位推計を万人単位に丸めた系列と整合する。推計は各年10月1日現在であることを注記するとよい。  
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp

### Claim 8: 1990年201万人から2050年74万人へ約63%減
- Status: CORRECT
- Evidence: `(201 - 74) / 201 = 63.18%` で、約63%減は正しい。

### Claim 9: 2005→2020年は19万人減
- Status: CORRECT
- Evidence: `137 - 118 = 19` 万人。

### Claim 10: 2020→2040年は36万人減で、年平均の減少ペースも速い
- Status: CORRECT
- Evidence: `118 - 82 = 36` 万人。年平均では約1.8万人減で、2005→2020年の約1.27万人減を上回る。

### Claim 11: 2040年82万人は2005年137万人の59.9%
- Status: CORRECT
- Evidence: `82 / 137 × 100 = 59.85%`。

## DEMO 2

### Claim 1: 2010年の大学（学部）進学率は50.9%
- Status: CORRECT
- Evidence: 文部科学省「学校基本調査」の大学（学部）進学率と一致する。  
  https://www.mext.go.jp/b_menu/toukei/002/index.htm

### Claim 2: 2015年の大学（学部）進学率は51.5%
- Status: CORRECT
- Evidence: 文部科学省「学校基本調査」の大学（学部）進学率と一致する。  
  https://www.mext.go.jp/b_menu/toukei/002/index.htm

### Claim 3: 2024年の大学（学部）進学率は59.1%
- Status: CORRECT
- Evidence: 令和6年度学校基本調査確定値と一致する。  
  https://www.mext.go.jp/content/20241213-mxt_chousa01-000037551_01.pdf

### Claim 4: 2010→2015年は +0.6pt
- Status: CORRECT
- Evidence: `51.5 - 50.9 = 0.6` ポイント。

### Claim 5: 2015→2024年は +7.6pt
- Status: CORRECT
- Evidence: `59.1 - 51.5 = 7.6` ポイント。

### Claim 6: +7.6pt は反証条件 +2pt の3.8倍
- Status: CORRECT
- Evidence: `7.6 / 2.0 = 3.8`。

### Claim 7: 2024年の大学（学部）入学者数は63.3万人
- Status: CORRECT
- Evidence: 令和6年度学校基本調査確定値の約63.3万人と一致する。  
  https://www.mext.go.jp/content/20241213-mxt_chousa01-000037551_01.pdf

### Claim 8: 2024年の18歳人口106万人を、59.1%の直接の分母として扱える
- Status: NEEDS VERIFICATION
- Evidence: 私学事業団の18歳人口約106.3万人と、学校基本調査の進学率算定に使う18歳人口には定義差がある。63.3万人を59.1%で割ると約107.1万人となり、表の丸め値106万人とは一致しない。グラフでは「出典・定義が異なる系列」である旨を明示すべきである。  
  https://www.shigaku.go.jp/files/shigan_doukouR7.pdf  
  https://www.mext.go.jp/content/20241213-mxt_chousa01-000037551_01.pdf

### Claim 9: 18歳人口201万人→106万人は47.3%減
- Status: CORRECT
- Evidence: 表示値による計算は `(201 - 106) / 201 = 47.26%`。

### Claim 10: 入学者数49.2万人→63.3万人は28.7%増
- Status: CORRECT
- Evidence: `(63.3 - 49.2) / 49.2 = 28.66%`。

## DEMO 3

### Claim 1: 都道府県別充足率は「デモ用近似値」であることが明示されている
- Status: CORRECT
- Evidence: RESULTS.md の Fact-check メモに「本デモの数値は近似値」「私学事業団の公表値と細部で異なる可能性」と明記されている。ただし、聴衆が必ず見る**グラフ本体または直下の注記**にも同じ注意書きを表示することが望ましい。数値自体の公式値照合は本レビューの対象外とした。

## DEMO 4

### Claim 1: 1990年代前半の出生数は約120万人前後
- Status: CORRECT
- Evidence: 1990～1994年は約118.7万～122.2万人であり、表現は妥当。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 2: 2000年の出生数は約119万人
- Status: CORRECT
- Evidence: 確定数は1,190,547人。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 3: 2010年の出生数は約107万人
- Status: CORRECT
- Evidence: 確定数は1,071,304人。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 4: 2016年は約97万人で、初めて100万人を下回った
- Status: CORRECT
- Evidence: 確定数は976,978人で、100万人割れは初めて。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 5: 2022年の出生数は約77万人
- Status: CORRECT
- Evidence: 確定数約77.0万人と整合する。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 6: 2023年の出生数は約73万人
- Status: CORRECT
- Evidence: 確定数約72.7万人を四捨五入した表現として妥当。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suii00/index.html

### Claim 7: 2024年の出生数は推計約68～70万人
- Status: CORRECT
- Evidence: 令和6年人口動態統計の確定数は686,061人で、範囲内である。ただし2026年時点では「推計」ではなく「確定数約68.6万人」と更新できる。  
  https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/index.html

### Claim 8: 2024年の18歳人口は約110万人
- Status: CORRECT
- Evidence: 用いる定義により約106～107万人であり、「約110万人」という十万人単位の概数としては許容範囲。ただし他デモとの統一のため「約106万人」または「約107万人」と出典別に示す方が正確。

### Claim 9: 2030年代前半の18歳人口は約100万人前後
- Status: NEEDS VERIFICATION
- Evidence: 社人研系列では2030年約96万人、2035年約89万人である。「前半」の範囲によって90万人台前半まで低下するため、具体的な年を示して「2030年約96万人、2035年約89万人」と書くべきである。  
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp

### Claim 10: 2040年頃の18歳人口は約80万人
- Status: CORRECT
- Evidence: 社人研の2040年約82万人と整合する。  
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp

### Claim 11: 2040年代後半には18歳人口が約70万人以下
- Status: INCORRECT
- Evidence: 同じRESULTS.mdの社人研系列は2045年78万人、2050年74万人であり、2040年代後半に「70万人以下」とはならない。**「2050年でも約74万人」または「2040年代後半は70万人台」**に修正すべきである。  
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp

### Claim 12: 社人研系列は2020年118、2030年96、2040年82、2050年74万人
- Status: CORRECT
- Evidence: 社人研「日本の将来推計人口（令和5年推計）」の中位推計を万人単位に丸めた値と整合する。  
  https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/pp_zenkoku2023.asp

### Claim 13: 2030年の仮想線125万人との差は+29万人
- Status: CORRECT
- Evidence: `125 - 96 = 29` 万人。

### Claim 14: 2040年の仮想線135万人との差は+53万人
- Status: CORRECT
- Evidence: `135 - 82 = 53` 万人。

### Claim 15: 2050年の仮想線145万人との差は+71万人
- Status: CORRECT
- Evidence: `145 - 74 = 71` 万人。

