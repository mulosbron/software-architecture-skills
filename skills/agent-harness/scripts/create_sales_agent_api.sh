#!/usr/bin/env bash
# Create & Deploy a Sales Representative Agent via REST API (AutoManus-style)
# Usage:
#   export SALES_AGENT_API_KEY="your_api_key"
#   export SALES_AGENT_API_URL="https://api.example.com/v1/agents"
#   ./scripts/create_sales_agent_api.sh "Acme Corp" "https://acme.com" "founder@acme.com"

set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 "<Company Name>" "<Website URL>" "<Owner Email>"" >&2
  exit 1
fi

COMPANY_NAME="$1"
WEBSITE_URL="$2"
OWNER_EMAIL="$3"

API_KEY="${SALES_AGENT_API_KEY:?Set SALES_AGENT_API_KEY environment variable first}"
API_URL="${SALES_AGENT_API_URL:?Set SALES_AGENT_API_URL environment variable first}"

curl -sS -X POST "$API_URL" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"company_name\": \"${COMPANY_NAME}\",
    \"website_url\": \"${WEBSITE_URL}\",
    \"email\": \"${OWNER_EMAIL}\",
    \"channels\": [\"web_chat\", \"whatsapp\"],
    \"widget\": {
      \"position\": \"bottom-right\",
      \"theme_color\": \"#2563EB\"
    }
  }" | python3 -m json.tool
