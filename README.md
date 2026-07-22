# Valegends

A single-file story / survival game. Open **`valegends.html`** in any browser — no install, no build.

## Play
- **WASD / arrows** — travel between locations
- **E** (or Space) — interact (the gold `Press [E] to…` prompt)
- **F** — eat food from your bag
- **I** — hero sheet & inventory · **M** — map hint

Pick one of 12 heroes (each has a signature skill), then rekindle the Sunwell:
gather **Iron Ore** (mine), **Sunstone** (volcano) and a **Chronicle Page** (library),
then activate the **Portal Ruin**. Watch health & stamina — running out of stamina
drains health, so forage, fish, cook and rest.

## Art
Scenes and heroes are drawn as **layered SVG** (a cohesive illustrated-vector style),
so the game runs with zero external files. The HUD (heart/health bar, lightning/stamina
bar, round compass, gold prompt, location label) matches the reference sheets.

### Dropping in your own painted artwork (exact-quality upgrade)
Every location and every hero has an **image slot**. To use real painted images
instead of the drawn scene, put the file next to `valegends.html` (e.g. in an
`assets/` folder) and set the path in the code:

- **Locations** — in the `WORLD` object, set `img:'assets/lake.png'` on any place.
  When `img` is set it renders that image instead of the SVG — no other changes needed.
- **Heroes** — in the `HEROES` array, set `portrait:'assets/paladin.png'` on any hero.

That's the whole upgrade path: drop a file in, add one path, and that scene/hero
becomes your exact artwork at full quality.
