#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHANGELOG_PATH="${REPO_ROOT}/CHANGELOG.md"
TEMPLATE_PATH="${REPO_ROOT}/.github/RELEASE_TEMPLATE.md"

if [[ ! -f "${CHANGELOG_PATH}" ]]; then
  echo "ERROR: CHANGELOG not found: ${CHANGELOG_PATH}" >&2
  exit 1
fi

VERSION="${1:-}"
if [[ -z "${VERSION}" ]]; then
  echo "Usage: $0 <version-tag>" >&2
  echo "Example: $0 v1.1.0" >&2
  exit 1
fi

DATE_STR="$(date +%F)"
OUTPUT_PATH="${REPO_ROOT}/release-notes-${VERSION}.md"

{
  echo "# ${VERSION} 发布说明 / Release Notes"
  echo
  echo "- 发布日期: ${DATE_STR}"
  echo "- 版本标签: ${VERSION}"
  echo
  echo "## 从 CHANGELOG 提取 / Extracted from CHANGELOG"
  echo
  awk '
    BEGIN { in_block=0 }
    /^## \[Unreleased\]/ { in_block=1; next }
    /^## \[/ && in_block==1 { exit }
    in_block==1 { print }
  ' "${CHANGELOG_PATH}"
  echo
  echo "## 模板补全区 / Template"
  echo
  cat "${TEMPLATE_PATH}"
} > "${OUTPUT_PATH}"

echo "Release notes generated: ${OUTPUT_PATH}"
