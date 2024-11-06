# Anaconda Installation Guide

Here are the steps to install Anaconda on your PC.

## Step 1: Download Anaconda

1. **Visit the Anaconda Website:**
   Go to the [Anaconda Distribution page](https://www.anaconda.com/products/distribution#download-section).
   Click "Skip registration" if don't want to regist.
   
3. **Choose Your Operating System:**
   Select the version appropriate for your operating system (Windows, macOS, or Linux).

4. **Download the Installer:**
   Click on the download button for the graphical installer or the command-line installer, depending on your preference.

## Step 2: Install Anaconda

1. **Run the Installer:**

   
   * Windows: Locate the downloaded `.exe` file and double-click it to run (Windows).
   * MacOS: Find the downloaded `.pkg` file and double-click it to start the installation.
   * Linux & MacOS: Type the following command (replace `Anaconda3-2023.XX-Linux-x86_64.sh` with the actual filename):
   ```bash
   bash Anaconda3-2023.XX-Linux-x86_64.sh (MaOS)

---
# Anacondaインストールガイド

## ステップ1: Anacondaのダウンロード

1. **Anacondaのウェブサイトにアクセス:**
   [Anaconda Distributionページ](https://www.anaconda.com/products/distribution#download-section)に移動します。
   登録したくない場合は「Skip registration」をクリックしてください。

2. **オペレーティングシステムを選択:**
   自分のオペレーティングシステム（Windows、macOS、Linux）に適したバージョンを選びます。

3. **インストーラーをダウンロード:**
   グラフィカルインストーラーまたはコマンドラインインストーラーのダウンロードボタンをクリックします。

## ステップ2: Anacondaのインストール

1. **インストーラーを実行:**

   * Windows: ダウンロードした`.exe`ファイルを見つけ、ダブルクリックして実行します。
   * macOS: ダウンロードした`.pkg`ファイルを見つけ、ダブルクリックしてインストールを開始します。
   * Linux & macOS: 以下のコマンドを入力します（`Anaconda3-2023.XX-Linux-x86_64.sh`を実際のファイル名に置き換えてください）:
   ```bash
   bash Anaconda3-2023.XX-Linux-x86_64.sh (Linux)
----

# Install xarray and cartopy

To install Xarray, run the following command:

- `conda install -c conda-forge xarray`
- `conda install -c conda-forge cartopy`

Verify the Installation
To confirm that Xarray and Cartopy have been installed correctly, open a Python environment (e.g., using Anaconda Prompt or any Python IDE) and run the following commands:

- `python`
- `import xarray as xr`
- `import cartopy`

---
# xarrayとCartopyのインストール

Xarrayをインストールするには、以下のコマンドを実行します:

- `conda install -c conda-forge xarray`
- `conda install -c conda-forge cartopy`

## インストールの確認

XarrayとCartopyが正しくインストールされたか確認するには、Python環境を開き（Anaconda Promptや任意のPython IDEを使用）、以下のコマンドを実行します:

- `python`
- `import xarray as xr`
- `import cartopy`

