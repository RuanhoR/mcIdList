#!/usr/bin/env python3
"""Generate JE 1.26.2 data file with translations in en, ja, ko, zh."""
import json, os

def t(en, ja, ko, zh):
    return {"en": en, "ja": ja, "ko": ko, "zh": zh}

effects = {
    "speed": t("Speed", "移動速度上昇", "신속", "迅捷"),
    "slowness": t("Slowness", "移動速度低下", "둔화", "缓慢"),
    "haste": t("Haste", "採掘速度上昇", "가속", "急迫"),
    "mining_fatigue": t("Mining Fatigue", "採掘速度低下", "채굴 피로", "挖掘疲劳"),
    "strength": t("Strength", "力", "힘", "力量"),
    "instant_health": t("Instant Health", "即時回復", "즉시 회복", "瞬间治疗"),
    "instant_damage": t("Instant Damage", "即時ダメージ", "즉시 데미지", "瞬间伤害"),
    "jump_boost": t("Jump Boost", "跳躍力上昇", "점프 증가", "跳跃提升"),
    "nausea": t("Nausea", "吐き気", "메스꺼움", "反胃"),
    "regeneration": t("Regeneration", "再生", "재생", "生命恢复"),
    "resistance": t("Resistance", "耐性", "저항", "抗性提升"),
    "fire_resistance": t("Fire Resistance", "火炎耐性", "화염 저항", "抗火"),
    "water_breathing": t("Water Breathing", "水中呼吸", "수중 호흡", "水下呼吸"),
    "invisibility": t("Invisibility", "透明化", "투명", "隐身"),
    "blindness": t("Blindness", "暗闇", "실명", "失明"),
    "night_vision": t("Night Vision", "暗視", "야간 투시", "夜视"),
    "hunger": t("Hunger", "空腹", "배고픔", "饥饿"),
    "weakness": t("Weakness", "弱体化", "약화", "虚弱"),
    "poison": t("Poison", "毒", "독", "中毒"),
    "wither": t("Wither", "ウィザー", "시듦", "凋零"),
    "health_boost": t("Health Boost", "体力増強", "체력 증가", "生命提升"),
    "absorption": t("Absorption", "吸収", "흡수", "伤害吸收"),
    "saturation": t("Saturation", "満腹度", "포만감", "饱和"),
    "glowing": t("Glowing", "発光", "발광", "发光"),
    "levitation": t("Levitation", "浮遊", "공중 부양", "飘浮"),
    "luck": t("Luck", "幸運", "행운", "幸运"),
    "unluck": t("Bad Luck", "不運", "불행", "霉运"),
    "slow_falling": t("Slow Falling", "落下速度低下", "천천히 낙하", "缓降"),
    "conduit_power": t("Conduit Power", "導管の力", "전류의 힘", "潮涌能量"),
    "dolphins_grace": t("Dolphin's Grace", "イルカの恩恵", "돌고래의 은혜", "海豚的恩惠"),
    "bad_omen": t("Bad Omen", "凶兆", "나쁜 징조", "不祥之兆"),
    "hero_of_the_village": t("Hero of the Village", "村の英雄", "마을 영웅", "村庄英雄"),
    "darkness": t("Darkness", "暗闇", "어둠", "黑暗"),
    "trial_omen": t("Trial Omen", "試練の兆し", "시험의 징조", "试炼之兆"),
    "raid_omen": t("Raid Omen", "襲撃の兆し", "습격의 징조", "袭击之兆"),
    "wind_charged": t("Wind Charged", "風充填", "바람 충전", "蓄风"),
    "weaving": t("Weaving", "糸紡ぎ", "거미줄", "盘丝"),
    "oozing": t("Oozing", "滲出", "끈적임", "渗浆"),
    "infested": t("Infested", "寄生", "기생", "寄生"),
    "breath_of_the_nautilus": t("Breath of the Nautilus", "ナウティラスの息吹", "나우틸러스의 숨결", "鹦鹉螺之息"),
}
