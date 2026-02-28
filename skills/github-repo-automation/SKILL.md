---
name: github-repo-automation
description: Create a new GitHub repository under the user's account (public or private), push local project, and verify state. Uses gh CLI when available, otherwise GitHub API (PAT).
---

# GitHub Repository Automation Skill

Purpose
- Automate the end-to-end flow of creating a GitHub repository, initializing with your local project, pushing the initial commit, and verifying the result.
- Supports two pathways: GitHub CLI (gh) and GitHub API (via PAT). If gh is available and you are logged in, it’s preferred for simplicity.

Inputs
- repo_name: string. Example: transformer-lstm-yolo-env-noise
- private: boolean. true for private, false for public
- description: string. Repository description
- method: string. one of "gh", "api", or "auto" (default: auto)
- repo_path: string. Local repository path (default: current working directory)
- branch: string. Default branch name, typically main
- github_user: string. GitHub username (used for messaging or config hints)
- github_token: string. Personal Access Token (needed if method is "api")

Outputs
- repo_url: string. Repository URL (SSH or HTTPS, depending on remote)
- push_status: string. Status message of the push action
- commit_hash: string. The initial commit hash (if available)
- status_summary: string. High-level status (OK / ERROR) with details

Behavior / Flow
1) Detect provisioning method
   - If gh is installed and user is authenticated, use: gh repo create <name> --public|--private --description <desc> --source <repo_path> --remote origin
   - If gh is not available or not authenticated, fall back to API-based creation:
     curl -X POST https://api.github.com/user/repos \
       -H "Authorization: token <TOKEN>" \
       -d '{"name":"<name>","private":<private>,"auto_init":true,"description":"<desc>"}'

2) Push local code
   - cd <repo_path>
   - git remote set-url origin <repo_url> (if needed)
   - git branch -M <branch>
   - git push -u origin <branch>

3) Verify
   - git ls-remote <repo_url> HEAD

4) Return artifacts
   - repo_url, push_status, commit_hash, status_summary

Examples
- Example using gh
  - repo_name: transformer-lstm-yolo-env-noise
  - private: false
  - description: "Transformer+LSTM YOLO-style env-noise skeleton"
  - method: gh
  - repo_path: /home/ubuntu/.openclaw/workspace/transformer_lstm_yolo_env_noise
  - branch: main
  - repo_url: (derived by gh)

- Example using API
  - repo_name: transformer-lstm-yolo-env-noise
  - private: false
  - description: "Transformer+LSTM YOLO-style env-noise skeleton"
  - method: api
  - github_user: your-username
  - github_token: your-token
  - repo_path: /home/ubuntu/.openclaw/workspace/transformer_lstm_yolo_env_noise
  - branch: main

Notes
- This skill assumes you have either gh CLI installed and authenticated or a valid GitHub PAT for API access.
- If the repository already exists, fallback strategies include using the existing repository or renaming to avoid conflict.
- For multiple retries or extra safety, you might want to implement a wrap-around shell script that handles transient errors.
