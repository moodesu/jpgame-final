# Publishing guide images (JP-Game V2)

The repository includes a small **standard-library Python** utility to take an annotated image on your own computer all the way through to the Netlify V2 preview.

## First-time setup

Clone the repository, if you have not already:

```powershell
git clone https://github.com/moodesu/jpgame-final.git
cd jpgame-final
git switch v2-refresh
```

If your local clone is already set up, start from its root and run `git switch v2-refresh` followed by `git pull --ff-only`.

You need Python 3 and Git, plus working GitHub push credentials for the repository. Netlify already builds pushes to `v2-refresh` automatically.

## Publish the annotated A350 overhead screenshot

Download `a350_overhead_precise_annotations.png` from the ChatGPT conversation onto your computer, then run **one command** from the repository root:

```powershell
python scripts/publish_guide_image.py a350-overhead "C:\Users\YOURNAME\Downloads\a350_overhead_precise_annotations.png"
```

On Manjaro, use the corresponding Linux file path:

```bash
python scripts/publish_guide_image.py a350-overhead ~/Downloads/a350_overhead_precise_annotations.png
```

The script:

1. Checks that you are on `v2-refresh`, have no unrelated staged files, and the source is a PNG.
2. Copies the original PNG *without resampling or changing any pixels* to `content/blog/inibuilds-a350-full-flight-tutorial/a350-overhead-precise-annotations.png`.
3. Ensures `{{< a350-overhead-image >}}` is present under the cold-and-dark section.
4. Stages **only** the image and, if modified, the article; commits them.
5. Pushes to `origin/v2-refresh`, which triggers the existing Netlify build.

The Hugo shortcode only displays the image if the page-bundle file exists, so the site does not show a broken placeholder when the file is absent.

## Safe options

`--dry-run` previews what would happen without writing files. `--no-push` commits locally but does not push. `--replace` is required to overwrite an existing image with different contents.

A new guide/image can be added by extending the `PRESETS` dictionary in `scripts/publish_guide_image.py`; no Python dependencies are required.

## Check the deployment

- A350 guide: https://v2-refresh--jp-gamer.netlify.app/blog/inibuilds-airbus-a350-full-flight-tutorial/
- Netlify dashboard: https://app.netlify.com/projects/jp-gamer

A successful Git push starts the Netlify build but **does not alone prove a successful deployment**. Confirm its latest deploy is ready and that the page shows the image.

## Current limitation

The connected GitHub text actions cannot directly read a binary image from ChatGPT's container. The low-level GitHub blob API accepts base64 bytes, but the current integration cannot hand off container file bytes to that operation directly. Until that bridge exists, the local publisher is the reliable upload path.
