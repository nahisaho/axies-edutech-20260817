"""Generate presentation-embed charts for AXIES 2026 slides.

Output: axies-edutech-20260817/assets/slides/*.png
Design tokens: Microsoft Fluent palette (#0078D4 / #107C10 / #D13438 / #FFB900),
IPAexGothic (via japanize_matplotlib) fonts, 16:9 aspect ratio for hero graphs.
"""
from __future__ import annotations
import os
import warnings

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable
import japanize_matplotlib  # noqa: F401
from japanmap import picture, pref_names

warnings.filterwarnings("ignore", category=UserWarning)

OUT = os.path.expanduser(
    "~/SHIKIGAKI/20260716_AXIES_EduTech/axies-edutech-20260817/assets/slides"
)
os.makedirs(OUT, exist_ok=True)

# Fluent tokens
COL_BLUE = "#0078D4"
COL_GREEN = "#107C10"
COL_RED = "#D13438"
COL_AMBER = "#FFB900"
COL_GRAY = "#605E5C"
COL_INK = "#323130"
COL_PAPER = "#F3F2F1"

DPI = 180


def save(fig, name: str):
    path = f"{OUT}/{name}.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  OK {name}.png")


# =====================================================================
# Slide 28: DEMO 1 hero (16:9)
# =====================================================================
def slide28_demo1_hero():
    fig, ax = plt.subplots(figsize=(13.33, 7.5))

    years_j = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024, 2025]
    vals_j = [201, 177, 151, 137, 122, 120, 118, 106, 109]
    years_s = [2030, 2035, 2040, 2045, 2050]
    vals_s = [96, 89, 82, 78, 74]

    ax.plot(years_j, vals_j, marker="o", markersize=10, linewidth=4,
            color=COL_BLUE, label="実測 (文科省 学校基本調査 / 私学事業団)")
    ax.plot([2025, 2030], [109, 96], linestyle=(0, (2, 3)),
            color="#909090", linewidth=1.5)
    ax.plot(years_s, vals_s, marker="s", markersize=10, linewidth=4,
            color=COL_RED, linestyle="--", label="推計 (社人研 R5 中位)")

    ax.annotate("▲ +2.6%\n(2006 生まれが約3万人多)",
                xy=(2025, 109), xytext=(2013, 138),
                fontsize=15, color="#B08000", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=COL_AMBER, lw=2))
    ax.annotate("2040: 82 万人\n= 2005 年の約 60%",
                xy=(2040, 82), xytext=(2032, 50),
                fontsize=16, color=COL_RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=COL_RED, lw=2))

    ax.axvline(x=2027.5, color="#909090", linestyle=":", linewidth=1.2)
    ax.text(2027.5, 212, "実測 → 推計", ha="center",
            fontsize=13, color=COL_GRAY)

    ax.set_xlabel("年", fontsize=16)
    ax.set_ylabel("18 歳人口（万人）", fontsize=16)
    ax.set_title("日本の 18 歳人口の推移（1990-2050）",
                 fontsize=22, fontweight="bold", pad=18, color=COL_INK)
    ax.set_ylim(40, 225)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper right", fontsize=13, framealpha=0.95)

    fig.text(0.02, 0.015,
             "出典: 文科省 学校基本調査 (~2024) / 私学事業団 R7 志願動向 (2025) / 社人研 R5 中位推計 (2030~)",
             fontsize=10, color=COL_GRAY)

    plt.tight_layout()
    save(fig, "slide28_demo1_hero")


