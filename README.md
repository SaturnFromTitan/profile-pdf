# Profile

This repo contains code to generate my profile/CV via HTML/CSS and WeasyPrint.
It also hosts my profile under [pythomation.de](http://pythomation.de).

The layout is heavily inspired by [Ben Oertel](https://www.benoertel.com/).

## Execution

The following prerequisites have to be installed:

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python Package Manager)
- [just](https://github.com/casey/just) (Command Runner)

Now you can render the profile via

```bash
just generate-pdf
```

The file will be available in `public/profile.pdf`.
