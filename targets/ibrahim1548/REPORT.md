# Report: catalogue 885

- Target: catalogue 885 (`targets/ibrahim1548`).
- Documents: HHStA Wien, StAbt Türkei I 7-4-4 (AIS 7040827, fol. 28-30), 7-4-5 (AIS 7040824, fol. 31-34), 7-4-9 (AIS 7040845, fol. 51-59).
- Access (corrected 30 Oct 2026): the scans are public without a login; the maintainer's `fetch_images.py` gets the full 2400 px scans. The AIS "Kein Zugang (Reservatbestand)" fields concern the originals. The 29 Oct 2026 version of this report called the item blocked; that was wrong and is withdrawn.
- Images worked from (30-31 Oct 2026): screenshots of the AIS viewer from a cloud browser, about 930-1565 px, because this session's proxy refuses the AIS host. Not committed.
- Key: the Ferdinand-Malvezzi key of 1548, DECODE R367 (`targets/malvezzi1548/k367.txt`), with corrections for this hand (crossed-tail 9 = r, smooth-tail 9 = x, h-hook = n, plain Pi = g) and new code groups (NOTES.md).
- Decipherment: 7-4-4 both copies and 7-4-5 all four copies read; the 7-4-9 letter's six cipher paragraphs read from the signs and checked on its contemporary interlinear decipherment; the 7-4-9 enclosures (two further Frater Georg letters, 22 and 28 July 1548) read in part. Plaintext: `reading_full.txt`.
- Method: read after matching with key from external sources (R367, filed in Budapest for another letter).
- Share of tokens that give sense: 0.80 of 1,431 cipher words (`measure_sense.py`; 0.92 without the 7-4-9 enclosures). Agreement with the filed exemplars 0.897, with the 7-4-9 gloss 0.886; both are upper bounds, the reader had them open.
- Already published: no modern decipherment found (repo, DECODE, AIS, web search). The exemplars and the 7-4-9 gloss are contemporary plaintext in the archive. Austro-Turcica 1541-1552 (pp. 276-278) not seen.
- Open: unread groups in the 7-4-9 enclosures (resolution, a tear, four codes), the 7-4-9 replica (not transcribed). Next step: re-read them from the 2400 px scans.
- Step log: WORKLOG.md in this folder; solution steps in profile.json.
- Tools: Claude Code; Python, cloud browser.
