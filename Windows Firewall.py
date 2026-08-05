netsh advfirewall set allprofiles state off
```

### Step-by-Step Guide

1. **Open Command Prompt as Admin**: Click Start, type **cmd**, right-click **Command Prompt**, and select **Run as administrator**.
2. **Turn Off All Profiles**: Copy, paste, and run the command above to disable the firewall entirely across public, private, and domain networks.
3. **Turn On Later**: For security, re-enable the firewall when you are done by running:
   ```cmd
   netsh advfirewall set allprofiles state on
   ```

### Turn Off Specific Network Profiles

If you do not want to turn off the entire firewall, you can target specific profiles instead:

* **Domain Network Only**: 
  ```cmd
  netsh advfirewall set domainprofile state off
  ```
* **Private Network Only**: 
  ```cmd
  netsh advfirewall set privateprofile state off
  ```
* **Public Network Only**: 
  ```cmd
  netsh advfirewall set publicprofile state off
  ```

### Alternative PowerShell Command
If you prefer using [Microsoft PowerShell](https://microsoft.com), run this command as an administrator:
```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

Would you like help **creating a specific rule** to allow a program through instead of turning the whole firewall off?
