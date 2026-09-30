# -*- coding: utf-8 -*-
"""
The रु of 8.2.66 and what becomes of it — 8.2.66, 6.1.113, 8.3.15, 8.3.17,
8.3.19, 8.3.34.

**One sound, five fates, decided by what stands beside it.** A pada-final स्
becomes a रु (8.2.66). Before a short अ that रु is an उ (6.1.113), so
*रामस्* + *अत्र* is रामोऽत्र; before a soft consonant likewise (6.1.114); before
a pause or a खर् it is a visarga (8.3.15); after अ or आ and before an अश् it is
a य् (8.3.17), which may then be dropped (8.3.19).

**The reason it is worth a module of its own is ordering.** 8.2.66 stands in
the tripādī and 6.1.113 in the सपादसप्ताध्यायी, so 8.2.1 says the रु is asiddha
to 6.1.113 — yet 6.1.113 *names* the रु and would be empty if it could not see
it. The grammar's answer is वचनप्रामाण्यात्: `consumes` on the rule, the mark
`RU` on the sound. And the same 8.2.1 that hides it there makes **हर इह**
come out with its अ and इ apart: 8.3.19 drops the य् and the two vowels stand
side by side, and 6.1.87 does not join them, for the loss is asiddha to it.
"""

from __future__ import annotations

from src.astadhyayi.anga import akah_savarne_dirghah
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.rule import (
    sk,
    ADESA, LOPA, Application, Detail, NewSeg, Via, delete, replace, rule,
    site)
from src.astadhyayi.sandhi.segs import RU, View

#: What a rule that NAMES a loss must be allowed to see of it — 6.3.111's
#: ढ्रलोपे. Written on the loss by 8.3.13 and 8.3.14.
RA_LOPA = "ra-lopa"


def _ru_sight(s) -> bool:
    return s.s == "r" and s.has(RU)


@rule("8.2.66", name="ससजुषो रुः", families=("visarga",),
      overrides=(("8.2.39", "a rule laid down for a pada-final स् itself is "
                            "the exception to 8.2.39's जश्त्व for any झल्"),))
def sasajuso_ruh(v: View):
    """सकारान्तस्य पदस्य सजुषश्च रुः — रामस्, हरिस् ⟶ रु."""
    for s in v.live:
        if not v.pada_final(s):
            continue
        if s.s == "s" or (s.s == "ṣ" and v.word(s).text == "sajuṣ"):
            yield Application(
                site=site(s),
                edits=(replace(s, NewSeg("r", frozenset({RU}), show="ru")),),
                detail=Detail(
                    kind=ADESA, sthanin=s.s, adesa="ru",
                    nimitta="the end of a pada",
                    because=(f"{sk(s.s)} ends a pada, so it is replaced by "
                             f"{{ru}} — a र् whose उ is an इत् and is lost"),
                    via=S.it_removed("u")))


def _after_short_a(v: View, r):
    prev = v.prev(r)
    return prev is not None and prev.s == "a" and not prev.seg.has("pluta")


@rule("6.1.113", name="अतो रोरप्लुतादप्लुते", families=("visarga",),
      consumes=(RU,))
def ato_ror_aplutad_aplute(v: View):
    """अप्लुतादतः परस्य रोरुः स्यादप्लुतेऽति — शिवोऽर्च्यः, रामोऽत्र."""
    for r in v.live:
        if not _ru_sight(r) or not _after_short_a(v, r):
            continue
        nxt = v.next(r)
        if nxt is None or nxt.s != "a" or nxt.seg.has("pluta"):
            continue
        yield Application(
            site=site(v.prev(r), r, nxt), edits=(replace(r, "u"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="u",
                nimitta="a short a before and a short a after",
                because=("the {ru} stands after a short अ and before a short "
                         "अ, neither pluta, so it becomes उ"),
                via=(S.tapara("a"),)))


@rule("8.3.15", name="खरवसानयोर्विसर्जनीयः", families=("visarga",))
def kharavasanayor_visarjaniyah(v: View):
    """रेफान्तस्य पदस्य खरि परतोऽवसाने च विसर्जनीयः — वृक्षः, वृक्षस्तरति."""
    khar = S.members("khaR")
    for r in v.live:
        if r.s != "r" or not v.pada_final(r):
            continue
        nxt = v.next(r)
        if not (v.at_pause(r) or (nxt is not None and nxt.s in khar)):
            continue
        yield Application(
            site=site(r, nxt) if nxt is not None else site(r),
            edits=(replace(r, "ḥ"),),
            detail=Detail(
                kind=ADESA, sthanin="r", adesa="ḥ",
                nimitta=("a pause follows" if nxt is None
                         else f"the {{khar}} {sk(nxt.s)} follows"),
                because=("the pada ends in र् and " + (
                    "a pause follows" if nxt is None
                    else f"{sk(nxt.s)} is a {{khar}}") + ", so it becomes the "
                    "visarga"),
                via=(S.avasana_condition(),) if nxt is None else ()))


@rule("8.3.34", name="विसर्जनीयस्य सः", families=("visarga",))
def visarjaniyasya_sah(v: View):
    """खरि परे विसर्जनीयस्य सः — चक्रिँस्त्रायस्व, विष्णुस्त्राता."""
    khar = S.members("khaR")
    for h in v.live:
        if h.s != "ḥ":
            continue
        nxt = v.next(h)
        if nxt is None or nxt.s not in khar:
            continue
        yield Application(
            site=site(h, nxt), edits=(replace(h, "s"),),
            detail=Detail(
                kind=ADESA, sthanin="ḥ", adesa="s",
                nimitta=f"the {{khar}} {sk(nxt.s)} follows",
                because=(f"the visarga stands before the {{khar}} {sk(nxt.s)}, "
                         f"so it becomes स्"),
                via=()))


@rule("8.3.17", name="भोभगोअघोअपूर्वस्य योऽशि", families=("visarga",))
def bhobhago_yo_si(v: View):
    """एतत्पूर्वस्य रोर्यादेशोऽशि — देवा इह ⟶ देवायिह."""
    ash = S.members("aŚ")
    for r in v.live:
        if not _ru_sight(r):
            continue
        prev, nxt = v.prev(r), v.next(r)
        if prev is None or nxt is None:
            continue
        if prev.s not in ("a", "ā") or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, r, nxt), edits=(replace(r, "y"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="y",
                nimitta=f"{sk(prev.s)} before and the {{aś}} {sk(nxt.s)} after",
                because=(f"the {{ru}} follows {sk(prev.s)} and the {{aś}} "
                         f"{sk(nxt.s)} comes after it, so it becomes य्"),
                via=()))


