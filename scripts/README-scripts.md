# Profile build scripts

- `make_monitor.py live-monitor-v2.svg` - wide animated monitor (top of profile)
- `gen_profile.py .` - wide panels in `assets/`
- `gen_mobile.py .` - big-text panels (`*-m.svg`) used on screens up to 1011px wide (phones, tablets, small laptops)
- `activity.py assets` - real GitHub activity feed; run automatically by `.github/workflows/activity.yml` twice a day

The README picks the right version with `<picture><source media="(max-width: 1011px)">`.
