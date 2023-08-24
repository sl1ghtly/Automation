:: batch file to do 2 parts:
:: 1. run any program on 2 guest machines
:: 2. update guest machines if they are not updated
:: By: Eryk Gloginski

:: change the \VMware Player to \VMware Workstation when testing
:: this because I am using a different version for no errors

:: make output visible only and clear screen right after
@echo off
cls
echo "Part 1: "
C:
CD C:\Program Files (x86)\VMware\VMware Player
:: virtual machines must be on before continuing
:: start at 1, increment by 1, end at 2 and do command to run programs in guest machine to display xclock
FOR /L %%I IN (1,1,2) DO vmrun -T ws -gu eryk -gp 1234 runProgramInGuest "I:\VMs\VM%%I\VM%%I.vmx" -noWait /usr/bin/xclock -display :0
pause

echo "Part 2: "
:: I have made the updatescript.sh which can be pasted into the guest machine to run it however it does not run due to a bug in gnome or vmware
:: start at 1, increment by 1, end at 2 and do command to run program/script in guest machine to check for updates and update
FOR /L %%I IN (1,1,2) DO vmrun -T ws -gu eryk -gp 1234 runScriptInGuest "I:\VMs\VM%%I\VM%%I.vmx" -noWait /bin/bash /home/eryk/Desktop/updatescript.sh
pause