# =====================================================================
# Slide 31: DEMO 2 hero
# =====================================================================
def slide31_demo2_hero():
    fig, ax1 = plt.subplots(figsize=(13.33, 7.5))

    years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]
    jinkou = [201, 177, 151, 137, 122, 120, 118, 106]
    nyugaku = [49.2, 56.8, 59.9, 60.3, 61.9, 61.8, 63.5, 63.3]
    shingaku = [24.6, 32.1, 39.7, 44.2, 50.9, 51.5, 54.4, 59.1]

    ax1.plot(years, jinkou, marker="o", markersize=10, linewidth=4,
             color=COL_BLUE, label="18 歳人口（万人・左軸）")
    ax1.plot(years, nyugaku, marker="s", markersize=10, linewidth=4,
             color=COL_GREEN, label="大学入学者数（万人・左軸）")
    ax1.set_xlabel("年", fontsize=16)
    ax1.set_ylabel("人数（万人）", fontsize=16)
    ax1.set_ylim(0, 230)
    ax1.tick_params(axis="both", labelsize=13)
    ax1.grid(True, linestyle="--", alpha=0.4)

    ax2 = ax1.twinx()
    ax2.plot(years, shingaku, marker="D", markersize=10, linewidth=4,
             color=COL_RED, linestyle="--", label="大学進学率（%・右軸）")
    ax2.set_ylabel("大学進学率（%）", fontsize=16, color=COL_RED)
    ax2.set_ylim(0, 70)
    ax2.tick_params(axis="y", labelcolor=COL_RED, labelsize=13)

    ax2.annotate("プラトー予想を反証\n2015→2024 で +7.6pt",
                 xy=(2024, 59.1), xytext=(2010, 35),
                 fontsize=16, color=COL_RED, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=COL_RED, lw=2))

    ax1.set_title("18 歳人口減 vs 大学入学者数横ばい — 進学率上昇で相殺",
                  fontsize=20, fontweight="bold", pad=18, color=COL_INK)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2,
               loc="center left", fontsize=13, framealpha=0.95)

    fig.text(0.02, 0.015,
             "出典: 文科省 学校基本調査 令和 6 年 (2024) 確定値。進学率は 3 年前中卒者数ベース。",
             fontsize=10, color=COL_GRAY)

    plt.tight_layout()
    save(fig, "slide31_demo2_hero")


# =====================================================================
# Slide 34: DEMO 3 hero (47都道府県ヒートマップ)
# =====================================================================
PREF_DATA = {
    "北海道": 92, "青森県": 82, "岩手県": 84, "宮城県": 96, "秋田県": 78,
    "山形県": 83, "福島県": 88, "茨城県": 94, "栃木県": 93, "群馬県": 95,
    "埼玉県": 101, "千葉県": 102, "東京都": 108, "神奈川県": 105, "新潟県": 89,
    "富山県": 91, "石川県": 97, "福井県": 90, "山梨県": 92, "長野県": 90,
    "岐阜県": 94, "静岡県": 97, "愛知県": 104, "三重県": 93, "滋賀県": 99,
    "京都府": 103, "大阪府": 105, "兵庫県": 100, "奈良県": 96, "和歌山県": 87,
    "鳥取県": 79, "島根県": 80, "岡山県": 95, "広島県": 98, "山口県": 86,
    "徳島県": 82, "香川県": 88, "愛媛県": 85, "高知県": 81, "福岡県": 102,
    "佐賀県": 89, "長崎県": 90, "熊本県": 93, "大分県": 88, "宮崎県": 86,
    "鹿児島県": 89, "沖縄県": 104,
}


def slide34_demo3_hero():
    cmap = LinearSegmentedColormap.from_list(
        "fuel", [COL_RED, COL_AMBER, COL_PAPER, COL_GREEN], N=256
    )
    norm = Normalize(vmin=80, vmax=110)

    pref_color = {}
    for i, pname in enumerate(pref_names[1:], start=1):
        rgba = cmap(norm(PREF_DATA[pname]))
        pref_color[i] = tuple(int(c * 255) for c in rgba[:3])

    fig, ax = plt.subplots(figsize=(13.33, 7.5))
    ax.imshow(picture(pref_color))
    ax.set_axis_off()
    ax.set_title("47 都道府県 私立大学 定員充足率（合成データ・可視化技術デモ）",
                 fontsize=20, fontweight="bold", pad=18, color=COL_INK)

    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, orientation="vertical",
                        shrink=0.6, pad=0.02)
    cbar.set_label("定員充足率（%）", fontsize=14)
    cbar.set_ticks([80, 90, 100, 110])
    cbar.ax.tick_params(labelsize=12)

    fig.text(0.02, 0.03,
             "⚠ 合成データによる可視化技術のデモです。政策判断には一次資料（私学事業団年報 / e-Stat）を参照してください。",
             fontsize=11, color=COL_RED)
    fig.text(0.02, 0.005,
             "参考: 私学事業団 令和 7 年度 志願動向 (2025) の傾向を反映した合成値",
             fontsize=9, color=COL_GRAY)

    plt.tight_layout()
    save(fig, "slide34_demo3_hero")


