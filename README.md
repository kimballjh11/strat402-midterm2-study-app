# Start here

Folder: this folder, inside "zStrat 402". Plan: BUILD-GUIDE.md. Tonight, run it in this order.

1. Open Terminal and run:
   cd ~/Desktop/"zStrat 402"/M2-STUDY-APP
   caffeinate -dimsu &
   claude
   Keep the Mac plugged in and open. The caffeinate line keeps it awake.
2. In Claude Code type /model and pick Sonnet (Pro plan, saves usage).
3. Run the stages in order, one command each:
   /stage 00
   /stage 01
   /stage 10 S15
   /stage 10 S16
   /stage 10 S18
   /stage 10 S19
   /stage 10 S20
   /stage 20
   Then type /clear and run /audit.
4. If a usage limit stops it, wait for the reset, open claude again, type /resume-build.
5. Progress check any time: run  .venv/bin/python scripts/validate.py  and open STATUS.generated.md.
6. Morning: open app/index.html. The 5 minute checklist is in BUILD-GUIDE.md section 10.
7. When class materials arrive, drop them in inbox/ and run /ingest (see inbox/README.md). S21 and S22 are about a quarter of the exam, so do this as soon as you have notes.

Because the Pro plan limits usage, finishing all five sessions plus audit in one night is not guaranteed. The stages are ordered so the app works after stage 01 plus S15, and each session adds a finished, verified piece.
