#!/bin/bash
# Re-fetch the third-party sandhi datasets at the commits used on 2026-09-30.
# DATA IS NOT IN THIS REPO and must not be added to it: SandhiKosh is research-use
# only, three clones state no licence, two are GPL (see the handover, SOURCES.md).
# usage: tools/sandhi_datasets/fetch.sh [DEST]     (default: ../sandhi_work/external_data/raw)
set -u
DEST="${1:-../sandhi_work/external_data/raw}"
mkdir -p "${DEST:?}"
fetch() {  # name owner/repo sha
  local name="$1" repo="$2" sha="$3" dir="${DEST}/$1"
  if [ -d "$dir/.git" ]; then echo "EXISTS $name"; return; fi
  GIT_TERMINAL_PROMPT=0 git clone --quiet "https://github.com/${repo}.git" "$dir" || { echo "FAIL $name"; return; }
  if [ -n "$sha" ]; then git -C "$dir" checkout --quiet "$sha" && echo "OK $name @ ${sha:0:10}"; else echo "OK $name (unpinned)"; fi
}
fetch sanskrit-sandhi_SandhiKosh                        sanskrit-sandhi/SandhiKosh                              b4938f82982a3217899fb554bbc093fab3a6b85b
fetch funderburkjim__ScharfSandhi                       funderburkjim/ScharfSandhi                              51ca52895ad5bb585fd1479f6fa7eeb7ab93985c
fetch kmadathil_sanskrit_parser                         kmadathil/sanskrit_parser                               a31ff41cc0869201007ca87a01aaee574ebe01b1
fetch performance__sandhi-joiner-benchmark              performance/sandhi-joiner-benchmark                     ba5cbfc481ff2e3abb34707147c44e3f5ab35746
fetch ambuda-org_vidyut                                 ambuda-org/vidyut                                       8da2f90bee3ce1c07505fa432fc3729e3f7e02ea
fetch ambuda-org__dcs                                   ambuda-org/dcs                                          7622c22f9c5fb1bf183af58951e96d7043edd699
fetch SriramKrishnan8__sanskrit_segmentation_evaluation SriramKrishnan8/sanskrit_segmentation_evaluation       799cb9e560e44285af8e31fad2e074af0f81eea2
fetch shantanuo__sandhi                                 shantanuo/sandhi                                        2e62fa51bc222b1465b76b7c94eff495d62b2e5f
fetch krishnamrith12__KISS_Sanskrit_Parsing_Data        krishnamrith12/KISS_Sanskrit_Parsing_Data               4c0aaec9bc78dccd9383f087a0a89d7ab2d52272
fetch SandhiKSU__SandhiSplitter                         SandhiKSU/SandhiSplitter                                814ab00f070c8e3af82ddc2d9545070f6d20facd
fetch sanskrit-sandhi__sanskrit_sandhi_corpus           sanskrit-sandhi/sanskrit_sandhi_corpus                  7799c85cb1417d82ee60ec789153c5b951cee901
fetch SandeshLamichhane4473__sandhi-split-sanskrit-dataset SandeshLamichhane4473/sandhi-split-sanskrit-dataset ""
echo "Kaggle (needs the kaggle CLI and an API token; not automated here):"
echo "  kaggle datasets download -d viragumathe5/sanskrit-sandhi-corpus   # train.xlsx, test.xlsx"
echo "  kaggle datasets download -d tanujsaxena/sandhi-data               # sandhi_data.xlsx (a superset of the above)"
echo "  kaggle datasets download -d varunrajuvangar/rigved-all-sukta-verses-and-meaning-dataset"
