# Sigismund August, Frater Georg and Queen Isabella to Ibrahim Pasha, 1548 (catalogue 885)

Status: in progress. All cipher copies of 7-4-4 (2) and 7-4-5 (4) and the cipher of the 7-4-9 letter deciphered with R367 (30-31 Oct 2026, section "R367 applied to every copy" below); the 7-4-9 enclosures B and C read in part and the 7-4-9 replica not transcribed, so not yet at the read bar.

HHStA Wien, StAbt Türkei I 7-4-4 (AIS 7040827, f. 28-30, 5 images), 7-4-5 (AIS 7040824, f. 31-34, 6 images), 7-4-9
(AIS 7040845, f. 51-59, 11 images). Copies of letters to Ibrahim Pasha ("Hebrai Bassa") that Malvezzi sent to
Ferdinand I in the summer of 1548. Each cipher copy is filed with a clear Latin exemplar, so the plaintext is in hand.

## Access (corrects the first report)

AIS marks the records "Kein Zugang (Reservatbestand)", but the digital copy downloads to any client that keeps the
session cookie from `detail.aspx`: `fetch_images.py` (one request at a time; `width=2400` returns the full scan; the
JPEG is labelled text/html). `bildansicht.aspx` looks empty without that session. All 22 images fetched 30 Oct 2026
(not committed). PR #196 reported these as unreachable; they are not.

## What is on the images

- **7-4-4** (Sigismund August to Ibrahim Pasha, Cracow, 1 June 1548): image 1 (f. 28) and image 3 (f. 29, headed A,
  "Dupl. 1548") are cipher, image 2 is a scribbled-out verso, image 4 (f. 30) is the **Latin exemplar**
  (`texts/exemplar_7-4-4_A.txt`), image 5 a docket verso.
- **7-4-5** (Frater Georg to Ibrahim Pasha, Vinea, 2 July 1548): images 1-3 are cipher copies (B and C among them),
  image 5 carries two **Latin exemplars**, C ("Aliud exemplum", `texts/exemplar_7-4-5_C.txt`) and B (not yet
  transcribed), image 6 their continuation.
- **7-4-9** (Malvezzi to Ferdinand I, covering letter with enclosed cipher copies): images 1-5 and 10-11 landscape,
  6-9 portrait; not looked at beyond a contact sheet.

## The system (first look)

The signs on 7-4-4 f. 29 are the signs of the Ferdinand-Malvezzi key of 1548 (`../malvezzi1548/KEY_BRIEF.md`, DECODE
R367/R386): the first line begins with the Latin-letter words *Idcirco*, *b.*, *d.*, which are three of that key's
nulls, and the graphic signs (hash, pi, crossed circles, breve and bar forms) are the same. Same key family, to be
tested. The Latin exemplar of 7-4-4 is about 560 letters; the cipher on f. 29 is 13 lines of about 45 signs, the same
order of magnitude, so f. 29 may encipher exactly this text (with nulls). Not yet tested.

## 7-4-4 f. 29 transcribed and decoded (30 Oct 2026)

Thirteen lines, 572 signs (21 of them Latin-letter null words), transcribed from half-line crops by two image agents
(`TRANSCRIPTION_BRIEF.md`; `transcription/f29_lines_01-07.txt`, `f29_lines_08-13.txt`, labels in `f29_labels_*.txt`).
`align_f29.py` aligns the values on `texts/exemplar_7-4-4_A.txt`: the cipher spells the exemplar from *Sigismundus
Augustus Dei gratia Rex Poloniae ...* to *... Maiestatis*, with 462 of 473 key-derived tokens matching (97.7%;
`transcription/f29_alignment.txt`). 56 further tokens take their value from the exemplar (marked `*`) and are not counted.
The exemplar's heading (*Ad Hebrai Bassa. Exemplum literae Regis Poloniae*) is not enciphered. The cipher opens with
a short passage not in the exemplar (*replica*, after the nulls *idcirco b d*), and the last line ends *Maiestatis
propria* where the exemplar reads *... Prebria*. The date clause and the closing (*Regni vero nri primo, Et loco suo, ex
commissione ...*) fit only in part (L11-L12); 11 signs there are unexplained.

