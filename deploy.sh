#!/usr/bin/env bash
# Выкладка собранных сайтов на хостинг cPanel по SSH.
# Использование: DEPLOY=user@host DEPLOY_PORT=22 SSH_KEY=~/.ssh/key ./deploy.sh [домен ...]
set -euo pipefail
cd "$(dirname "$0")"
: "${DEPLOY:?укажите DEPLOY=user@host}"
PORT="${DEPLOY_PORT:-22}"
KEY="${SSH_KEY:-$HOME/.ssh/id_ed25519}"
python3 build.py
DOMAINS=("$@")
[ ${#DOMAINS[@]} -eq 0 ] && DOMAINS=(cakescats.com main.cakescats.com os.cakescats.com phone.cakescats.com vpn.cakescats.com llm.cakescats.com)
for dom in "${DOMAINS[@]}"; do
  # основной домен лежит в public_html, поддомены — в одноимённых папках
  if [ "$dom" = cakescats.com ]; then D=public_html; else D="$dom"; fi
  tar czf - -C "out/$dom" . | ssh -i "$KEY" -o IdentitiesOnly=yes -p "$PORT" "$DEPLOY" \
    "cd ~/$D && find . -mindepth 1 -maxdepth 1 ! -name '.well-known' ! -name 'cgi-bin' -exec rm -rf {} + && tar xzf - --no-same-permissions --no-overwrite-dir && find . -mindepth 1 -type d -exec chmod 755 {} + && find . -mindepth 1 -type f -exec chmod 644 {} +"
  echo "$dom: $(curl -s -o /dev/null -w '%{http_code}' "https://$dom/")"
done
