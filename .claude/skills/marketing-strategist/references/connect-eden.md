# Connecting Eden, and handling limits

What to do when the Eden tools are missing, the connection breaks, or the user runs out of credits. Never just point at a marketing page; walk the user through the fix right here in chat.

## No `eden_*` tools available

The user hasn't connected the Eden MCP yet. Give them the exact steps for where they're running you, then have them say "build my promotion kit" again once connected.

**First:** if they don't have an Eden account, they need one (free to start): https://app.eden.so

**claude.ai or Claude Desktop**: give them this link and these steps:

1. Open: https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Eden&connectorUrl=https%3A%2F%2Fmcp.eden.so%2Fmcp
   (It opens Claude's connector settings with Eden pre-filled. They just click Add.)
2. Sign in with their Eden account when the small window appears, and approve.
3. Back in the chat: click the tools / connectors icon in the message box and switch Eden on.
4. Say "build my promotion kit" again.

Alternative path: in Eden itself, Settings, then Integrations, then "Add to Claude". Same result.

**Claude Code**: run:

```
claude mcp add --transport http eden https://mcp.eden.so/mcp
```

Then `/mcp` to sign in to Eden, and re-run the kit.

**Codex**: run:

```
codex mcp add eden --url https://mcp.eden.so/mcp
codex mcp login eden
```

They finish the sign-in in the browser tab that opens (Eden returns them to Codex on its own). Codex only loads MCP tools when it starts, so have them restart Codex once, then re-run the kit.

**Any other MCP client**: add a custom MCP server: URL `https://mcp.eden.so/mcp`, transport Streamable HTTP, auth OAuth. Sign in with their Eden account.

## Tools exist but calls fail with auth errors

Errors like "OAuth authorization required", "Unauthorized", "auth-expired", or a session error mean the connection went stale (this happens after server restarts). The fix is to reconnect, not to retry:

- claude.ai / Desktop: Settings, Connectors, find Eden, reconnect or re-authenticate. Then re-run.
- Claude Code: `/mcp` and re-authenticate Eden.

Tell the user plainly: "The Eden connection expired. Reconnect it and say build my promotion kit; I'll pick up where we left off."

## The draft close fails with a write or scope error

`eden_schedule_post` drafts (and the note writes the kit depends on) need a write-scoped connection. If a write returns `status: "read-only-token"` or a permissions error, don't fight it: save the draft as a note fallback if notes work, or hand the user the draft text directly, and tell them in one line that removing and re-adding the Eden connector with write access enables one-step drafting next time. If note writes themselves fail, deliver the kit in chat or as a file and say the Eden copy is missing.

## Out of credits mid-run

Eden research tools spend credits from the user's Eden plan. When they run out, the tool returns a structured error instead of results:

```json
{
  "ok": false,
  "status": "out_of_credits",
  "message": "...",
  "upgradeRequired": true,
  "upgradeUrl": "..."
}
```

When you see `status: "out_of_credits"`:

1. **Stop making research calls immediately.** Retrying spends nothing and returns the same error.
2. **Deliver the kit you can stand behind from what you already have.** Diagnose from the inputs alone, say the market read is unresearched, and label the kit partial in one line at the top: "Ran out of Eden research credits partway through, so this kit's market diagnosis is inferred, not researched."
3. **Give the user the way out, once, without nagging.** Use the `upgradeUrl` from the error payload as the link. One line: "To get researched diagnoses, add credits or upgrade here: <upgradeUrl>." If the payload has no link, use https://app.eden.so/?settings=billing
4. Still save the kit note to the "Promotion" board if note writes are working; the kit and its log cost nothing extra to keep consistent.

Never fake a market finding to fill the diagnosis, and never end the run with only an error message. The user should always get the best kit the remaining data supports, plus one clear line about what happened and the link.

## Any other tool failure

Read the structured error. `invalid` means fix your input and don't retry the same call. `unreachable` means retry once. Anything else: note it in one line under the diagnosis ("couldn't check X this run") and keep going. One broken call never cancels the run.
