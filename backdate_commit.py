import subprocess
import datetime

def create_backdated_commit(date, message):
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    env = {
        'GIT_COMMITTER_DATE': formatted_date,
        'GIT_AUTHOR_DATE': formatted_date
    }
    subprocess.run(['git', 'commit', '--allow-empty', '-m', message], env=env)

def main():
    # Example: Backdate to January 1, 2022
    backdate_to = datetime.datetime(2023, 1, 16)
    commit_message = "Backdated Commit"
    create_backdated_commit(backdate_to, commit_message)

if __name__ == "__main__":
    main()
