# Sense measure for ibrahim1548, adapted from ../malvezzi1548/measure_sense.py (same tests, same thresholds).
# Reads reading_full.txt in this folder: one line per cipher unit, "unit | tokens", nulls removed. Token marks:
#   word      read, every sign matches the key
#   {word}    read after correcting a writer's slip that the context forces
#   <word>    nomenclator code word, rendered in its grammatical form
#   [x]       not read; x is what the signs give
# A plaintext word counts as read when it is marked read (plain, {slip} or <code>) and, for a non-code word, the word
# is a Latin word (corpus vocabulary or a word score above the 2nd percentile of rare corpus words) and the 9-word
# window centred on it scores above the 2nd percentile of random 9-word corpus windows ('la' 5-gram model).
# Units named on the command line are Italian: no n-gram test (no Italian corpus here); they get the mark count and,
# for the 7-4-9 letter units, agreement with the contemporary interlinear gloss (texts/gloss_7-4-9_letter.txt).
# The 'la' corpus host (gutenberg.org) was refused from the 30 Oct 2026 session; lang/corpora/la-gutenberg.txt was
# built instead from Latin Library texts on GitHub (Caesar, Cicero, Livy 1-5, Vulgate, Erasmus; cltk mirror).
# Second test, for units filed with a Latin exemplar (EXEMPLAR below): the share of read tokens that agree with the
# exemplar word they align to (difflib on normalised words: u/v, i/j, ae/e, doubled letters). This is a check against
# external plaintext, not part of the decipherment. Control: letters shuffled inside each word.
import os, sys, random, difflib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
os.chdir(os.path.dirname(os.path.abspath(__file__)))

EXEMPLAR = {          # unit -> exemplar text file
    '744A': 'texts/exemplar_7-4-4_A.txt', '744D': 'texts/exemplar_7-4-4_A.txt',
    '745B': 'texts/exemplar_7-4-5_B.txt', '745X4': 'texts/exemplar_7-4-5_B.txt',
    '745C': 'texts/exemplar_7-4-5_C.txt', '745X3': 'texts/exemplar_7-4-5_C.txt',
}
ITALIAN = set(a for a in sys.argv[1:] if not a.startswith('-'))   # units to score as Italian, if any

M = lm.load('la')
N = lambda s: lm.norm(s, 'latin')
corpus = N(open(os.path.join('..', '..', 'lang', 'corpora', 'la-gutenberg.txt'), encoding='utf8', errors='ignore').read())
cw = corpus.split()
LEX = set(cw)
random.seed(1)
cal = sorted(M.per_char(' '.join(cw[i:i + 9])) for i in (random.randrange(len(cw) - 9) for _ in range(2000)))
THR = cal[int(0.02 * len(cal))]
from collections import Counter
cnt = Counter(cw)
rare = [w for w, c in cnt.items() if c == 1 and len(w) >= 5]
random.shuffle(rare)
wc = sorted(M.per_char(' ' + w + ' ') for w in rare[:3000])
WTHR = wc[int(0.02 * len(wc))]

def wordok(w):
    return w in LEX or M.per_char(' ' + w + ' ') > WTHR

def parse(fn='reading_full.txt'):
    units = {}
    for line in open(fn, encoding='utf8'):
        if line.startswith('#') or '|' not in line: continue
        u, t = line.split('|', 1)
        for tok in t.split():
            if tok.startswith('['): kind, w = 'U', tok.strip('[]')
            elif tok.startswith('{'): kind, w = 'S', tok.strip('{}')
            elif tok.startswith('<'): kind, w = 'C', tok.strip('<>')
            else: kind, w = 'R', tok
            units.setdefault(u.strip(), []).append((kind, w))
    return units

def judge(toks, W=4):
    words = [N(w) for _, w in toks]
    ok = []
    for i, (k, w) in enumerate(toks):
        if k == 'U': ok.append(False); continue
        if k == 'C': ok.append(True); continue
        win = ' '.join(words[max(0, i - W): i + W + 1])
        ok.append(wordok(words[i]) and M.per_char(win) > THR)
    return ok

def canon(w):
    w = ''.join(c for c in N(w) if c.isalpha())
    w = w.replace('v', 'u').replace('j', 'i').replace('ae', 'e').replace('oe', 'e')
    out = ''
    for c in w:
        if not out or out[-1] != c: out += c
    return out

def exemplar_words(fn):
    t = open(fn, encoding='utf8').read()
    t = t.split('\n\n', 1)[1] if '\n\n' in t else t          # drop the file's description paragraph
    t = t.replace('[', '').replace(']', '').replace('|', ' ').replace('&', ' et ').replace('-', '')
    return [c for c in (canon(w) for w in t.split()) if c]

GLOSS = 'texts/gloss_7-4-9_letter.txt'

def gloss_words(unit):
    # the "== Lk" section of the gloss file, editorial marks removed: (?) [..] [?] and bracketed notes
    import re
    want, out, on = unit.replace('749', '').rstrip('a'), [], False
    for line in open(GLOSS, encoding='utf8'):
        if line.startswith('=='):
            on = line.split()[1] == want; continue
        if on and not line.startswith(('#', '(')):
            line = re.sub(r'\(\?\)|\[[^\]]*\]|\([^)]*\)', ' ', line).replace("'", ' ')
            out += [c for c in (canon(w) for w in line.split()) if c]
    return out

