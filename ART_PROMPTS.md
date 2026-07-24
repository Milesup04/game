# Valegends — Art Generation Kit

Everything here is written so the art you generate (Gemini, Midjourney, DALL·E, etc.)
**matches across the whole game** and **drops into the engine with no rework**.

The secret to a "one world" look is that every asset shares **three constants**:

1. **One style** — copy the STYLE ANCHOR into *every* prompt.
2. **One light direction** — light always comes from the **upper-left**.
3. **One background** — generate on a **plain flat background** (ideally transparent, else
   solid chroma green `#00b140`) so I can cut it out perfectly.

If you can only change one thing over what you have now: generate on a **transparent or
solid single-colour background** — that alone removes the ragged cut-out edges.

---

## 🔑 STYLE ANCHOR — paste into every prompt

> painterly storybook fantasy game art, hand-illustrated, warm earthy colours, soft
> cel-shading with clean dark outlines, gentle top-left light source with soft shadows,
> consistent proportions, high detail, cohesive art style, no text, no watermark,
> no UI, no border, no frame

## 🔑 BACKGROUND / FRAMING RULE — paste into every prompt

> full subject centred, isolated on a plain solid chroma-green background (#00b140),
> no scenery, no ground, no shadow on the background, even flat lighting on the backdrop

(If your generator supports transparent PNG output, ask for that instead of chroma-green —
even cleaner.)

---

## 1) PLAYER CHARACTERS  (highest impact)

Generate each hero in **three poses** so they turn as they walk: **front, side, back.**
Same character, same outfit, same scale in all three.

**Framing rule for characters (add this):**
> full body head-to-toe, standing straight, feet at the very bottom of the frame,
> small even margin, character fills ~80% of frame height, 3/4 top-down game camera angle

**Template** (swap the description):

> A `<HERO DESCRIPTION>`, `<POSE>` view, standing.
> [STYLE ANCHOR] [BACKGROUND RULE] [CHARACTER FRAMING]

`<POSE>` = `front-facing` · `left-side profile, facing left` · `back view, facing away`

**The three heroes to (re)generate** — keep them recognisable to your existing ones:

- **Herbalist** — `a young forest herbalist in a green tunic and brown travel cloak,
  leather boots, holding a bundle of herbs, a small satchel of potions at the hip`
- **Vanguard** — `an armoured knight in polished steel plate with a tabard, sword sheathed,
  a shield on the back, helmet under one arm`
- **Shadow-Stepper** — `a hooded rogue in dark leather armour, twin daggers, a cloak,
  face half-shadowed under the hood`

> Deliver 9 files: `<hero>_front`, `<hero>_side`, `<hero>_back` for each of the three.
> I slot them into `assets/sprites/` — the engine already flips the side view for
> left/right, so you only need the character facing **one** side.

---

## 2) VILLAGERS / NPCs

Single **front-facing** pose each (they don't walk far). Same template as characters
but `front-facing` only.

Prompts (one each): **Blacksmith** `a stout blacksmith in a leather apron holding a hammer` ·
**Innkeeper** `a friendly innkeeper/cook in an apron and white cap holding a tray` ·
**Merchant/Trader** `a travelling merchant with a pack of wares and coin pouches` ·
**Mayor** `a dignified town mayor in a fine red robe with a chain of office` ·
**Alchemist** `an alchemist in a work apron holding a glowing potion flask` ·
**Scholar** `a robed scholar holding an open glowing tome` ·
**Gravekeeper** `a solemn gravekeeper in dark hooded robes with a lantern` ·
**Old Angler** `a weathered old fisher in a sun hat with a rod and basket` ·
**Forester** `a woodland hunter/forester with a longbow and quiver`

> 9 files → `assets/npcs/`.

---

## 3) ENEMIES / BESTIARY

Front or 3/4 **facing the camera**, menacing, same template.

**Wolf** `a snarling grey dire wolf` · **Goblin** `a small green goblin with a crude dagger` ·
**Skeleton** `an undead skeleton warrior with a rusty sword` · **Zombie** `a shambling
rotted zombie` · **Giant Spider** `a large hairy black spider, front view` · **Slime**
`a cute translucent green slime blob with a sad face` · **Bandit** `a rough human bandit
in leathers with a hood` · **Ghost** `a translucent pale spectre floating` · **Ogre**
`a huge brutish ogre with a club` · **Minotaur (BOSS)** `a towering fearsome minotaur
with great horns and a massive axe, imposing`

> 10 files → `assets/enemies/`. Keep the Minotaur clearly the biggest/scariest — it's the boss.

---

## 4) BUILDINGS & PROPS

These sit on the ground, so use a **3/4 top-down oblique** angle (like a tabletop
diorama piece), same light from upper-left.

**Framing rule for buildings (add this):**
> single building, 3/4 top-down oblique diorama view, sitting flat, base of the building
> at the bottom of the frame, [BACKGROUND RULE]

Prompts you'll want (match your current set): `a cosy timber-framed village inn` ·
`a stone town hall with a flag` · `a blacksmith forge with an anvil and chimney smoke` ·
`a small stone chapel` · `a stone village well` · `a colourful market stall with produce` ·
`a thatched cottage` (make 2–3 variants) · `a wooden fishing dock over water` ·
`a tiered stone fountain` · `an ancient carved stone pylon gate` · `a crumbling stone
ruin arch` · `a stone bell tower` · `a glowing magic portal in a stone frame` ·
plants: `an apple orchard tree` · `a great oak` · `a weeping willow` · `a berry bush
heavy with fruit` · `a patch of glowing blue mushrooms` · `a wheat field tile` ·
`a vegetable garden patch`

> Files → `assets/structures/`. Keep filenames matching the ones already in that folder
> and I re-wire nothing — they just get sharper.

---

## 5) GROUND TILES  (makes the floor look real)

These must be **seamless / tileable** so they repeat with no visible seams. Square,
top-down, flat.

**Template:**
> a seamless tileable top-down `<TERRAIN>` texture for a game map, flat overhead view,
> repeating pattern, no shadows, no objects, even lighting, high detail
> [STYLE ANCHOR minus the light line]

`<TERRAIN>` = `lush green grass` · `worn dirt path` · `dry desert sand` · `grey stone
cobble` · `dark forest floor with roots` · `cracked volcanic rock` · `shallow clear water`

> Deliver as 512×512 (or 1024) squares → put in `assets/tiles/`. I'll swap the CSS-drawn
> ground for a real tiled floor using these. This is the single biggest "not a flat
> backdrop" upgrade after characters.

---

## How to hand them to me

1. Generate, then (if not transparent) leave them on the flat chroma-green — **don't** crop
   them yourself; my slicer handles it cleanly when the background is uniform.
2. Upload into the matching `assets/` subfolder on the `claude/story-game-design-3oxdci`
   branch (or just dump them in `assets/` and tell me what's what).
3. Say "new art is in" — I cut out the backgrounds, drop each into its slot, rebuild the
   single-file game, and send it back. **Zero code changes needed from you.**

### Batch tip
Most generators let you make a **sheet** (e.g. "6 characters in a row, same style, evenly
spaced, chroma-green background"). That's fine — I already have the slicer that detects
and separates grid sheets, exactly like your original Valegends sheets. So one big sheet
per category works great and saves you time.

---

### Priority order (biggest visual payoff first)
1. **Ground tiles** (§5) — kills the "flat backdrop" feel instantly
2. **Player characters** (§1) — the thing you look at most
3. **Enemies** (§3) — combat readability
4. **Buildings** (§4) and **NPCs** (§2) — sharpen what's already decent
