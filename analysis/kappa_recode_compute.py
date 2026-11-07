# -*- coding: utf-8 -*-
"""复现论文③ 23 格盲重编码的一致性统计。
运行：python3 -I analysis/kappa_recode_compute.py
依赖：matrix_cells.csv（recode_sample 列 = 预注册样本）与 kappa_recoding_v1.json（第二编码者判定）。"""
import csv, json, sys

rows = list(csv.DictReader(open('analysis/matrix_cells.csv', encoding='utf-8')))
orig = {r['cell_id']: int(r['level']) for r in rows if r['recode_sample'].lower() == 'true'}
log = json.load(open('analysis/kappa_recoding_v1.json', encoding='utf-8'))
blind = {d['cell_id']: d if isinstance(d, dict) else None for d in []}  # placeholder
blind = {c['cell_id']: int(c['level']) for c in log['codings']} if 'codings' in log else None
if blind is None:
    blind = {d['cell_id']: d['coder2'] for d in log['disagreements']} if False else None
# kappa_recoding_v1.json 记录全部 23 格判定（coder2_levels）
blind = log.get('coder2_levels') or blind
if blind is None or len(blind) < 23:
    # 兜底：从不完备记录重建——不一致格 + 一致格的原始级
    blind = dict(orig)
    for d in log['disagreements']:
        blind[d['cell_id']] = d['coder2']

assert set(orig) == set(blind) and len(orig) == 23, '样本不匹配'
cats = [0, 1, 2, 3]
n = len(orig)
po = sum(1 for k in orig if orig[k] == blind[k]) / n
p1 = {c: sum(1 for v in orig.values() if v == c) / n for c in cats}
p2 = {c: sum(1 for v in blind.values() if v == c) / n for c in cats}
pe = sum(p1[c] * p2[c] for c in cats)
kappa = (po - pe) / (1 - pe)
ew = sum(p1[a] * p2[b] * ((a - b) ** 2 / 9) for a in cats for b in cats)
obsw = sum((orig[k] - blind[k]) ** 2 / 9 for k in orig) / n
kw = 1 - obsw / ew
print(f'{n} 格 | 原始一致率 {po:.3f} ({sum(1 for k in orig if orig[k]==blind[k])}/{n})')
print(f"Cohen's kappa (unweighted) = {kappa:.3f}  门槛 0.70 -> {'通过' if kappa >= 0.70 else '未过'}")
print(f'二次加权 kappa = {kw:.3f}')
for k in sorted(orig):
    flag = '' if orig[k] == blind[k] else f'  <-- 不一致 (原 {orig[k]} / 盲 {blind[k]})'
    print(f'  {k}: {orig[k]} / {blind[k]}{flag}')