@rule("8.3.19", name="लोपः शाकल्यस्य", families=("visarga",))
def lopah_sakalyasya(v: View):
    """अवर्णपूर्वयोः पदान्तयोर्यवयोर्लोपो वाशि परे — हर इह, हरयिह."""
    ash = S.members("aŚ")
    for y in v.live:
        if y.s not in ("y", "v") or not v.pada_final(y):
            continue
        prev, nxt = v.prev(y), v.next(y)
        if prev is None or nxt is None:
            continue
        if prev.s not in ("a", "ā") or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(delete(y),),
            optional="विभाषा",
            detail=Detail(
                kind=LOPA, sthanin=y.s, adesa="",
                nimitta=f"{sk(prev.s)} before and the {{aś}} {sk(nxt.s)} after",
                because=(f"a pada-final {sk(y.s)} after अ or आ and before an "
                         f"{{aś}} may be lost, by Śākalya's opinion"),
                via=()))


@rule("6.1.114", name="हशि च", families=("visarga",), consumes=(RU,))
def hasi_ca(v: View):
    """तथा रोरुः स्याद्धशि — शिवो वन्द्यः, मनोरथः."""
    has = S.members("haŚ")
    for r in v.live:
        if not _ru_sight(r) or not _after_short_a(v, r):
            continue
        nxt = v.next(r)
        if nxt is None or nxt.s not in has:
            continue
        yield Application(
            site=site(v.prev(r), r, nxt), edits=(replace(r, "u"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="u",
                nimitta=f"a short a before and the {{haś}} {sk(nxt.s)} after",
                because=(f"the {{ru}} stands after a short अ and before the "
                         f"{{haś}} {sk(nxt.s)}, so it becomes उ"),
                via=(S.tapara("a"),)))


@rule("8.3.14", name="रो रि", families=("visarga",))
def ro_ri(v: View):
    """रेफस्य रेफे परे लोपः — पुना रमते, हरी रम्यः, शम्भू राजते."""
    for r in v.live:
        if r.s != "r" or not v.pada_final(r):
            continue
        nxt = v.next(r)
        if nxt is None or nxt.s != "r":
            continue
        yield Application(
            site=site(r, nxt), edits=(delete(r, RA_LOPA),),
            detail=Detail(
                kind=LOPA, sthanin="r", adesa="",
                nimitta="a र् follows",
                because=("a pada-final र् before another र् is lost"),
                via=()))


@rule("6.3.111", name="ढ्रलोपे पूर्वस्य दीर्घोऽणः", families=("visarga",),
      consumes=(RA_LOPA,))
def dhralope_purvasya_dirgho_nah(v: View):
    """ढ्रेफयोर्लोपनिमित्तयोः पूर्वस्याणो दीर्घः — पुना रमते, हरी रम्यः."""
    sights = list(v.sights)
    for index, lost in enumerate(sights):
        if not lost.seg.elided or RA_LOPA not in lost.marks or index == 0:
            continue
        before = sights[index - 1]
        if before.seg.elided or not S.is_member(before.s, "aṆ"):
            continue
        got = akah_savarne_dirghah(before.s, before.s)
        if got.result is None or got.result == before.s:
            continue
        yield Application(
            site=site(before, lost), edits=(replace(before, got.result),),
            detail=Detail(
                kind=ADESA, sthanin=before.s, adesa=got.result,
                nimitta="a र् has just been lost after it",
                because=(f"{sk(before.s)} is an {{aṇ}} and the ढ् or र् after "
                         f"it has been lost, so it is lengthened to "
                         f"{sk(got.result)}"),
                via=(S.pratyahara("aṆ", "a, i, u"),)))


RULES = (sasajuso_ruh, ato_ror_aplutad_aplute, hasi_ca,
         kharavasanayor_visarjaniyah, visarjaniyasya_sah, bhobhago_yo_si,
         lopah_sakalyasya, ro_ri, dhralope_purvasya_dirgho_nah)

#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("8.2.66", "rule", ""),
    ("6.1.113", "rule", ""),
    ("6.1.114", "rule", ""),
    ("8.3.14", "rule", ""),
    ("8.3.15", "rule", ""),
    ("8.3.17", "rule", ""),
    ("8.3.19", "partial", "य् and व् after अ or आ; the lighter य् of 8.3.18 is not yet done"),
    ("8.3.34", "partial", "without the exceptions of 8.3.35–37"),
    ("6.3.111", "rule", ""),
)
