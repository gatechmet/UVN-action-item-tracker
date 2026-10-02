# UVNN 2026 Strategy Tracker

Shared action item tracker: Priorities → Objectives → Actions, with owners, regions,
target dates (with change history), monthly status, dated update notes, a dashboard,
and bowler Performance charts.

## What the team uses

**`shared-drive-demo/UVNN-Tracker.html`, the shared-folder version.** It opens on a
setup screen, connects to the `tracker-data` folder in the UVNN SharePoint/OneDrive
(`UVNN - General › KPI Leadership › Strategy Tracker`), and saves every record there
as a small JSON file. `Strategy-Tracker.zip` holds the same HTML plus a copy of the
data folder. See `shared-drive-demo/tracker-data/README.txt` for team setup steps.

## Making changes

| Step | Command or file |
|---|---|
| 1. Edit the app | `tracker.html` |
| 2. Preview (optional) | Publish `tracker.html` to the sandbox artifact: https://claude.ai/artifact/FdMPm2peYUEbiBrV7FrxRS |
| 3. Build the release | `python3 shared-drive-demo/build/build.py` |
| 4. Check | `python3 shared-drive-demo/build/build.py --check` |
| 5. Commit all three | `tracker.html`, `shared-drive-demo/UVNN-Tracker.html`, `shared-drive-demo/Strategy-Tracker.zip` |

Never edit `UVNN-Tracker.html` by hand. The build adds the shared-folder layer
(`shared-drive-demo/build/*.html`) to `tracker.html`. A GitHub check and a Claude Code
hook both refuse a release that isn't a fresh shared-folder build. Full rules are in `CLAUDE.md`.

The sandbox artifact keeps its own test data in claude.ai. It is never the release.

## Other files

- `seed.json`: the original import from `2026V2_UVNN_Strategy_Tracker_test.xlsx`.