# =====================================================================
# Slide 37: DEMO 4 hero
# =====================================================================
def slide37_demo4_hero():
    fig, ax = plt.subplots(figsize=(13.33, 7.5))

    years = [2020, 2024, 2025, 2030, 2035, 2040, 2045, 2050]
    jitsu = [118, 106, 109, 96, 89, 82, 78, 74]

    kasou_years = [2020, 2030, 2040, 2050]
    kasou_vals = [118, 125, 135, 145]

    ax.plot(years, jitsu, marker="o", markersize=10, linewidth=4,
            color=COL_BLUE, label="実データ（社人研 R5 中位推計）")
    ax.plot(kasou_years, kasou_vals, marker="x", markersize=14,
            linewidth=3, linestyle=":", color=COL_RED, alpha=0.85,
            label="プロンプトが含意する仮想線（説明用架空値）")

    interp = [118, 96, 82, 74]
    ax.fill_between(kasou_years, interp, kasou_vals,
                    color=COL_RED, alpha=0.15, label="乖離領域")

    ax.annotate("2040 年の乖離:\n仮想 135 − 実 82 = 53 万人\n（説明用の架空シナリオ）",
                xy=(2040, 108), xytext=(2028, 45),
                fontsize=15, color=COL_RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=COL_RED, lw=2))

    ax.set_xlabel("年", fontsize=16)
    ax.set_ylabel("18 歳人口（万人）", fontsize=16)
    ax.set_title("逆質問デモ — 実データ vs プロンプトの仮想前提",
                 fontsize=20, fontweight="bold", pad=18, color=COL_INK)
    ax.set_ylim(40, 165)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper right", fontsize=13, framealpha=0.95)

    fig.text(0.02, 0.015,
             "実データ出典: 社人研 令和 5 年 中位推計 / 私学事業団 令和 7 年度 志願動向。仮想線は説明用の架空値。",
             fontsize=10, color=COL_GRAY)

    plt.tight_layout()
    save(fig, "slide37_demo4_hero")


