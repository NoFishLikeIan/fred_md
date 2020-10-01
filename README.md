# FRED_MD

Import and transform the [FRED](https://research.stlouisfed.org/wp/more/2015-012) monthly data. See [here](https://s3.amazonaws.com/files.fred.stlouisfed.org/fred-md/Appendix_Tables_Update.pdf) for a variable description


## Installing

For now I am not going to publish it on PyPI. If you want to use it in the meantime simply do,

```bash
pip install git+https://github.com/NoFishLikeIan/fred_md
```

should do the trick.

## Usage

The transformations are the suggested ones, taken from [McCracken, 2015](https://s3.amazonaws.com/real.stlouisfed.org/wp/2015/2015-012.pdf).

You can get the raw and the tranformed data as,


```python
from fred_md.ingest_fred import import_transformed_data, import_raw_data

df = import_transformed_data()
raw_df = import_raw_data()
```

The package defaults to the latest version. If you want a specific one, just imput the version as `YYYY-MM`, 


```python
from fred_md.ingest_fred import import_transformed_data, import_raw_data

df = import_transformed_data("2018-02")
raw_df = import_raw_data("2018-02")
```

