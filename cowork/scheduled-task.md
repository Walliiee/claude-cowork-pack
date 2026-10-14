# Scheduled task (template)

A scheduled task is a saved prompt that runs on a cadence: hourly, daily, weekly, on weekdays, or manually. Create one from "Scheduled" in the sidebar, either with Claude or by hand. Tasks that do not need local files run in the cloud, so they run while your computer is off. Tasks that need local files or apps run only on your computer, with Claude Desktop open.

Fields to fill in when setting one up by hand:

| Field | Example |
|---|---|
| Task name | Monday pipeline summary |
| Prompt | Summarise last week's changes in the pipeline sheet in my Drive. Flag deals that slipped. Write it as a one-page doc. |
| Approval mode | Manual: Claude asks before each action (start here) |
| Frequency | Weekly |
| Model | Optional |
| Folder | Optional; leave empty if the task only uses connected apps |
