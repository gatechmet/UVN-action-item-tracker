# UVNN Strategy Tracker: rules for every session

## The one rule

**The team uses the shared-folder version: `shared-drive-demo/UVNN-Tracker.html`.**
It opens on a "Connect to the UVNN tracker" setup screen and stores data as JSON
files in the team's OneDrive/SharePoint `tracker-data` folder.

Anything handed to the user as "the tracker", "the HTML", "the export" or "the
published version" must be that file (and `Strategy-Tracker.zip`, which contains
the same HTML). Never hand over `tracker.html` or the claude.ai artifact as the
release. That mistake happened once (Oct 2026): the user received a page that
demanded a claude.ai sign-in instead of the folder setup screen.

## How the files fit together

| File | What it is | Edit it? |
|---|---|---|
| `tracker.html` | App source: all tracker UI and logic. Also what the claude.ai sandbox artifact runs. | **Yes**, this is where changes go |
| `shared-drive-demo/build/head.html`, `folder-layer.html`, `tail.html` | The shared-folder layer: setup screen, folder storage, seed data | Only for folder or setup-screen changes |
| `shared-drive-demo/UVNN-Tracker.html` | **The release.** Built from the two rows above. | **Never by hand**, always run the build |
| `shared-drive-demo/Strategy-Tracker.zip` | Release HTML plus the `tracker-data` folder, for setting up the shared folder | Refreshed by the build |
| `shared-drive-demo/tracker-data/` | Snapshot of the team's data | Only when the user asks for a data update |

## Workflow for any change

1. **Start from `main`.** Run `git fetch origin main` and make sure your branch contains it.
   `main` is the source of truth, not the claude.ai artifact and not an older session's memory.
2. **Edit `tracker.html`.**
3. **Optional preview:** publish `tracker.html` to the sandbox artifact
   (https://claude.ai/artifact/FdMPm2peYUEbiBrV7FrxRS) so the user can try it.
   This is for previews only. Its data lives in claude.ai, not the team folder.
   If the artifact was changed elsewhere, merge those changes into `tracker.html` first.
4. **Build the release:** `python3 shared-drive-demo/build/build.py`
5. **Test the release, not the source:** open `UVNN-Tracker.html`, confirm the
   setup screen appears, connect a *copy* of `tracker-data`, and exercise the change.
   (Headless: stub `window.showDirectoryPicker` with an OPFS folder loaded from a copy of `tracker-data`.)
6. **Check:** `python3 shared-drive-demo/build/build.py --check` must print `OK`.
7. **Commit `tracker.html`, `UVNN-Tracker.html` and the zip together, then push.**
8. **Send the user `shared-drive-demo/UVNN-Tracker.html`** (plus the zip if asked).

## Guardrails that enforce this

- `.claude/settings.json` has a hook that blocks `git commit` and `git push` in
  Claude Code sessions whenever `build.py --check` fails.
- `.github/workflows/release-check.yml` runs the same check on every push and pull request.

## Before you answer "where is X?" or "export the last version"

Look in git (`git log --all -- shared-drive-demo/`), not just the artifact. If
what you find doesn't have the folder setup screen, it's the wrong file.
