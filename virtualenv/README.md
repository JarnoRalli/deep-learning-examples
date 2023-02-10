# Virtualenv

Virtualenv is a tool for creating isolated virtual Python environments.

## 1. Requirement Files

* **[financial.txt](./financial.txt)**. Requirements for the FinancialEngineering examples.

## 2. Installation

The proposed method for installing `virtualenv` is using `pipx`

```bash
pipx install virtualenv
```

## 3. Create a New Environment and Activate It

In order to create a new virtual environment, simple execute the following command:

```bash
virtualenv <NAME-OF-THE-ENVIRONMENT>
```

Above command will create a directory called `<NAME-OF-THE-ENVIRONMENT>` that contains all the packages etc.
of the virtual environment. In order to activate the virtual environment, execute the following:

```bash
source <NAME-OF-THE-ENVIRONMENT>/bin/activate
```

Once you have activated the virtual environment, you can install Python packages to it

```bash
pip install -r <PATH-TO-THE-REQUIREMENTS-FILE>
```

## 4. Deactivate an Environment

You can deactivate an activ virtual environment as using the following command:

```bash
deactivate
```
