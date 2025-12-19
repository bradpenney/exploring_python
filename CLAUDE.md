# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

This is a Material for MkDocs site teaching Python programming from fundamentals through advanced topics. The site serves as a teaching tool, portfolio, and reference for learners at all levels.

## Important Preferences

**Git Operations**: The user handles all git operations (commits, pushes, etc.) themselves. Do not commit or push changes.

## Project Structure

- `docs/` - Markdown content organized by skill level
  - `basics/` - Fundamental Python concepts
    - `data_types/` - Strings, integers, floats, booleans, None
    - `control_structures/` - If statements, loops, functions, comprehensions
    - `data_structures/` - Lists, tuples, dictionaries, sets, slicing
  - `intermediate/` - Intermediate topics (planned expansion)
  - `advanced/` - Advanced topics (planned)
- `mkdocs.yaml` - Site configuration and navigation
- `pyproject.toml` - Poetry dependencies (if present)

## Common Commands

```bash
# Install dependencies (if using Poetry)
poetry install

# Serve locally (http://localhost:8000)
poetry run mkdocs serve
# OR if not using Poetry:
mkdocs serve

# Build static site
mkdocs build
```

## Content Guidelines

### Tone and Style

Articles must balance **playfulness with professionalism** and be **technically accurate** while remaining **accessible**. The goal: meaningful for beginners, yet useful for experienced Python developers reviewing fundamentals.

**Core Principles:**

- **Strong openings**: Ground in real-world scenarios (data processing, web apps, automation scripts, everyday programming tasks)
- **Professional yet engaging**: Use wit in parentheticals and asides, not emoji spam (limit to 1-3 per article, used strategically)
- **Technical rigor**: Include formal definitions where appropriate, Python version context, and precise terminology
- **Structured learning**: Build from simple to complex examples; use clear section headers
- **Thoughtful closings**: Tie concepts to broader Python philosophy or programming concepts; avoid jokey endings
- **Direct voice**: Address reader as "you"; be confident but not arrogant; educational but not preachy
- **Practical focus**: Python is a practical language—show real use cases, not just abstract examples

**Required Sections:**

1. Opening paragraph(s) - hook with real-world relevance
2. Formal definition (if applicable) - clear explanation of what the concept is
3. Simple examples building to complex - start basic, layer complexity
4. "Why [Topic] Matters" section - practical importance in real Python programming
5. Practice Problems with full solutions (use `??? question` and `??? tip`)
6. "Key Takeaways" table - summarize essential points
7. "Further Reading" section with links to official docs, PEPs, quality resources
8. Closing paragraph(s) - thoughtful reflection on broader significance
9. Video Summary (when available) - embedded YouTube tutorial

**Examples of Good Tone:**
- "This is why Python developers love list comprehensions." (confident assertion)
- "(Spoiler: it's not what you'd think.)" (playful aside in parenthetical)
- "Python's approach to duck typing means we care about what an object can do, not what it is." (precise yet accessible)

**Avoid:**
- Excessive emojis (📋✨🎮😄 scattered everywhere)
- Over-the-top phrases like "amazing!", "incredible!", "mind-blowing!"
- Condescending language or talking down to readers
- Jokey closings that undermine the technical content
- Creating files unless absolutely necessary

### Content Structure

- Articles should be teaching-focused, not just notes
- Use mermaid diagrams for visual concepts (already configured)
- Include practice problems with expandable solutions (`??? question`)
- Cross-link related articles using markdown links
- Use admonitions for tips and callouts:
  - Prefer `??? tip` (collapsible tips) for helpful insights
  - **Avoid** `??? note` or `!!! note` (the "note" style doesn't render well in Material for MkDocs)
- **Code examples must include titles, line numbers, and annotations**:
  - Format: ` ```python title="Descriptive Title" linenums="1" `
  - Example: ` ```python title="List Comprehension with Filter" linenums="1" `
  - The title should describe what the code demonstrates
  - Material for MkDocs provides copy button automatically
  - **Add code annotations** to explain key concepts:
    - Use `# (1)!`, `# (2)!`, etc. for inline annotations
    - After the code block, provide numbered explanations
    - Annotate important lines that explain language features, idioms, or non-obvious logic
    - Example:
      ```python title="F-String Formatting" linenums="1"
      name = "Alice"
      age = 30
      print(f"Hello, {name}! You are {age} years old.")  # (1)!
      ```

      1. F-strings automatically convert variables to strings and embed them—no need for str() casting
- **Markdown list formatting**: Always add a blank line before lists that follow text/bold headers
- Embed YouTube videos at the bottom of articles in a "Video Summary" section using the responsive wrapper class:
  ```markdown
  ## Video Summary

  <div class="video-wrapper">
    <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Descriptive Title" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  ```
  Replace `VIDEO_ID` with the YouTube video ID (from `https://youtu.be/VIDEO_ID`) and provide a descriptive title.

  The `video-wrapper` class is defined in `docs/stylesheets/extra.css` and provides:
  - Full-width responsive embedding (100% width, max 800px)
  - Automatic 16:9 aspect ratio
  - Rounded corners and no border
  - Proper spacing above and below the video

### Python-Specific Guidelines

- **Version awareness**: Note when features were introduced (e.g., "f-strings, introduced in Python 3.6")
- **Pythonic idioms**: Show the "Python way" of doing things, not just what works
- **Common pitfalls**: Call out gotchas (mutable default arguments, late binding in closures, etc.)
- **Official resources**: Link to official Python docs, relevant PEPs when applicable
- **Type hints**: Include type hints in more advanced examples where they add clarity
- **Real examples**: Use realistic variable names and scenarios, not just `foo`, `bar`, `x`, `y`

### Practice Problems

Every article should include 2-4 practice problems:

- Use `??? question "Practice Problem N: Descriptive Title"`
- Provide solutions in nested `??? tip "Answer"` blocks
- Problems should test understanding, not just memorization
- Build from basic recall to application
- Include explanation in answers, not just code

Example:
```markdown
??? question "Practice Problem 1: String Indexing"

    What does `"Python"[-1]` return?

    ??? tip "Answer"

        It returns `'n'` - the last character. Negative indexing counts from the end, with -1 being the last element.
```

### Key Takeaways Format

End each article with a table summarizing core concepts:

```markdown
## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **List** | Mutable, ordered sequence of items |
| **Mutability** | Lists can be modified after creation |
| **Indexing** | Access elements by position (0-indexed) |
```

## Working with This Repository

- Read existing content before modifying to match established tone
- Preview changes locally with `mkdocs serve` before committing
- Keep navigation in `mkdocs.yaml` organized and logical
- Ensure all internal links work (Material for MkDocs will warn about broken links)
