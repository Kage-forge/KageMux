# ⚡ Python Forge: Environment Architecture

Follow these exact execution protocols to configure a clean, modern Python environment using the official Microsoft Store deployment. This method isolates your installation, preventing system path conflicts and broken registry variables.

### 🛠️ Step 1: Deploy the Official Manager
1. Open the **Microsoft Store** application on your Windows machine.
2. Search for **Python Install Manager** (verify the publisher is the Python Software Foundation).
3. Click **Install** to deploy the package.

### ⚙️ Step 2: Configure System Aliases
1. Open a new **Windows PowerShell** terminal. A green configuration helper prompt will appear automatically.
2. When prompted to modify App execution aliases, type `y` and press **Enter**.
3. The Windows Settings application will launch. Scroll down and verify that **Python (default)** and **Python install manager** are both toggled to **On**.
4. Close the Settings window and return to your PowerShell terminal.

### 📥 Step 3: Install the Python Runtime
1. The terminal will ask if you want to install the latest CPython runtime. Type `y` and press **Enter**.
2. Wait for the background installation to complete, then verify the deployment by executing:
```powershell
python --version
```

### 🔗 Step 4: Rebuild Path Variables (Critical)
Windows requires explicit pathing to locate your installed package tools. Run this PowerShell script to automate the path reconstruction. It will dynamically detect your active Python version.
1. Copy this entire code block:
```powershell
$PythonScripts = (Get-ChildItem -Path "$env:LOCALAPPDATA\Python\pythoncore-*\Scripts" -Directory | Select-Object -First 1).FullName
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($CurrentPath -notmatch [regex]::Escape($PythonScripts)) { [Environment]::SetEnvironmentVariable("Path", $CurrentPath + ";" + $PythonScripts, "User") }
```
2. Paste the block into PowerShell and press **Enter**.
3. **Close your PowerShell window entirely** and launch a fresh instance to load the new environment variables into system memory.

### 📦 Step 5: Deploy Core Packages
You are now ready to install your required media automation dependencies.
1. In your fresh PowerShell window, execute:
```powershell
python -m pip install --upgrade pip requests pymediainfo
```
2. Verify the package installation by running:
```powershell
pip list
```

---

### 🔄 Lifecycle Management: Updating Python
When a new stable version of Python is released, **do not** download a standalone installer from the web. The Python Install Manager handles lifecycle updates automatically. To upgrade your runtime without generating path redundancies, execute these steps:

1. **Scan for updates:** Run `py list --online` to view all available stable releases.
2. **Deploy the new runtime:** Run `py install <version>` (replacing `<version>` with the target build, such as `3.15`).
3. **Purge the old runtime:** Run `py uninstall <old_version>` (for example, `py uninstall 3.14`) to eradicate redundant binaries.
4. **Rebuild the architecture:** Execute the Step 4 path fix script again to update your system variables for the new version. Finally, run the Step 5 package command to compile your dependencies cleanly against the new environment.

Your Python Forge environment is now fully optimized and locked for production.