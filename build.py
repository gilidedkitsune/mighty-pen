#!/usr/bin/env python3
"""
Generate the mighty-pen marketplace from the LIVE skills in
~/.claude/skills/. Re-run this after editing any skill, then commit + push.

    python3 build.py [version]      # default version 1.0.0

Why this exists: installed plugins live in a cache dir, not ~/.claude/skills/,
and cannot reach files outside their own plugin root. So every cross-skill path
inside a SKILL.md must be rewritten to the ${CLAUDE_PLUGIN_ROOT} form. This
script copies the skills into the plugin layout and does that rewrite, so the
live skills stay the single source of truth.

The plugin marketplace is the ONLY distribution channel. The claude.ai
Shared Skills library was retired Jul 6 2026 (uploads there went stale
between deploys and duplicate copies hijacked skill triggers in desktop
sessions). Do not re-add an upload step.
"""
import os, sys, shutil, json

HOME = os.path.expanduser("~")
SRC  = os.path.join(HOME, ".claude", "skills")
REPO = os.path.dirname(os.path.abspath(__file__))
VERSION = sys.argv[1] if len(sys.argv) > 1 else "1.0.0"

KIT = ["quill", "tone-and-guidelines", "voice-profiles",
       "no-slops", "content-formats",
       "ogilvy-copywriting", "seo-geo", "blog", "aeo-craft"]
STANDALONE = ["red-pen"]
RESEARCH = ["cited-works"]

EXCLUDE_NAMES  = {".last-source-check", ".DS_Store", "__pycache__", ".git"}
EXCLUDE_SUFFIX = (".pyc",)

def ignore(_dir, names):
    return [n for n in names if n in EXCLUDE_NAMES or n.endswith(EXCLUDE_SUFFIX)]

def rewrite_md(text, self_name, sibling_names):
    # D: quill's monthly-check tracker -> a writable, persistent spot
    #    (the plugin cache is volatile and changes on every update)
    text = text.replace("~/.claude/skills/quill/.last-source-check",
                        "~/.claude/.quill-last-source-check")
    # A: absolute sibling/own refs -> plugin root (leaves ~/.config/claude-seo alone)
    text = text.replace("~/.claude/skills/", "${CLAUDE_PLUGIN_ROOT}/skills/")
    # C: short-form sibling refs  `<skill>/...  ->  `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/...
    for name in sibling_names:
        text = text.replace("`" + name + "/",
                            "`${CLAUDE_PLUGIN_ROOT}/skills/" + name + "/")
    # B: bare own refs  `references/... and `scripts/...  ->  plugin-root self paths
    text = text.replace("`references/",
                        "`${CLAUDE_PLUGIN_ROOT}/skills/" + self_name + "/references/")
    text = text.replace("`scripts/",
                        "`${CLAUDE_PLUGIN_ROOT}/skills/" + self_name + "/scripts/")
    return text

def copy_skill(src_skill_dir, dest_skills_dir, self_name, sibling_names):
    dst = os.path.join(dest_skills_dir, self_name)
    shutil.copytree(src_skill_dir, dst, ignore=ignore)
    for root, _dirs, files in os.walk(dst):
        for f in files:
            if f.endswith(".md"):
                p = os.path.join(root, f)
                with open(p, encoding="utf-8") as fh:
                    t = fh.read()
                t2 = rewrite_md(t, self_name, sibling_names)
                if t2 != t:
                    with open(p, "w", encoding="utf-8") as fh:
                        fh.write(t2)

def build_plugin(plugin_name, skill_list, description):
    pdir = os.path.join(REPO, "plugins", plugin_name)
    if os.path.exists(pdir):
        shutil.rmtree(pdir)
    os.makedirs(os.path.join(pdir, ".claude-plugin"))
    skills_dir = os.path.join(pdir, "skills")
    os.makedirs(skills_dir)
    for s in skill_list:
        copy_skill(os.path.join(SRC, s), skills_dir, s, skill_list)
    plugin_json = {
        "name": plugin_name,
        "description": description,
        "version": VERSION,
        "author": {"name": "Taylor"},
    }
    with open(os.path.join(pdir, ".claude-plugin", "plugin.json"), "w") as fh:
        json.dump(plugin_json, fh, indent=2)
        fh.write("\n")
    print("  built plugin %-18s (%d skills)" % (plugin_name, len(skill_list)))

def main():
    build_plugin("fresh-ink", KIT,
        "The make-it kit: routing spine, brand voice, personas, content formats, "
        "Ogilvy, slop audit, and SEO/GEO data for written content.")
    build_plugin("red-pen", STANDALONE,
        "The fix-it tool: a tough, exacting copyeditor with verdict-first review, "
        "quick-fix or full report, and concreteness scoring.")
    build_plugin("cited-works", RESEARCH,
        "The find-it tool: a research assistant with newsroom-strict sourcing. Traces "
        "every stat to its primary source, dates it, checks it against a do-not-cite "
        "trap list, and delivers a ready-to-use citation.")
    marketplace = {
        "name": "mighty-pen",
        "owner": {"name": "Taylor"},
        "description": "Personal writing and editing skills: research, draft, and edit.",
        "plugins": [
            {"name": "fresh-ink", "source": "./plugins/fresh-ink",
             "description": "The make-it kit: routing spine + craft + voice + personas + formats + SEO/GEO.",
             "version": VERSION},
            {"name": "red-pen", "source": "./plugins/red-pen",
             "description": "The fix-it tool: verdict-first copyedit, quick-fix or full report, concreteness scoring.",
             "version": VERSION},
            {"name": "cited-works", "source": "./plugins/cited-works",
             "description": "The find-it tool: newsroom-strict sourcing, trap-list checks, ready-to-use citations.",
             "version": VERSION},
        ],
    }
    os.makedirs(os.path.join(REPO, ".claude-plugin"), exist_ok=True)
    with open(os.path.join(REPO, ".claude-plugin", "marketplace.json"), "w") as fh:
        json.dump(marketplace, fh, indent=2)
        fh.write("\n")
    print("marketplace built at version %s" % VERSION)

if __name__ == "__main__":
    main()
