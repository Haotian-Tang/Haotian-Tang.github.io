# Haotian Tang's personal website

Live website: https://haotian-tang.github.io/

A lightweight academic website hosted on GitHub Pages. The pages share one
layout and stylesheet; no external fonts or JavaScript libraries are required.

## Update content

1. Edit the corresponding `.Rmd` file. Each page contains JSON-quoted YAML
   metadata and a single raw HTML block.
2. Replace `Resume.pdf` when updating the CV.
3. Run `python3 scripts/build_site.py` from any directory. This builds all six
   HTML pages, the old `publication.html` redirect, and `sitemap.xml`.
4. Preview with `python3 -m http.server 8000` from the repository root, then open
   `http://localhost:8000`.
5. Commit the source files and generated HTML together. GitHub Pages serves the
   checked-in HTML; no deployment service or build dependencies are needed.

`_templates/page.html` owns the shared navigation, metadata, and footer.
`styles.css` owns all styling. Keep factual updates consistent across the home,
research, experience, and publications pages.

The page sources can also be rendered with R Markdown using the custom template
in `_site.yml`. The Python builder is the simplest way to regenerate the complete
site, including the legacy redirect and sitemap. Do not edit generated HTML
directly.

## Page structure

- `index.Rmd`: introduction, current research, and selected publications.
- `research.Rmd`: current projects and individual contributions.
- `publications.Rmd`: preprint, peer-reviewed articles, and conference abstract.
- `experience.Rmd`: research and teaching roles, plus an education overview.
- `education.Rmd`: degrees and technical skills.
- `teaching.Rmd`: teaching experience.

Existing education, teaching, and publication URLs are preserved.
