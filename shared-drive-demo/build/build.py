#!/usr/bin/env python3
"""Build the RELEASE tracker (shared-folder version) from the app source.

    tracker.html                        app source (also what the claude.ai sandbox artifact runs)
  + shared-drive-demo/build/*.html      the shared-folder layer (setup screen, folder storage, seed data)
  = shared-drive-demo/UVNN-Tracker.html the RELEASE the team uses, also copied into Strategy-Tracker.zip

Usage (from the repo root):
  python3 shared-drive-demo/build/build.py           build the release and refresh the zip
  python3 shared-drive-demo/build/build.py --check   verify only; exits 1 if anything is out of step

Never edit shared-drive-demo/UVNN-Tracker.html by hand. Edit tracker.html (or the
folder layer pieces in this folder), then run this script.
"""
import os, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'tracker.html')
B = os.path.join(ROOT, 'shared-drive-demo', 'build')
REL = os.path.join(ROOT, 'shared-drive-demo', 'UVNN-Tracker.html')
ZIP = os.path.join(ROOT, 'shared-drive-demo', 'Strategy-Tracker.zip')
ZIP_HTML = 'Strategy Tracker/UVNN-Tracker.html'

SRC_TITLE = '<title>UVNN Strategy Tracker</title>\n'
CHART = 'chart.umd.min.js"></script>\n<script>\n'
# Markers that prove a file is the shared-folder version, not the claude.ai one.
MARKERS = ['showDirectoryPicker', 'id="sp-connect"', 'FIRST TIME - Click here to connect folder', 'window.SEED=']


def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return f.read()


def build():
    src = read(SRC)
    if not src.startswith(SRC_TITLE):
        sys.exit(f'tracker.html must start with {SRC_TITLE!r}. Strip any wrapper the artifact added.')
    if 'showDirectoryPicker' in src:
        sys.exit('tracker.html already contains the folder layer. It must be the plain app source.')
    if src.count(CHART) != 1:
        sys.exit('Could not find the single Chart.js <script> anchor in tracker.html.')
    head, layer, tail = (read(os.path.join(B, n)) for n in ('head.html', 'folder-layer.html', 'tail.html'))
    body = src[len(SRC_TITLE):]
    i = body.index(CHART) + len(CHART)
    return head + body[:i] + layer + body[i:] + tail


def zip_html():
    with zipfile.ZipFile(ZIP) as z:
        return z.read(ZIP_HTML).decode('utf-8').replace('\r\n', '\n')


def check(out):
    problems = []
    rel = read(REL)
    if rel != out:
        problems.append('UVNN-Tracker.html does not match a fresh build of tracker.html. Run build.py.')
    for m in MARKERS:
        if m not in rel:
            problems.append(f'UVNN-Tracker.html is missing {m!r}: it is not the shared-folder version.')
    if zip_html() != rel:
        problems.append(f'{ZIP_HTML} inside Strategy-Tracker.zip differs from UVNN-Tracker.html. Run build.py.')
    return problems


def write_zip(out):
    """Replace only the HTML inside the zip (Windows line endings, as the team's copy uses)."""
    tmp = ZIP + '.tmp'
    with zipfile.ZipFile(ZIP) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = out.replace('\n', '\r\n').encode('utf-8') if item.filename == ZIP_HTML else zin.read(item.filename)
            zout.writestr(item, data)
    os.replace(tmp, ZIP)


if __name__ == '__main__':
    out = build()
    if '--check' not in sys.argv:
        with open(REL, 'w', encoding='utf-8', newline='') as f:
            f.write(out)
        write_zip(out)
        print('Built shared-drive-demo/UVNN-Tracker.html and refreshed Strategy-Tracker.zip')
    problems = check(out)
    for p in problems:
        print('FAIL:', p)
    if problems:
        sys.exit(1)
    print('OK: release is the shared-folder version, matches tracker.html, and the zip matches.')
