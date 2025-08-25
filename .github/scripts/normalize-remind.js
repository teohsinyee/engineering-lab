// Normalizes /remind comments so timezone defaults to SGT and "tmr" → "tomorrow".
// Usage: node .github/scripts/normalize-remind.js
// Prints the path to a rewritten event JSON (or the original event if unchanged).

const fs = require("fs");
const path = require("path");

function hasExplicitTimezone(text) {
  if (!text) return false;
  const tzRegex =
    /\b(SGT|UTC|GMT|WIB|CET|CEST|EET|EEST|IST|PST|PDT|MST|MDT|CST|CDT|EST|EDT|HKT|JST|KST)\b|(?:UTC|GMT)[+-]\d{1,2}(?::?\d{2})?/i;
  return tzRegex.test(text);
}

function normalize(body) {
  if (!body) return body;
  let b = body;

  // Only care about comments that contain /remind
  if (!/\/remind\b/i.test(b)) return b;

  // Expand common shorthand "tmr" → "tomorrow"
  b = b.replace(/\btmr\b/gi, "tomorrow");

  // If no explicit timezone detected, append " SGT"
  if (!hasExplicitTimezone(b)) {
    // Keep it idempotent (avoid double appends)
    if (!/\bSGT\b/i.test(b)) b = `${b} SGT`;
  }

  return b;
}

function main() {
  const eventPath = process.env.GITHUB_EVENT_PATH;
  if (!eventPath || !fs.existsSync(eventPath)) {
    console.error("GITHUB_EVENT_PATH not found.");
    process.exit(1);
  }

  const raw = fs.readFileSync(eventPath, "utf8");
  const payload = JSON.parse(raw);

  // Handle issue_comment events (created/edited). For manual dispatch, pass-through.
  const comment = payload?.comment?.body;
  const newBody = normalize(comment);

  if (!comment || newBody === comment) {
    // No change — return original path
    process.stdout.write(eventPath);
    return;
  }

  // Write a rewritten event file next to RUNNER_TEMP
  const outDir = process.env.RUNNER_TEMP || "/tmp";
  const outPath = path.join(outDir, "event.rewritten.json");

  // Mutate the payload with the normalized body
  payload.comment.body = newBody;
  fs.writeFileSync(outPath, JSON.stringify(payload), "utf8");

  process.stdout.write(outPath);
}

main();