**Caveat, and the blind check.** Both transcribers had the exemplar open, so 97.7% is an upper bound. A blind
transcription of lines 8-10 (no exemplar, no crib; `transcription/blind/RESULT.md`) matches the exemplar for 61.4% of its
scored tokens (70/114), against 99.2% for the crib-assisted values of the same lines; the two transcriptions agree on 43%
of values. So the key family is confirmed without the crib (chance is about 8%), but the crib moved the ambiguous
signs: quote 61% as the independent fit, one noisy transcriber, three lines. The sign-to-value table (`transcription/f29_label_values.tsv`)
is consistent for 65 of 80 labels; 15 labels carry two values (mostly e/ae and u/e, the circle-on-stem family the key
brief already calls ambiguous).

**Corrections to the R367 brief** (from the transcribers, unchecked): r and x look reversed (the 9 with a crossed tail
reads r, the 9 with a long smooth tail reads x); a pi with a right-leg stub reads s; a cup with a taller left upright
reads g; the small round cup and the open arch read l.

## f. 28 looked at, not transcribed (30 Oct 2026, paused)

f. 28 (image 1 of AIS 7040827; also headed A, docket "1548 1/6") is not a second copy of f. 29's length: a header
line (*... cum*, *1548 1/6*) and about 19 closely set lines of cipher, roughly 1,000 signs against the exemplar's 560
letters, in a denser hand with many look-alike signs. It begins *... dicirco Dar.* (nulls) and ends *n spu atq spo*
(nulls). Lines run down to the right by about 2.5 degrees (a deskew near 2.5 degrees sharpens the line profile best),
and line spacing is about 66 px, so crops need rotation first. Whether it enciphers the same text with many more nulls
or a longer text is not known; the exemplar crib may not fit. Work paused by the user on 30 Oct 2026.
(Answered below: f. 28 enciphers the same letter, heading included, in 16 lines plus an interlinear header.)

## R367 applied to every copy (30-31 Oct 2026, PR #196)

Done for PR #196 after the review pointed out that the scans are public. The container proxy refuses the AIS host, so
the images were read in the cloud browser from the viewer (anonymous, one page at a time) as screenshots of about
930-1565 px, not the 2400 px scans `fetch_images.py` gets. Image agents transcribed each copy sign by sign with the R367
files; the Latin exemplars and the 7-4-9 gloss were used only as a check, and a value only an exemplar supports is
marked `{..}` or `[..]`, never written as read. One reader per copy, no second blind pass.

