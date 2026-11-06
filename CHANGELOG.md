# Changelog

One line per version of `data/taglines.json`, newest first. Each version that reaches `main` is tagged `data-vX.Y.Z`, so `git show data-v1.0.0:data/taglines.json` returns exactly what shipped.

## How versions bump

- **Major:** something existing breaks. A field is removed, renamed, changes type, or changes meaning. Ships with a new `/v2/` API path.
- **Minor:** something is added. A season, a franchise, a housewife, or a new optional field.
- **Patch:** corrections only. A reworded line, or a line moved to the right season.

## Versions

- 1.11.0 (2026-11-06): ties five themes to seasons, RHOC S1–S3, RHOA S1–S2, RHOD S1–S5 and RHODC S1 from IMDb's per-episode credits and RHOM S2–S4 from Bravo, and adds `listen_url` links for the RHOBH, RHOM and RHOD themes.
- 1.10.0 (2026-11-05): adds Ramona Singer's eye color, dark brown, sampled from two Bravo pages.
- 1.9.0 (2026-11-05): adds optional `eye_color` on housewives, for the housewife dollz: one of 12 colors, how it was decided, and the article pages it was read from. Six housewives so far. The v2 housewife resource carries it, or `null`.
- 1.8.0 (2026-11-02): adds `themes` for RHOD and RHODC from IMDb, and for RHOM from Bravo: Adriana de Moura's "Feel the Rush", the first theme with a title and vocals.
- 1.7.0 (2026-11-02): adds RHOSLC S7, 7 taglines.
- 1.6.0 (2026-11-02): adds RHOD S1–S5 and RHODC S1, 34 taglines. Both shows have ended, so both are complete.
- 1.5.0 (2026-11-01): adds `themes`, intro theme music credits from IMDb for RHOSLC, RHOBH, RHONY, RHOC and RHOA. Adds `intro_order`, each season's opening-credits order with the closer last, filled in only for seasons a rewatch has confirmed. RHOM S7 is the first.
- 1.4.0 (2026-11-01): adds RHOM S1–S7, RHODubai S1–S2 and RHORI S1, 61 taglines. Miami gets a second era, a revival from S4.
- 1.3.0 (2026-10-29): adds `id`, a stable three-word id, to every franchise, era, housewife and tagline. Ships the PokeAPI-shaped `/v2/` API alongside `/v1/`.
- 1.2.0 (2026-10-29): adds RHOP S1–S11, RHOC S1–S20, RHONJ S1–S14 and RHOA S1–S17, 359 taglines.
- 1.1.0 (2026-10-28): adds `premieres`, each season's US premiere date from Wikipedia's episode lists; season API files gain a `premiere` field.
- 1.0.0 (2026-10-26): RHOSLC S1–S6, RHOBH S1–S15 and RHONY S1–S16, 229 taglines.
