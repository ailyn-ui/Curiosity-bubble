# Connecting Eden, and handling limits

What to do when the Eden tools are missing, the connection breaks, or the user runs out of credits mid-session. Never just point at a marketing page; walk the user through the fix right here in chat.

## No `eden_*` tools available

The user hasn't connected the Eden MCP yet. Give them the exact steps for where they're running you, then have them say "outline my next piece" again once connected.

**First:** if they don't have an Eden account, they need one (free to start): https://app.eden.so

**claude.ai or Claude Desktop**: give them this link and these steps:

1. Open: https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Eden&connectorUrl=https%3A%2F%2Fmcp.eden.so%2Fmcp
   (It opens Claude's connector settings with Eden pre-filled. They just click Add.)
2. Sign in with their Eden account when the small window appears, and approve.
3. Back in the chat: click the tools / connectors icon in the message box and switch Eden on.
4. Say "outline my next piece" again.

Alternative path: in Eden itself, Settings, then Integrations, then "Add to Claude". Same result.

**Claude Code**: run

```
claude mcp add --transport http eden https://mcp.eden.so/mcp
```

Then `/mcp` to sign in to Eden, and say "outline my next piece" again.

**Codex**: run:

```
codex mcp add eden --url https://mcp.eden.so/mcp
codex mcp login eden
```

They finish the sign-in in the browser tab that opens (Eden returns them to Codex on its own). Codex only loads MCP tools when it starts, so have them restart Codex once, then say "outline my next piece" again.

**Any other MCP client**: add a custom MCP server: URL `https://mcp.eden.so/mcp`, transport Streamable HTTP, auth OAuth. Sign in with their Eden account.

## Tools exist but calls fail with auth errors

Errors like "OAuth authorization required", "Unauthorized", "auth-expired", or a session error mean the connection went stale (this happens after server restarts). The fix is to reconnect. Retrying does nothing:

- claude.ai / Desktop: Settings, Connectors, find Eden, reconnect or re-authenticate. Then re-run.
- Claude Code: `/mcp` and re-authenticate Eden.

Tell the user plainly: "The Eden connection expired. Reconnect it and say outline my next piece; I will pick up where we left off, the outline note keeps our progress."

## The outline note fails with a write or scope error

Creating the board and writing the outline note (`eden_create_board`, `eden_create_note`, `eden_update_note`) need a write-scoped connection. If a write returns `status: "read-only-token"` or a permissions error, do not fight it: hand the user the full outline as markdown in chat (or a file if you can write one), and tell them in one line that removing and re-adding the Eden connector with write access lets the outline land on their board next time.

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
2. **Finish the outline from what you already have.** The interview, stress test, and route do not need research credits; only packaging research does. Build the package from the title families in `references/craft-reference.md` and add one line at the top of the Package section: "Ran out of Eden research credits before packaging research, so these titles come from craft families rather than a market read."
3. **Give the user the way out, once, without nagging.** Use the `upgradeUrl` from the error payload as the link. One line: "To get full runs, add credits or upgrade here: <upgradeUrl>." If the payload has no link, use https://app.eden.so/?settings=billing
4. Still save the outline note to the "Long-form outlines" board if note writes are working; notes and settings cost nothing extra.

Never invent a market read, and never end the session with only an error message. The user should always get a complete outline, honestly labeled, plus one clear line about what happened and the link.

## Any other tool failure

Read the structured error. `invalid` means fix your input and don't retry the same call. `unreachable` means retry once. Anything else: note it in one line in the Market signal block ("could not search X") and keep going. One broken call never cancels the session.
