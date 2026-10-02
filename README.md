# Lab Analysis Platform (LAP)

A Python library for loading, checking, fitting, and plotting
experimental lab data.

**First useful version:** load a lab CSV, validate it, fit a dependent
column vs a chosen independent column, plot data + fit + residuals,
and print parameters with uncertainty.

## Status

Phase 1 is in progress. These pieces already exist:

- Package layout (`src/lap`, `pyproject.toml`, `requirements.txt`)
- CSV loader (`src/lap/data/loader.py`)
- Dataset wrapper (`src/lap/data/dataset.py`)
- Tests for both (`tests/`)
- Sample CSVs (`examples/sample_data/`)

There is no CLI, web UI, or analysis/fitting yet.

## Setup

```bat
cd lab-analysis-platform
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -e .
python -m pip install -r requirements.txt
python -m pytest
```

On PowerShell, activate with `.\.venv\Scripts\Activate.ps1` instead of
`activate.bat`. Use `python -m pip` if `pip` is not on PATH.

## Roadmap

Testing stays with each feature. CI, Docker, and deploy wait until
the library is worth shipping.

### Phase 1 — Analysis engine (the actual product)

Keep this slice narrow: one independent column `x` vs one measured
column `y` (voltage vs current, position vs time, absorbance vs
wavelength, and so on). `examples/sample_data/projectile.csv` is
only a sample, not the only supported experiment. Multiple
independent variables can wait.

- [x] Project setup
- [x] CSV data loader
- [x] Data representation (`Dataset`)
- [ ] Data validation (empty frames, types, independent column)
- [ ] Data cleaning (missing values, basic outlier handling)
- [ ] Statistical summaries (mean, std, count)
- [ ] Model fitting (linear / quadratic via scipy, not a general fitter)
- [ ] Uncertainty (parameter errors from the fit, not a full error engine)
- [ ] Visualization (data + fit + residuals)
- [ ] Small CLI so a CSV can be analyzed from the terminal

### Phase 2 — Interfaces (optional)

Only after Phase 1 can run on a real CSV.

- [ ] REST API
- [ ] Minimal web UI that calls the library
- [ ] Database / saved runs (skip until something needs persisting)

### Phase 3 — Ship (optional)

- [ ] CI
- [ ] Documentation beyond this README
- [ ] Docker
- [ ] Deployment
