# Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a *lightweight*, HTML-like language that lets us format text, insert images, and create documents. This means that you won't, for example, highlight a word and find the **bold** button in a menu bar. Instead, you will use Markdown notation to indicate what formatting you would like. Once you learn Markdown, you'll start to see it everywhere - README files on GitHub, note-taking apps, documentation, and of course, Jupyter notebooks.

```{margin} History of Markdown
Markdown was created in 2004 by John Gruber of [Apple blogging fame](https://daringfireball.net) and Aaron Swartz. You should be aware of [Aaron Swartz's tragic story](https://en.wikipedia.org/wiki/Aaron_Swartz), if you aren't already.
```

## Why Markdown?

In this class, you'll use Markdown to:
- Write explanations alongside your Python code in Jupyter notebooks
- Create professional-looking reports that combine code, output, and analysis
- Document your projects with README files
- Take notes that include formatted text, code snippets, and math equations

## Basic Syntax

### Headers

Use `#` symbols to create headers. More `#` symbols = smaller headers.

| Markdown | Result |
|----------|--------|
| `# Header 1` | Largest header |
| `## Header 2` | Second level |
| `### Header 3` | Third level |

### Text Formatting

| Markdown | Result |
|----------|--------|
| `**bold text**` | **bold text** |
| `*italic text*` | *italic text* |
| `***bold and italic***` | ***bold and italic*** |
| `` `code` `` | `code` |

### Lists

**Unordered lists** use `-`, `*`, or `+`:

```markdown
- First item
- Second item
  - Nested item
  - Another nested item
- Third item
```

**Numbered lists** use numbers:

```markdown
1. First step
2. Second step
3. Third step
```

### Links and Images

**Links:**
```markdown
[Link text](https://www.example.com)
```

Example: `[Elon University](https://www.elon.edu)` creates [Elon University](https://www.elon.edu)

**Images:**
```markdown
![Alt text](path/to/image.png)
```

### Code

For **inline code**, use single backticks: `` `print("hello")` `` renders as `print("hello")`.

For **code blocks**, use triple backticks with an optional language identifier:

````markdown
```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
```
````

This renders as:

```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
```

### Blockquotes

Use `>` for quotes:

```markdown
> This is a blockquote. Great for highlighting
> important information or citing sources.
```

> This is a blockquote. Great for highlighting important information or citing sources.

## Math and Equations

This is especially important for finance! Markdown supports LaTeX math notation.

### Inline Math

Use single dollar signs for inline math: `$\mu$` renders as $\mu$.

Examples:
| Markdown | Result |
|----------|--------|
| `$\mu$` | $\mu$ (mean) |
| `$\sigma$` | $\sigma$ (standard deviation) |
| `$\beta$` | $\beta$ (beta) |
| `$r_f$` | $r_f$ (risk-free rate) |
| `$R^2$` | $R^2$ (R-squared) |

### Display Equations

Use double dollar signs for centered equations:

```markdown
$$
R_p = \sum_{i=1}^{n} w_i R_i
$$
```

Renders as:

$$
R_p = \sum_{i=1}^{n} w_i R_i
$$

### Common Finance Equations

**Sharpe Ratio:**
```markdown
$$
\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
$$
```

$$
\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
$$

**CAPM:**
```markdown
$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$
```

$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$

**Portfolio Variance (two assets):**
```markdown
$$
\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12}
$$
```

$$
\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12}
$$

## Tables

Create tables using pipes `|` and hyphens `-`:

```markdown
| Asset | Weight | Return |
|-------|--------|--------|
| AAPL  | 0.40   | 12.5%  |
| MSFT  | 0.35   | 10.2%  |
| GOOG  | 0.25   | 8.7%   |
```

Renders as:

| Asset | Weight | Return |
|-------|--------|--------|
| AAPL  | 0.40   | 12.5%  |
| MSFT  | 0.35   | 10.2%  |
| GOOG  | 0.25   | 8.7%   |

## Jupyter Book Special Features

Since our course notes use Jupyter Book, you have access to some extra features:

### Notes and Warnings

```markdown
```{note}
This is a helpful note for students.
```
```

```{note}
This is a helpful note for students.
```

```markdown
```{warning}
Be careful about this common mistake!
```
```

```{warning}
Be careful about this common mistake!
```

### Tips

```markdown
```{tip}
A useful tip for your workflow.
```
```

```{tip}
A useful tip for your workflow.
```

## Practice in VS Code

In VS Code (and Codespaces), you can:

1. **Preview Markdown**: Right-click on a `.md` file and select "Open Preview" (or use `Cmd+Shift+V` on Mac, `Ctrl+Shift+V` on Windows)

2. **Side-by-side editing**: Use `Cmd+K V` to see your Markdown and preview side by side

3. **In Jupyter notebooks**: Double-click a Markdown cell to edit it, then `Shift+Enter` to render it

## Resources

Here's a Markdown [cheatsheet](https://www.markdownguide.org/cheat-sheet/) - bookmark this! You'll get the hang of it very quickly.

The [Markdown Section from Coding for Economists](https://aeturrell.github.io/coding-for-economists/wrkflow-markdown.html) is excellent and goes into more detail.

For LaTeX math symbols, this [reference guide](https://en.wikibooks.org/wiki/LaTeX/Mathematics) is comprehensive.

You can read more about how to use [VS Code and Markdown](https://code.visualstudio.com/docs/languages/markdown).
