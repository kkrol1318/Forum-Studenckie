# 🧭 Contribution Guide for Forum-Studenckie

Welcome to the Forum-Studenckie project! This guide will help our team collaborate smoothly and avoid common issues like merge conflicts, duplicated work, or broken code.

---

## 🌳 Branching Strategy

### Main Branches

- `main` — Production-ready code. Always stable. **Protected**: No direct pushes.
- `dev` — Integrates all new features before merging to `main`.

### Feature and Fix Branches

Create a new branch for each task:

- Format: `feature/<task-name>` or `bugfix/<issue-name>`
- Examples: `feature/login-form`, `bugfix/register-error`

### Personal Dev Branches (Optional)

- Format: `dev-<your-name>`
- Use for early experimentation or if you want a space before merging to `dev`.

---

## ✅ Workflow

1. **Start from latest **``:

   ```bash
   git checkout dev
   git pull
   git checkout -b feature/my-feature
   ```

2. **Do your work and commit**:

   ```bash
   git add .
   git commit -m "Add my feature"
   git push origin feature/my-feature
   ```

3. **Create a Pull Request to **`` on GitHub.

   - Ask for a review if needed.
   - Fix merge conflicts before merging.

4. **Test everything** in `dev`.

5. When ready to release, create a PR from `dev` to `main`.

---

## 🔒 GitHub Repo Settings (For Maintainers)

- Protect the `main` branch (Settings > Branches > Rules):
  - Require pull request before merging
  - Require status checks (optional if using CI)
- Set required reviewers (optional for code review)

---

## 🛡️ Conflict Prevention Tips

| ✅ Do This                                | ❌ Avoid This                     |
| ---------------------------------------- | -------------------------------- |
| Pull from `dev` before starting new work | Starting from an old branch      |
| Commit and push often                    | Waiting days before syncing      |
| Keep PRs small and focused               | Merging large changes unreviewed |
| Use clear branch names                   | Vague or generic branch names    |
| Communicate task ownership               | Two people editing the same file |

---

## 📁 Using `.gitignore` Properly

The `.gitignore` file tells Git which files or folders **not to track**. This prevents issues like:

- Uploading sensitive files (e.g., `.env`)
- Committing OS-specific files (e.g., `.DS_Store`, `Thumbs.db`)
- Adding compiled code or IDE configs (e.g., `*.class`, `.vscode/`)

### Example Entries

```
# Node
node_modules/

# IDE
.vscode/
.idea/

# System
.DS_Store
Thumbs.db

# Env/Secrets
.env

# Build output
/dist
/build
```

> Make sure every team member has the same `.gitignore`. It should be committed to the repo!

---

Happy coding and good teamwork! 💻🚀

