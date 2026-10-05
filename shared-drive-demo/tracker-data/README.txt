UVNN Strategy Tracker - shared-folder version
==============================================

What's in the folder
  Strategy Tracker\
    UVNN-Tracker.html     <- open this
    tracker-data\         <- all the tracker's records, plus this file

Lives in SharePoint at
  UVNN - General > KPI Leadership > Strategy Tracker

First time, for each person
1. Open the team's General folder in SharePoint and click
   "Add shortcut to OneDrive".
2. In File Explorer, go to OneDrive > UVNN - General > KPI Leadership >
   Strategy Tracker and double-click UVNN-Tracker.html. It opens in Edge or
   Chrome. Don't open it from SharePoint or Teams in the browser - the
   folder picker is blocked there.
3. Click "FIRST TIME - Click here to connect folder" and select the
   tracker-data folder. Click "Edit files" when asked.

After that
- If you chose "Allow on every visit", the tracker connects by itself.
- Otherwise click "Reconnect to ..." once.

Tabs
- Activity Tracker
  - Action Items: priorities, objectives and actions, with filters, the
    status pop-up, month colors, notes, and bulk paste of new actions.
  - Dashboard: progress bars and counts by priority and objective.
- Weekly KPI
  - Dashboard: bowler charts. Each chart has its own Weekly / Run rate /
    Quarters view and a Full year or Q1-Q4 range.
  - Inputs: the weekly bowler grid. Type into cells, paste a row of
    weeks, or paste the whole bowler from Excel.
- Forecasting
  - Dashboard: AOP vs monthly forecasts and actuals, by region, with
    forecast accuracy and book-to-bill.
  - Inputs: the monthly curve, AOP, each monthly forecast (quarter
    totals) and monthly actuals. Type, paste a block from Excel, or paste
    a whole tab from the forecast input workbook.

Good to know
- OneDrive syncs in the background, so other people's edits can take a few
  seconds to a minute to appear.
- The whole year's bowler is one file (bowler__2026.json), and the year's
  forecasting inputs are one file (forecast__2026.json). If two people
  type into the same file at the same moment, one person's entries can be
  lost, so have one person enter the bowler and one the forecasting inputs.
- If two people change the same action at the same moment, OneDrive may keep
  a copy named like actions__A12-YOURPC.json. The tracker ignores these.
- Don't edit or delete the files in tracker-data by hand.
- The Performance charts load a charting library from the internet.
- Filters, views and chart settings stay in your own browser tab.