def exemplar_agreement(toks, fn):
    ex = gloss_words(fn[6:]) if fn.startswith('gloss:') else exemplar_words(fn)
    rd = [canon(w) for k, w in toks]
    sm = difflib.SequenceMatcher(None, rd, ex, autojunk=False)
    agree = [False] * len(rd)
    for a, b, n in sm.get_matching_blocks():
        for j in range(n): agree[a + j] = True
    # words aligned inside replace blocks agree when they differ by at most one letter
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'replace':
            for x, y in zip(range(i1, i2), range(j1, j2)):
                if difflib.SequenceMatcher(None, rd[x], ex[y]).ratio() >= 0.8: agree[x] = True
    readmask = [k != 'U' for k, _ in toks]
    return [a and r for a, r in zip(agree, readmask)]

if __name__ == '__main__':
    units = parse()
    print(f'THR window = {THR:.3f}, WTHR word = {WTHR:.3f}')
    T = S = E = ET = B = 0
    IG = IT = IM = IC = 0
    for u, toks in units.items():
        if u in ITALIAN:
            n = sum(k != 'U' for k, _ in toks)
            line = f'{u}: Italian, mark count {n}/{len(toks)}'
            if os.path.exists(GLOSS) and gloss_words(u):
                # code words are left out: the gloss renders them in Italian ("il Turcho" over Ras), and the
                # meaning of the new groups was taken from the gloss, so agreement there would be circular
                ag = exemplar_agreement(toks, 'gloss:' + u)
                pl = [(w, a) for (k, w), a in zip(toks, ag) if k != 'C']
                g = sum(a for _, a in pl)
                IG += g; IT += len(pl); IM += sum(k != 'U' for k, _ in toks if k != 'C'); IC += len(toks) - len(pl)
                line += f'  gloss agreement (code words left out) {g}/{len(pl)} = {g/len(pl):.3f}'
                line += f'  not agreeing: {" ".join(w for w, a in pl if not a)}'
            print(line)
            continue
        ok = judge(toks)
        T += len(toks); S += sum(ok)
        line = f'{u}: n-gram {sum(ok)}/{len(toks)} = {sum(ok)/len(toks):.3f}'
        ex = EXEMPLAR.get(u)
        if ex and os.path.exists(ex):
            # exemplar test per plaintext word; a code word like Regis_Poloniae agrees if all its parts do
            parts = [(i, p) for i, (k, w) in enumerate(toks) for p in w.split('_')]
            ag = exemplar_agreement([(toks[i][0], p) for i, p in parts], ex)
            per = [True] * len(toks)
            for (i, _), a in zip(parts, ag): per[i] = per[i] and a
            E += sum(per); ET += len(toks)
            both = [o or a for o, a in zip(ok, per)]
            B += sum(both)
            line += f'  exemplar {sum(per)}/{len(toks)} = {sum(per)/len(toks):.3f}  either {sum(both)}/{len(toks)} = {sum(both)/len(toks):.3f}'
            bad = [w for (k, w), o in zip(toks, both) if not o]
        else:
            B += sum(ok)
            bad = [w for (k, w), o in zip(toks, ok) if not o]
        print(line + f'  not counted: {" ".join(bad)}')
    if IT:
        print(f'Italian units against the gloss, plaintext words: agreement {IG}/{IT} = {IG/IT:.3f}, '
              f'mark count {IM}/{IT} = {IM/IT:.3f}; code words {IC}')
    if T:
        print(f'overall n-gram (Latin units): {S}/{T} = {S/T:.3f}')
        if ET: print(f'overall exemplar agreement (units with an exemplar): {E}/{ET} = {E/ET:.3f}')
        print(f'overall sense, n-gram or exemplar: {B}/{T} = {B/T:.3f}')
        marks = sum(k != 'U' for u, toks in units.items() if u not in ITALIAN for k, _ in toks)
        print(f'mark count only: {marks}/{T} = {marks/T:.3f}')
        print(f'slip-corrected: {sum(k == "S" for t in units.values() for k, _ in t)}; '
              f'code words: {sum(k == "C" for t in units.values() for k, _ in t)}')
        random.seed(2)
        ctl = [[(k, ''.join(random.sample(w, len(w))) if k != 'C' else w) for k, w in toks]
               for u, toks in units.items() if u not in ITALIAN]
        cs = sum(sum(judge(t)) for t in ctl)
        print(f'control, n-gram (letters shuffled within words): {cs}/{T} = {cs/T:.3f}')
        ce = cet = 0
        for (u, toks), t in zip([(u, t) for u, t in units.items() if u not in ITALIAN], ctl):
            ex = EXEMPLAR.get(u)
            if ex and os.path.exists(ex):
                ce += sum(exemplar_agreement([(k, w.replace('_', '')) for k, w in t], ex)); cet += len(t)
        if cet: print(f'control, exemplar (same shuffle): {ce}/{cet} = {ce/cet:.3f}')
