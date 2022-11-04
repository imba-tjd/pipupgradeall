# Pip Upgradeall

I have been using `Function PipUpgradeall { pip list -o --format=freeze | % {pip install -U $_.split("=")[0]} }` to do pip-upgradeall for a long time. However pip 22.3 disabled this function saying `ERROR: List format 'freeze' can not be used with the --outdated option`. See https://github.com/pypa/pip/pull/11482

So I have to parse `pip list -o` manually. It turns out usable.

Usage:

```bash
pip install git+https://github.com/imba-tjd/pipupgradeall
pipupgradeall
```
