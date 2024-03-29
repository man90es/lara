# Lara Artefact Retrieving Application

[![license](https://img.shields.io/github/license/octoman90/lara)](https://github.com/octoman90/lara)

A command-line application that downloads the latest GitHub Actions artefact from a given repository. It can be used together with [upload-artifact action](https://github.com/actions/upload-artifact) and GitHub webhooks to build a seamless CI/CD flow.

## Usage
When running LARA, you have to provide:
1. A GitHub access token
2. Repo owner's name (for example, "man90es")
3. Repo name (for example, "lara")
4. (Optional) File name or destination path (for example, "build.zip" or "~/Desktop/build.zip")

### Getting a GitHub token
To generate an access token, go to your [GitHub Developer Settings](https://github.com/settings/tokens). The default token settings are enough for LARA to work for public repositories, but for private repositories you'd have to select 	`All repositories` under `Repository access` and then grant `Read-only` `Actions` access under `Permissions`. You may also want to set the expiration date as far in the future as possible.

### Default file name
If file name or destination path isn't provided, the file will be downloaded into the current directory under the name specified in the workflow file.

### Example launch command:
```sh
GH_TOKEN="github_pat_xxx" ./lara.py man90es lara dist.zip
```

## Contributing
All pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
