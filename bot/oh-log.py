from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import os
import time
import subprocess
from dhooks import Webhook

if __name__ == "__main__":

    # 対象ディレクトリ
    DIR_WATCH = '/srv/tagoken-craft/logs/'
    # 対象ファイル名のパターン
    PATTERNS = ['*.log']
    
    HOOK_URL = "https://discord.com/api/webhooks/XXX"
    hook = Webhook(HOOK_URL)

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        # print('%s changed' % filename)
        context = subprocess.run(["tail", "-n", "1", "/srv/tagoken-craft/logs/latest.log"], capture_output=True, text=True)
        # print(context.stdout)

        # if ("joined" or "left") in context.stdout:
        #     print(context.stdout)
        #     hook.send(context.stdout)
        hook.send(context.stdout)

    # event_handler = LoggingEventHandler()
    event_handler = PatternMatchingEventHandler(PATTERNS)
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()