Files: `transcription/r367/*_signs.txt` (sign transcriptions; the maintainer's `transcription/f29_*` are untouched),
`transcription/r367/notes_7-4-4.md`, `notes_7-4-5.md` (sign variants, every disagreement with the exemplar),
`texts/exemplar_7-4-5_B.txt` (new), `texts/gloss_7-4-9_letter.txt` and `texts/clear_7-4-9_letter.txt` (new),
`reading_full.txt` (one line per cipher copy, nulls removed), `measure_sense.py`.

**Sign values for this hand** (all copies; they correct or extend `../malvezzi1548/KEY_BRIEF.md`): the 9 with a crossed
tail is r and the 9 with a smooth tail is x (as k367.txt has it; KEY_BRIEF has them reversed); h-hook = n; λ = h;
plain Π and Ш = g; footed circle and the horned 8 = q; δ with a barred stem = t; π with a right-leg stub = s; a cup
with a taller left upright = g; small round cup and open arch = l; °P, ∂ and P with a circle below = o; looped g = d.
The circle-on-stem family stays ambiguous (u, e/ae, at f. 28's resolution also t) and is settled word by word.
Loose nulls (b, d, n, z, π, and once a plain Π) are also written inside words. New sign: Ш with three bars = *annus*.
Two signs are not in the key: the z of *Chazum* (745C, 745X3) and a triple-barred x in *maximum* (745C).

**Code groups** as in R367: Ras = Turcarum Imperator, Sis = Ibrahim Passa, Ka = Passa, zos = Frater Georgius,
zi = Hungaria, Bi = Rex Galliae, Nis, 50 = bellum; Vb (Rex Poloniae) is written *Bu* on f. 28. **Not in R367**, meanings
from the 7-4-9 gloss or the context: Mos = the French, Mes = (Your) Majesty, Mus = both Majesties, Ris = the Venetian
bailo, za = Constantinople (R367 has Cad), Ses = Salih Reis, yu = Persia, 59 = exercito, 68 = a ship type (gloss
"Triremes"). Unexplained: *N.* and *F.* in 749B.

### 7-4-4: both copies read

f. 28 (`744A`) enciphers the exemplar with its heading (*Ad Hebrai Bassa. Exemplum literarum <Regis Poloniae>*) in 16
lines and an interlinear header; f. 29 (`744D`) is headed *replica* (the cipher's opening passage, which the f. 29
alignment left open) and leaves the heading out. The date clause resolves: *Regni vero nostri* (the copies drop
*primo*) and *ex commissione sacrae regiae Maiestatis propria* (the exemplar's *Prebria* is *propria*). Sigismund
Augustus asks Ibrahim to help his interpreter Nicolaus the Armenian reach the Sultan safely (Cracow, 1 June 1548).

| copy | cipher words | read | slip {} | code <> | unread [] |
|---|---|---|---|---|---|
| 744A f. 28 | 94 | 84 | 6 | 2 | 2 (an e with a superscript cross in *Bassar*, a blot in *auxilio*) |
| 744D f. 29 | 92 | 82 | 6 | 0 | 4 |

On f. 28 about 50 of the read words rest on a circle-on-stem value chosen by the word: the 932 px screenshot does
not separate δ, δ̶, ϙ and ♀. The 2400 px scan should settle them.

### 7-4-5: four copies of two letters, all read

Two Frater Georg letters to Ibrahim, each in two copies: **B** (6 June 1548, *Corde de curia*), image 1 (`745B`) and
image 4 (`745X4`, "Dupl. 2/7"); **C** (2 July 1548, *in arce Viiuar*), image 2 (`745C`, torn at the right edge) and
image 3 (`745X3`, "Dupl. 6/6"). The "Dupl." dockets on images 3 and 4 look swapped. Exemplar B (f. 34r foot and
f. 34v) is now transcribed; its torn right edge is filled by the cipher copies, which also confirm *Corde de curia*.
B: Ferdinand's force in Hungary is aimed only at the Hungarians who disobeyed him, not at the Sultan; the wheat was
spoiled by rain. C: they fear attack while the Sultan is away; he asks Ibrahim to order Kasım Pasha at Buda and
Mehmed Pasha to send help when asked. The twin copies code a word one spells out (*bellum*/50, *hongariam*/zi,
*anno*/annus sign).

| copy | cipher words | read | slip {} | code <> | unread [] |
|---|---|---|---|---|---|
| 745B | 130 | 115 | 9 | 3 | 3 |
| 745X4 | 132 | 111 | 12 | 6 | 3 |
| 745C | 121 | 104 | 5 | 7 | 5 (three at the torn edge, among them *Mehmeth*) |
| 745X3 | 118 | 102 | 9 | 5 | 2 |

745C leaves *quadragesimo* out of the date.

### 7-4-9: the letter, its gloss, and two enclosures

Image 1 is the right edge of f. 51r only; images 2-3 (f. 51v-52v) are Malvezzi's original letter to Ferdinand
(Constantinople, 26 Aug 1548), in Italian with six cipher paragraphs (L1-L6), and **a contemporary interlinear Italian
decipherment over every cipher line** (Vienna's decipherer; transcribed in `texts/gloss_7-4-9_letter.txt`). Images 4-5
(f. 53-54) are the replica, without gloss; its cipher blocks were matched to L1-L6 by position and code words only.
Image 6 is enclosed copy B, image 8 enclosed copy C ("Dupl. 1548.22.c"), images 7 and 9 are blank, images 10-11 clear
Latin petitions of Várad merchants.

**The letter (L1-L6) is read from the signs**, word by word before the gloss was compared: Aramon's letters to the
King of France, opened by Cambrai (dearth in the Sultan's army; Dragut and Salih Reis with the fleet; the bailo's bad
offices; next year's preparations "to ruin both Majesties"); Ibrahim and Yunus Bey on the French lies; Fumel's Turkish
copy of a French letter, enclosed; and *mando anchora a uostra Maiesta la copia de doi lettere de Frater Georgio
nouamente dirette al Bassa qua in Constantinopoli*, which are enclosures B and C. The gloss is a contemporary
decipherment of the same text, so the letter's reading is checked, not first broken, here. Where signs and gloss differ
the signs are usually fuller (*mirabilia mundi*, *pero de giorno in giorno*, *uinti uele*); the differences are listed
in `notes_7-4-9.md`. The opening of L1 is on f. 51r, outside image 1.

| unit | words | read | slip {} | code <> | unread [] |
|---|---|---|---|---|---|
| L1 | 45 | 37 | 0 | 1 | 7 (small signs, screenshot resolution) |
| L2-L5 | 325 | 299 | 3 | 22 | 1 (a group struck out with an ink blot, L2 l. 10) |
| L6 | 54 | 48 | 0 | 6 | 0 |

**Enclosed copy B** (15 lines, top left torn away) is a third Frater Georg letter to Ibrahim, dated *Corde, 28 July
1548*, matching neither 7-4-5 exemplar: he wrote earlier to the Sultan about Ferdinand and a coming war, and asks
that help be kept ready. 106 tokens: 48 read, 13 slip-corrected, 4 code, 41 unread (5 at the tear, 36 small crowded
signs that the screenshot does not resolve, *N.* and *F.* unexplained).

**Enclosed copy C** (28 lines, top left torn away) is a fourth Frater Georg letter to Ibrahim, dated *in Monostor*
(Kolozsmonostor), *die uigesimo secundo mensis Iulii* 1548, signed *seruitor <zos> episcopus uaradiensis*. It shares
only formulae with the exemplars (address, commendation, B's *Deus ... conseruet incolumem*, the subscription). He asks
whether the Sultan's tribute (*censum potentissimi Caesaris*) should go to Ibrahim or to the Sultan's son; the German
war is still in Hungary, with the castle of Eger (*arcemque Agriensem*); he asks Ibrahim to write to <Ko> Passa and
another Pasha and send their answers back by his servant. 214 tokens: 167 read, 10 slip-corrected, 7 code, 30 unread
(4 at the tear; l. 16 in part, all of l. 17, the start of l. 18, the names in ll. 19-20, a pair in l. 23, the sign
before the date). New: ^ (looks like λ) = f; N = dies; *eʃ.* a null group; Ko. (perhaps Ta.) a code not in R367.

B and C are Malvezzi's "doi lettere de Frater Georgio nouamente dirette al Bassa" of L6, so 7-4-9 holds two Frater
Georg letters (Corde, 28 July; Monostor, 22 July) of which no clear exemplar is filed here.

### Measure (`measure_sense.py`, 31 Oct 2026)

The README's n-gram measure needs the `la` corpus, whose host (gutenberg.org) the proxy refused. A stand-in corpus
from Latin Library texts on GitHub (Caesar, Cicero, Livy 1-5, Vulgate, Erasmus) under-scores: malvezzi1548's reading,
0.990 on the official corpus, scores 0.772 on it. So the main test here is agreement with the external plaintext:
the share of cipher words that agree with the exemplar word they align to (744, 745), or with the gloss word (749
letter, Italian, code words left out because their meaning came from the gloss). Both are checks against a text the
reader had open, so they are upper bounds on an independent fit (the f. 29 blind check gave 61%).

- 744 and 745, six copies, 687 words: exemplar agreement 616 = 0.897; n-gram (stand-in) 0.617; either 646 = 0.940.
- 749 letter, Italian, 395 plaintext words: gloss agreement 350 = 0.886; mark count 0.980; 29 code words.
- 749 enclosures B and C (Latin, no exemplar), 320 tokens: n-gram (stand-in) 126 = 0.394; mark count 249 = 0.778.
  The window test sinks next to unread groups, so for B (0.123) it says more about the gaps than the read words.
- All Latin copies, 1,007 tokens: n-gram or exemplar 772 = 0.767; mark count 0.911.
- Controls (letters shuffled within words): n-gram 0.034, exemplar 0.108.

## Remaining gaps

- 7-4-9 enclosed copy B: 36 groups in ll. 4-11 (small crowded signs, mostly the circle-on-stem and looped-9 families) - blocker: illegible; at the screenshot resolution of this session, the 2400 px scan from `fetch_images.py` (refused by this session's proxy) should resolve most of them
- 7-4-9 enclosed copy C: l. 16 in part, l. 17, the start of l. 18, the names in ll. 19-20, a pair in l. 23 - blocker: illegible; same resolution limit as B
- 7-4-9 B and C: the top left of both leaves is torn away (5 and 4 tokens) - blocker: needs-physical-access; the paper is missing, no other copy of these two letters is filed here
- 7-4-9 code groups *N.* and *F.* (B), *Ko.*, *Ta.* (C): not in R367, no gloss - blocker: open-codes
- 7-4-9 replica (f. 53-54, images 4-5): not transcribed; it duplicates the glossed letter and was matched to L1-L6 by position and code words only - blocker: not-attempted
- 7-4-9 L1: the opening on f. 51r is outside image 1 (right edge only); 7 small groups unread - blocker: illegible
- 7-4-9 L2 l. 10: one group struck out with an ink blot (gloss ".65. mare") - blocker: illegible
- 7-4-4 f. 28 *Bassar* (an e with a superscript cross) and *auxilio* (blot); f. 29 four tokens; 7-4-5 thirteen tokens, three at 745C's torn edge (*Mehmeth*) - blocker: illegible
- 7-4-5 signs not in the key: the z of *Chazum* and a triple-barred x - blocker: open-codes

## Escalation

- [x] siblings: malvezzi1548 (R366, R367, R386) is the same key family; R367 reads every copy here
- [x] clear-pages: the Latin exemplars on f. 30 and f. 34 (A, B, C) and the 7-4-9 interlinear gloss checked word by word
- [x] known-keys: R367 applied to all 14 cipher units, with the sign corrections above
- [ ] print: Austro-Turcica 1541-1552 (pp. 276-278) not seen; it may print Malvezzi's letter and the enclosures
- [ ] key-rebuild: not needed for the key; the new code groups (Mos, Mes, Mus, Ris, za, Ses, yu, 59, 68, Ko) come from the gloss or the context
- [ ] retry: B and C ll. 16-23 from the 2400 px scans (`fetch_images.py`), and the replica

## Next steps

1. Re-read the unread groups of 7-4-9 B and C, and the f. 28 circle-on-stem words, from the 2400 px scans.
2. Transcribe the replica (f. 53-54) and compare it with L1-L6.
3. A second blind transcriber on one copy, to replace the exemplar-agreement upper bound with an independent figure.
4. Look for the two Frater Georg letters of July 1548 (B, C) in Austro-Turcica 1541-1552 or the Martinuzzi editions.
5. Credit Harrison Bornstein (PR #196) for the lead to the Malvezzi key and for this pass.