# =====================================================================
# Slide 28 supplemental: 減少ペース棒グラフ（小型）
# =====================================================================
def slide28_delta_bars():
    fig, ax = plt.subplots(figsize=(6, 4.2))

    labels = ["2005 年\n137 万", "2020 年\n118 万", "2040 年\n82 万"]
    vals = [137, 118, 82]
    colors = [COL_GRAY, COL_BLUE, COL_RED]
    bars = ax.bar(labels, vals, color=colors, edgecolor="white", linewidth=2)

    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 3, f"{v}",
                ha="center", fontsize=15, fontweight="bold", color=COL_INK)

    ax.annotate("", xy=(1, 128), xytext=(0, 145),
                arrowprops=dict(arrowstyle="->", color=COL_GRAY, lw=1.5))
    ax.text(0.5, 152, "-19 万\n(15 年)", ha="center",
            fontsize=11, color=COL_GRAY)
    ax.annotate("", xy=(2, 92), xytext=(1, 128),
                arrowprops=dict(arrowstyle="->", color=COL_RED, lw=2))
    ax.text(1.5, 122, "-36 万\n(20 年)", ha="center",
            fontsize=12, color=COL_RED, fontweight="bold")

    ax.set_ylim(0, 175)
    ax.set_ylabel("18 歳人口（万人）", fontsize=12)
    ax.set_title("減少ペースの加速", fontsize=15,
                 fontweight="bold", color=COL_INK, pad=12)
    ax.tick_params(axis="both", labelsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    save(fig, "slide28_delta_bars")


# =====================================================================
# Slide 26: 予想通り側 小型折れ線サムネ
# =====================================================================
def slide26_thumb_line():
    fig, ax = plt.subplots(figsize=(3.5, 2.2))

    years = [1990, 2000, 2010, 2020, 2030, 2040, 2050]
    vals = [201, 151, 122, 118, 96, 82, 74]
    ax.plot(years, vals, marker="o", markersize=5, linewidth=2.5,
            color=COL_BLUE)
    ax.fill_between(years, 0, vals, color=COL_BLUE, alpha=0.12)

    ax.set_ylim(0, 220)
    ax.set_yticks([])
    ax.set_xticks([1990, 2020, 2050])
    ax.tick_params(axis="x", labelsize=9)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.set_title("減少トレンド", fontsize=10, color=COL_GREEN, pad=4)

    plt.tight_layout()
    save(fig, "slide26_thumb_line")


# =====================================================================
# Slide 9: 事実① 大数字対比
# =====================================================================
def slide09_bignum_hero():
    fig, ax = plt.subplots(figsize=(13.33, 7.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(2.3, 7.5, "2005 年", ha="center", fontsize=28, color=COL_GRAY)
    ax.text(2.3, 4.5, "137", ha="center", fontsize=180,
            color=COL_GRAY, alpha=0.75, fontweight="bold")
    ax.text(2.3, 2.2, "万人", ha="center", fontsize=36, color=COL_GRAY)

    ax.annotate("", xy=(6.8, 4.5), xytext=(4.2, 4.5),
                arrowprops=dict(arrowstyle="->", color=COL_RED, lw=4))
    ax.text(5.5, 5.5, "35 年後", ha="center", fontsize=22,
            color=COL_RED, fontweight="bold")
    ax.text(5.5, 3.5, "▲ 55 万人 (▲40%)", ha="center", fontsize=18,
            color=COL_RED)

    ax.text(8.4, 7.5, "2040 年", ha="center", fontsize=28,
            color=COL_RED, fontweight="bold")
    ax.text(8.4, 4.5, "82", ha="center", fontsize=180,
            color=COL_RED, fontweight="bold")
    ax.text(8.4, 2.2, "万人", ha="center", fontsize=36,
            color=COL_RED, fontweight="bold")

    ax.text(5, 9.4, "18 歳人口は 35 年で 4 割減少",
            ha="center", fontsize=32, fontweight="bold", color=COL_INK)
    ax.text(5, 0.5,
            "出典: 文科省 学校基本調査（2005 実測） / 社人研 R5 中位推計（2040）",
            ha="center", fontsize=12, color=COL_GRAY)

    save(fig, "slide09_bignum_hero")


# =====================================================================
# Slide 32: 進学率 +7.6pt KPI
# =====================================================================
def slide32_kpi_shingaku():
    fig, ax = plt.subplots(figsize=(13.33, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(1.8, 7.5, "2015 年", ha="center", fontsize=22, color=COL_GRAY)
    ax.text(1.8, 4.2, "51.5%", ha="center", fontsize=90,
            color=COL_GRAY, fontweight="bold")

    ax.annotate("", xy=(6.2, 4.2), xytext=(3.6, 4.2),
                arrowprops=dict(arrowstyle="->", color=COL_RED, lw=5))
    ax.text(4.9, 5.6, "9 年で", ha="center",
            fontsize=20, color=COL_RED, fontweight="bold")
    ax.text(4.9, 2.7, "+7.6 ポイント", ha="center",
            fontsize=26, color=COL_RED, fontweight="bold")

    ax.text(8.2, 7.5, "2024 年", ha="center", fontsize=22,
            color=COL_RED, fontweight="bold")
    ax.text(8.2, 4.2, "59.1%", ha="center", fontsize=90,
            color=COL_RED, fontweight="bold")

    ax.text(5, 0.6,
            "反証条件 +2pt の 3.8 倍 → プラトー予想は反証された  "
            "／ 出典: 文科省 学校基本調査 令和 6 年確定値",
            ha="center", fontsize=13, color=COL_GRAY)

    save(fig, "slide32_kpi_shingaku")


if __name__ == "__main__":
    print("Generating slide-embed charts...")
    slide28_demo1_hero()
    slide31_demo2_hero()
    slide34_demo3_hero()
    slide37_demo4_hero()
    slide28_delta_bars()
    slide26_thumb_line()
    slide09_bignum_hero()
    slide32_kpi_shingaku()
    print(f"\nDone. Output: {OUT}/")
